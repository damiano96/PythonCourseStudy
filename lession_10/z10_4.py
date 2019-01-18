import unittest


class Queue:
    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise IndexError("Kolejka pelna")
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise IndexError("Pusta kolejka")
        else:
            data = self.items[self.head]
            self.items[self.head] = None      # usuwam referencję
            self.head = (self.head + 1) % self.n
            return data


class TestQueue(unittest.TestCase):

    def test_is_full(self):
        a = Queue(1)
        a.put(4)
        self.assertTrue(a.is_full())
        a = Queue(2)
        a.put(4)
        self.assertFalse(a.is_full())

    def test_is_empty(self):
        a = Queue(1)
        self.assertTrue(a.is_empty())
        a = Queue(3)
        a.put(4)
        self.assertFalse(a.is_empty())

    def test_getWithRaisesError(self):
        a = Queue(4)
        self.assertRaises(LookupError, lambda: a.get())

    def test_putWithRaiseError(self):
        a = Queue(1)
        a.put(4)
        self.assertRaises(LookupError, lambda: a.put(2))


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
