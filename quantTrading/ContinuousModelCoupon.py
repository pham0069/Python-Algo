from math import exp

class Bond:
    def __init__(self, principal, rate, maturity, interest_rate):
        self.principal = principal
        self.rate = rate / 100
        self.maturity = maturity
        self.interest_rate = interest_rate / 100

    def present_value(self, x, t):
        return x*exp(-self.interest_rate*t)

    def calculate_price(self):
        price = 0

        # discount coupons
        for t in range(1, self.maturity+1):
            price = price + self.present_value(self.principal*self.rate, t)

        # discount principal
        price = price + self.present_value(self.principal, self.maturity)

        return price

if __name__ == '__main__':
    zeroCouponBond = Bond(1000, 0, 2, 4)
    couponBond = Bond(1000, 10, 3, 4)
    print("Buy zero coupon bond at %.2f" % zeroCouponBond.calculate_price())
    print("Buy coupon bond at %.2f" % couponBond.calculate_price())
