import unittest
import random as rnd

class RandomQueue:
    def __init__(self, size=10):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0

    def insert(self, item):
        if self.is_full():
            raise IndexError("Kolejka pelna")
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise IndexError("Pusta kolejka")

        x = rnd.randint(self.head, (self.tail-1))
        data = self.items[x]
        help_variable = self.items[self.head]
        self.items[self.head] = self.items[x]
        self.items[x] = help_variable
        self.items[self.head] = None  # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail


class TestRandomQueue(unittest.TestCase):

    def test_is_empty_false(self):
        random = RandomQueue(3)
        random.insert(3)
        random.insert(5)
        random.remove()
        self.assertFalse(random.is_empty())

    def test_is_empty_true(self):
        random = RandomQueue(2)
        random.insert(1)
        random.insert(6)
        random.remove()
        random.remove()
        self.assertTrue(random.is_empty())

    def test_remove_None(self):
        random = RandomQueue(4)
        random.insert(1)
        random.insert(6)
        random.insert(2)
        random.insert(4)
        for i in range(4):
            self.assertNotEqual(None, random.remove())



if __name__ == "__main__":
    unittest.main()     # wszystkie testy