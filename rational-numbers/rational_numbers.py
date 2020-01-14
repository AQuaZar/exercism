from __future__ import division
import math


class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        if gcd != 1:
            numer = numer / gcd
            denom = denom / gcd
        if denom < 0:
            denom = denom * -1
            numer = numer * -1

        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        n = self.numer * other.denom + self.denom * other.numer
        d = self.denom * other.denom

        return Rational(n, d)

    def __sub__(self, other):
        n = self.numer * other.denom - self.denom * other.numer
        d = self.denom * other.denom
        return Rational(n, d)

    def __mul__(self, other):
        n = self.numer * other.numer
        d = self.denom * other.denom
        return Rational(n, d)

    def __truediv__(self, other):
        if self.denom * other.numer != 0:
            n = self.numer * other.denom
            d = self.denom * other.numer
            return Rational(n, d)
        else:
            raise ZeroDivisionError

    def __abs__(self):
        n = abs(self.numer)
        d = abs(self.denom)
        return Rational(n, d)

    def __pow__(self, power):
        if power >= 0:
            n = self.numer ** power
            d = self.denom ** power
        elif power < 0:
            n = self.denom ** abs(power)
            d = self.numer ** abs(power)
        return Rational(n, d)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)

