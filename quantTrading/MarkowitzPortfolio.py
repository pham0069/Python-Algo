import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# ~ 365*5/7 - holidays
NUM_TRADING_DAYS = 252

# number of portfolios to be generated randomly
NUM_PORTFOLIOS = 10000

# stocks to handle
stocks = ['AAPL', 'WMT', "TSLA", 'GE', 'AMZ', 'DB']

# historical data - define START and END dates
start_date = '2016-01-01'
end_date = '2017-01-01'

def download_data():
    # name of stock (key) - stock values (2010-2017) as the values
    stock_data = {}

    for stock in stocks:
        # closing prices
        ticker = yf.Ticker(stock)
        print("Downloaded ticker for", stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']

    return pd.DataFrame(stock_data)

def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show()

# daily
def calculate_stock_return(data):
    # use ln for normalization - to measure all variables in comparable metrics
    # data  =>          1 2 3 4 5
    # data shift 1 =>     1 2 3 4
    # equivalent to data[t]/data[t-1]
    # the first row value will be not available
    log_return = np.log(data/data.shift(1))

    # filter the first row (NAN)
    return log_return[1:]

def show_stock_return(returns):
    # yearly return
    print(returns.mean() * NUM_TRADING_DAYS)
    print(returns.cov() * NUM_TRADING_DAYS)

# annually
def calculate_portfolio_return(returns, weights):
    return np.sum(returns.mean() * weights) * NUM_TRADING_DAYS

# annually
def calculate_portfolio_volatility(returns, weights):
    return np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))

def generate_portfolios(returns):
    portfolio_weights = []
    portfolio_means = []
    portfolio_risks = []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(stocks))
        w /= np.sum(w) # normalize
        portfolio_weights.append(w)
        portfolio_means.append(calculate_portfolio_return(returns, w))
        portfolio_risks.append(calculate_portfolio_volatility(returns, w))

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)

def show_portfolios(returns, volatilities):
    plt.figure(figsize=(10, 6))
    plt.scatter(volatilities, returns, c=returns/volatilities, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()

# assume Rf = 0 (return rate of risk-free asset)
def calculate_sharpe(returns, weights):
    return calculate_portfolio_return(returns, weights)/calculate_portfolio_volatility(returns, weights)

# we want to get max sharpe ~ min (-sharpe)
def min_sharpe_function(weights, returns):
    return - calculate_sharpe(returns, weights)

def statistics(weights, returns):
    return np.array([calculate_portfolio_return(returns, weights),
          calculate_portfolio_volatility(returns, weights),
          calculate_sharpe(returns, weights)])

def optimize_portfolio(returns, portfolio_weights):
    # the sum of weights is 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    # the weights can be 1 at most: 1 when 100% of money is invested into a single stock
    bounds = tuple((0, 1) for _ in range(len(stocks)))
    return optimization.minimize(fun=min_sharpe_function, x0=portfolio_weights[0], args=returns
                                 , method='SLSQP', bounds=bounds, constraints=constraints)

def print_optimal_portfolio(optimum, returns):
    weights = optimum['x'].round(3)
    print("Optimal portfolio: ", weights)
    print("Expected return, volatility and Sharpe ratio: ", statistics(weights, returns))


def show_optimal_portfolio(opt, rets, portfolio_rets, portfolio_vols):
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_vols, portfolio_rets, c=portfolio_rets / portfolio_vols, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(opt['x'], rets)[1], statistics(opt['x'], rets)[0], 'g*', markersize=20.0)
    plt.show()


if __name__ == '__main__':

    dataset = download_data()
    # show_data(dataset)

    log_daily_returns = calculate_stock_return(dataset)
    # show_return(log_daily_returns)

    portfolio_weights, portfolio_means, portfolio_risks = generate_portfolios(log_daily_returns)
    show_portfolios(portfolio_means, portfolio_risks)

    optimum = optimize_portfolio(log_daily_returns, portfolio_weights)
    print_optimal_portfolio(optimum, log_daily_returns)
    show_optimal_portfolio(optimum, log_daily_returns, portfolio_means, portfolio_risks)

