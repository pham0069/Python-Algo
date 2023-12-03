from math import exp

def future_discrete_value(x, r, n):
    return x*(1+r)**n

def present_discrete_value(x, r, n):
    return x*(1+r)**-n

def future_continuous_value(x, r, t):
    return x*exp(r*t)

def present_continuous_value(x, r, t):
    return x*exp(-r*t)

if __name__ == '__main__':
    # amount of money
    x = 100
    # interest rate
    r = 0.05
    # number of years
    n = 5

    print("Future values (discrete) of x: %s" % future_discrete_value(x, r, n))
    print("Present values (discrete) of x: %s" % present_discrete_value(x, r, n))
    print("Future values (discrete) of x: %s" % future_continuous_value(x, r, n))
    print("Present values (discrete) of x: %s" % present_continuous_value(x, r, n))
