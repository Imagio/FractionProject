def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

class Fraction(object):
    def __init__(self, a, b):
        self.top = a
        self.bottom = b
        t = gcd(self.top, self.bottom)
        self.top //= t
        self.bottom //= t

    def __add__(self, other):
        x = self
        y = other
        if type(y) == int:
            y = fraction(y)
        t = lcm(x.bottom, y.bottom)
        kx = t // x.bottom
        ky = t // y.bottom
        return Fraction(kx * x.top + ky * y.top, t)




def fraction(a, b=1):
    if type(a) != int:
        raise Exception("Invalid argument")
    return Fraction(a, b)




