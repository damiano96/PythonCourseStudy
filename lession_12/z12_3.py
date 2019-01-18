import math
import unittest


def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

    return L


def mediana_sort(L, left, right):
    if len(L) == 0:
        raise ValueError("Pusta Lista")
    L = bubble_sort(L)
    middle = (left+right)/2
    if middle.is_integer():
        return L[int(middle)]
    else:
        x = L[int(math.floor(middle))]
        y = L[int(math.ceil(middle))]
        return (x+y)/2


class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def testBinarySearch(self):
        #2,3,5,7,8 => 5
        L = [5, 3, 2, 7, 8]
        self.assertEqual(mediana_sort(L, 0, len(L)-1), 5)
        # 1,2,3,5,7,8 => [3,5]/2
        L = [5, 3, 2, 7, 8, 1]
        self.assertEqual(mediana_sort(L, 0, len(L) - 1), 4)
        # 1,2,3,5,6,7,8,9 => [5,6]/2
        L = [5, 3, 2, 7, 8, 1, 6, 9]
        self.assertEqual(mediana_sort(L, 0, len(L) - 1), 5.5)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
