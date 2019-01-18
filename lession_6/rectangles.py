import math

from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "[({0}, {1}), ({2}, {3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}), ({2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

    def area(self):             # pole powierzchni
        a = math.sqrt(math.pow(self.pt2.x - self.pt1.x, 2) + math.pow(self.pt1.y - self.pt1.y, 2))
        b = math.sqrt(math.pow(self.pt2.x - self.pt2.x, 2) + math.pow(self.pt2.y - self.pt1.y, 2))
        return a*b

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

# Kod testujący moduł.


class TestRectangle(unittest.TestCase):
    def setUp(self): pass

    def test_print(self):
        self.assertEqual(Rectangle(2, 3, 4, 5).__str__(), "[(2, 3), (4, 5)]")
        self.assertEqual(Rectangle(1, 3, 3, 6).__str__(), "[(1, 3), (3, 6)]")
        self.assertEqual(Rectangle(3, 5, 6, 8).__repr__(), "Rectangle(3, 5), (6, 8)")
        self.assertEqual(Rectangle(4, 2, 1, 7).__repr__(), "Rectangle(4, 2), (1, 7)")

    def test_cmp(self):
        self.assertTrue(Rectangle(2, 3, 4, 5) == Rectangle(2, 3, 4, 5))
        self.assertTrue(Rectangle(1, 4, 6, 8) == Rectangle(1, 4, 6, 8))
        self.assertTrue(Rectangle(1, 4, 6, 8) != Rectangle(1, 2, 3, 5))
        self.assertTrue(Rectangle(2, 6, 1, 8) != Rectangle(1, 4, 6, 8))

    def test_center(self):
        self.assertEqual(Rectangle(3, 5, 6, 8).center(), Point(4.5, 6.5))
        self.assertEqual(Rectangle(3, 5, 6, 8).center(), Point(4.5, 6.5))

    def test_area(self):
        self.assertEqual(Rectangle(1, 1, 3, 6).area(), 10)
        self.assertEqual(Rectangle(3, 5, 6, 8).area(), 9)

    def test_move(self):
        self.assertEqual(Rectangle(5, 4, 6, 7).move(4, 3), Rectangle(9, 7, 10, 10))
        self.assertEqual(Rectangle(2, 1, 4, 8).move(1, 2), Rectangle(3, 3, 5, 10))

    def tearDown(self): pass

    if __name__ == "__main__":
        unittest.main()