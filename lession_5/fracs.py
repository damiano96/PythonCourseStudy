import unittest


def add_frac(frac1, frac2):         # frac1 + frac2
    if frac1[1] == frac2[1]:
        return [frac1[0] + frac2[0], frac1[1]]
    else:
        denominator = frac1[1] * frac2[1]
        numerator1 = frac1[0] * frac2[1]
        numerator2 = frac2[0] * frac1[1]
        return [numerator1 + numerator2, denominator]


def sub_frac(frac1, frac2):         # frac1 - frac2
    if frac1[1] == frac2[1]:
        return [frac1[0] - frac2[0], frac1[1]]
    else:
        denominator = frac1[1] * frac2[1]
        numerator1 = frac1[0] * frac2[1]
        numerator2 = frac2[0] * frac1[1]
        return [numerator1 - numerator2, denominator]


def mul_frac(frac1, frac2):         # frac1 * frac2
    return [frac1[0]*frac2[0], frac1[1]*frac2[1]]


def div_frac(frac1, frac2):         # frac1 / frac2
    return [frac1[0] * frac2[1], frac1[1] * frac2[0]]


def is_positive(frac):              # bool, czy dodatni
    if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0):
        return True
    else:
        return False


def is_zero(frac):                  # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    if frac2float(frac1) == frac2float(frac2):
        return 0
    if frac2float(frac1) > frac2float(frac2):
        return 1
    if frac2float(frac1) < frac2float(frac2):
        return -1


def frac2float(frac):               # konwersja do float
    return float(frac[0]) / float(frac[1])


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 5], [2, 5]), [3, 5])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([4, 7], [2, 7]), [2, 7])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([-3, -4]), True)
        self.assertEqual(is_positive([-3, 4]), False)
        self.assertEqual(is_positive([3, 4]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 4]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 4]), 1)
        self.assertEqual(cmp_frac([1, 2], [3, 6]), 0)
        self.assertEqual(cmp_frac([1, 2], [3, 4]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 8]), 0.125)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
