import unittest


def binarne_rek(L, left, right, y): #zwraca numer indexu na ktorym znajduje sie dana liczba, jezeli jej nie ma zwracane jest -1
    if right >= left:     #sprawdzamy podstawowy warunek
        middle = left + (right - left) // 2
        if L[middle] == y:
            return middle
        elif L[middle] > y:  #jezeli element jest na indexie ponizej srdokowym, wowczas moze byc tylko na pozycji w lewo od middle
            return binarne_rek(L, left, middle-1, y)
        else:
            return binarne_rek(L, middle+1, right, y)  #jezeli element jest na indexie powyzej srdokowym, wowczas moze byc tylko na pozycji w prawo od middle

    else:
        return -1


class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def testBinarySearch(self):
        L = [2, 3, 4, 5, 10, 30, 40]
        y = 4
        self.assertEqual(binarne_rek(L, 0, len(L)-1, y), 2)
        y = 2
        self.assertEqual(binarne_rek(L, 0, len(L)-1, y), 0)
        y = 5
        self.assertEqual(binarne_rek(L, 0, len(L)-1, y), 3)
        y = 66
        self.assertEqual(binarne_rek(L, 0, len(L) - 1, y), -1)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()


