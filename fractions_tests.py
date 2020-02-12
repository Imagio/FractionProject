import unittest
from fractions import *


class InitTestCase(unittest.TestCase):
    def test_ab(self):
        x = fraction(1, 2)
        self.assertEqual(x.top, 1)
        self.assertEqual(x.bottom, 2)

    def test_a(self):
        x = fraction(4)
        self.assertEqual(x.top, 4)
        self.assertEqual(x.bottom, 1)


if __name__ == '__main__':
    unittest.main()
