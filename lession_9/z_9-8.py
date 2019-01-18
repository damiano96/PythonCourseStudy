class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:      # na prawo
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:    # na lewo
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass    # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


#czesc implementowana#
def bst_max(top):
    if top is None:
        raise ValueError("Puste drzewo")
    else:
        topReturn = top
        while top:
            if top.right is None:
                topReturn = top
            top = top.right
        return topReturn


def bst_min(top):
    if top is None:
        raise ValueError("Puste drzewo")
    else:
        topReturn = top
        while top:
            if top.left is None:
                topReturn = top
            top = top.left
        return topReturn


test_node = Node(6)
test_node.insert(3)
test_node.insert(1)
test_node.insert(19)
test_node.insert(7)
test_node.insert(8)
test_node.insert(11)
test_node.insert(10)
test_node.insert(15)
test_node.insert(2)

print(bst_max(test_node))
print(bst_min(test_node))