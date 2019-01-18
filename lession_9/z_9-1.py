class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


#czesc implementowana#
def remove_head(node):
    if node is None:
        raise ValueError("Pusta lista")
    currenNode = node
    head = currenNode.next
    if head is None:
        node = None
        return None, currenNode
    else:
        node = None
        return head, currenNode


def remove_tail(node):
    if node is None:
        raise ValueError("Pusta lista")
    if node.next is None:
        return None, node
    head = node
    while node:
        if node.next.next is None:
            currentNode = node.next
            node.next = None
            return head, currentNode
        node = node.next


head = None             #[]
head = Node(3, head)    #[3]
head = Node(5, head)    #[5->3]
head = Node(4, head)    #[4->5->3]
head = Node(1, head)    #[1->4->5->3]
head = Node(8, head)    #[8->1->4->5->3]



# Zastosowanie.
while head:
    #head, node = remove_head(head)
    head, node = remove_tail(head)
    print("usuwam", node)