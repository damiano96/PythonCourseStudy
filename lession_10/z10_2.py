import unittest


class Stack:
    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n < self.size:
            self.items[self.n] = data
            self.n += 1
        else:
            raise IndexError("stos przepelniony")

    def pop(self):
        if self.n > 0:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencję
            return data
        else:
            raise IndexError("pusty stos")


class TestStack(unittest.TestCase):

    def test_init(self):
        self.assertEqual(Stack(1).size, 1)

    def test_push(self):
        stack = Stack(3)
        stack.push(4)
        self.assertFalse(stack.is_empty())

    def test_isEmpty(self):
        self.assertEqual(Stack(3).is_empty(), True)
        stack = Stack(5)
        stack.push(4)
        self.assertEqual(stack.is_empty(), False)

    def test_isFull(self):
        stack = Stack(5)
        stack.push(4)
        self.assertEqual(stack.is_full(), False)
        stack = Stack(2)
        stack.push(4)
        stack.push(1)
        self.assertEqual(stack.is_full(), True)

    def test_Pop(self):
        stack = Stack(3)
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)

    def test_popWithRaisesError(self):
        stack = Stack()
        self.assertRaises(LookupError, lambda: stack.pop())

    def test_pushWithRaisesError(self):
        stack = Stack(1)
        stack.push(3)
        self.assertRaises(LookupError, lambda: stack.push(5))


if __name__ == '__main__':
    unittest.main()