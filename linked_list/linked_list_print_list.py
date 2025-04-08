class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        value (any): The data stored in this node.
        next (Node or None): A reference to the next node in the list, or None if this is the last node.
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
    A class that implements a singly linked list.

    Attributes:
        head (Node or None): The first node in the list.
        tail (Node or None): The last node in the list.
        length (int): The total number of nodes in the list.
    """

    def __init__(self, value):
        """
        Initializes the linked list with a single node.

        Args:
            value (any): The value to be stored in the first node of the list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the value of each node in the list, starting from the head and moving to the tail.

        This function traverses the entire list and outputs each value on a separate line.
        If the list is empty, nothing will be printed.
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds a new node with the specified value at the end (tail) of the linked list.

        If the list is empty, the new node becomes both the head and the tail.
        Otherwise, it is linked to the current tail and becomes the new tail.

        Args:
            value (any): The value to be added to the list.

        Returns:
            bool: True if the node was successfully appended.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


# Example usage
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(33)
my_linked_list.append(7)

my_linked_list.print_list()
