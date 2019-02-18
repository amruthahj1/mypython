from fractions import gcd

class fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.deno = denominator
    def __add__(self, other):
        self.sumOfn = self.num + other.num
        self.sumOfd = gcd(self.deno,other.deno)
        return(self.sumOfn, self.sumOfd)



print(fraction(1,4)+fraction(1,4))
