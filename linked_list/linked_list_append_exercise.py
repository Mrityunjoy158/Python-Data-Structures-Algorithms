class Node:
    """
    A class representing a node in a singly linked list.

    Each node stores a value and a reference to the next node in the list, forming the basic
    building block of a singly linked list. The `next` attribute is None if the node is the
    last in the sequence.

    Attributes:
        value (any): The value stored in the node.
        next (Node or None): A reference to the next node in the list, or None if there is no next node.

    Example:
        >>> node = Node(10)
        >>> print(node.value)
        10
        >>> print(node.next)
        None
    """
    def __init__(self, value):
        """
        Initialize a new node with the given value.

        Args:
            value (any): The data to store in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    A singly linked list is a linear data structure where each element (node) points to the next,
    allowing for efficient insertion at the end. This implementation tracks the head (first node),
    tail (last node), and length (number of nodes) of the list. It supports operations like appending
    nodes, printing the list, and emptying the list.

    Attributes:
        head (Node or None): The first node in the list, or None if the list is empty.
        tail (Node or None): The last node in the list, or None if the list is empty.
        length (int): The number of nodes currently in the list.

    Example:
        >>> ll = LinkedList(1)
        >>> ll.append(2)
        True
        >>> ll.print_list()
        1
        2
        >>> print(ll.length)
        2
        >>> ll.make_empty()
        >>> print(ll.length)
        0
    """
    def __init__(self, value):
        """
        Initialize the linked list with a single node.

        Creates a new node with the given value and sets it as both the head and tail of the list,
        initializing the length to 1.

        Args:
            value (any): The value to store in the first node of the list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Print all the values in the linked list.

        Traverses the list from the head to the tail, printing the value of each node on a new line.
        If the list is empty (head is None), no output is produced.

        Example:
            >>> ll = LinkedList(1)
            >>> ll.append(2)
            True
            >>> ll.print_list()
            1
            2
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        """
        Empty the linked list by resetting it to an initial empty state.

        Sets the head and tail to None and the length to 0, effectively removing all nodes from the list.
        This operation does not explicitly delete the nodes but allows them to be garbage collected if no
        other references to them exist.

        Example:
            >>> ll = LinkedList(1)
            >>> ll.append(2)
            True
            >>> print(ll.length)
            2
            >>> ll.make_empty()
            >>> print(ll.length)
            0
            >>> print(ll.head)
            None
        """
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """
        Add a node with the given value to the end of the list.

        Creates a new node with the specified value and appends it to the end of the list. If the list
        is empty (head is None), the new node becomes both the head and tail. Otherwise, the new node
        is linked to the current tail, and the tail reference is updated. The length is incremented
        in either case.

        Args:
            value (any): The value to be stored in the new node.

        Returns:
            bool: True if the operation was successful.

        Example:
            >>> ll = LinkedList(1)
            >>> ll.append(2)
            True
            >>> print(ll.head.value)
            1
            >>> print(ll.tail.value)
            2
            >>> print(ll.length)
            2
            >>> ll.make_empty()
            >>> ll.append(3)
            True
            >>> print(ll.head.value)
            3
            >>> print(ll.tail.value)
            3
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


# Example usage:
my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()