class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node or None): The reference to the next node in the list.
    """

    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value (any): The value to store in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
        length (int): The number of nodes in the list.
    """

    def __init__(self, value):
        """
        Initializes a new linked list with a single node.

        Args:
            value (any): The value of the initial node in the list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(4)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
