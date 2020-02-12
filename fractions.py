class Fraction(object):
    def __init__(self, a, b):
        self.top = a
        self.bottom = b


def fraction(a, b=1): return Fraction(a, b)
