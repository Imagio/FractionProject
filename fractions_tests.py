import unittest
from fractions import *


class InitTestCase(unittest.TestCase):
    def test_ab(self):
        x = fraction(1, 2)
        self.assertEqual(x.top, 1)
        self.assertEqual(x.bottom, 2)

    def test_gcd(self):
        x = fraction(39, 26)
        self.assertEqual(x.top, 3)
        self.assertEqual(x.bottom, 2)

    def test_a(self):
        x = fraction(4)
        self.assertEqual(x.top, 4)
        self.assertEqual(x.bottom, 1)

    def test_invalid_a(self):
        self.assertRaises(Exception, lambda: fraction(1.0))

class AddTestCase(unittest.TestCase):
    def test_add(self):
        a = fraction(1, 2)
        b = fraction(1, 3)
        c = a + b
        self.assertEqual(c.top, 5)
        self.assertEqual(c.bottom, 6)

    def test_add_int(self):
        a = fraction(1, 2)
        c = a + 3
        self.assertEqual(c.top, 7)
        self.assertEqual(c.bottom, 2)

if __name__ == '__main__':
    unittest.main()



