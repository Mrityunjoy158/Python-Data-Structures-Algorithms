class Node:
    """
    Represents a node in a singly linked list.

    Each node contains a value and a reference to the next node in the sequence.
    This class is used as the building block for the LinkedList class.

    Attributes:
        value (any): The data stored in the node.
        next (Node or None): A reference to the next node in the list, or None if this is the last node.

    Example:
        >>> node = Node(5)
        >>> print(node.value)
        5
        >>> print(node.next)
        None
    """
    def __init__(self, value):
        """
        Initializes a Node with the given value.

        Args:
            value (any): The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    A singly linked list data structure for storing ordered elements.

    The linked list maintains a sequence of nodes, where each node contains a value
    and a reference to the next node. It supports operations such as appending nodes
    to the end and removing nodes from the end. The list tracks its head (first node),
    tail (last node), and length (number of nodes).

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
        >>> print(ll.pop().value)
        2
        >>> print(ll.length)
        1
    """
    def __init__(self, value):
        """
        Initializes the linked list with a single node containing the given value.

        Args:
            value (any): The initial value to store in the first node of the list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the values of all nodes in the list from head to tail.

        Iterates through the list starting from the head and prints each node's value
        on a new line. If the list is empty, nothing is printed.

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

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        Creates a new node with the specified value and adds it after the current tail.
        Updates the tail reference and increments the list's length. Handles the case
        where the list is empty by setting the new node as both head and tail.

        Args:
            value (any): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully appended.

        Example:
            >>> ll = LinkedList(1)
            >>> ll.append(2)
            True
            >>> ll.print_list()
            1
            2
            >>> print(ll.length)
            2
        """
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, the new node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Link the current tail to the new node and update the tail reference
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Removes and returns the last node of the list.

        Traverses the list to find the last node, removes it by updating the second-to-last
        node's next reference to None, and sets the second-to-last node as the new tail.
        Decrements the list's length and handles edge cases, such as when the list has
        only one node or is empty.

        Returns:
            Node or None: The removed node if the list is not empty; otherwise, None.

        Example:
            >>> ll = LinkedList(1)
            >>> ll.append(2)
            True
            >>> print(ll.pop().value)
            2
            >>> print(ll.pop().value)
            1
            >>> print(ll.pop())
            None
            >>> print(ll.length)
            0
        """
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # If the list becomes empty after popping
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


# Example usage
my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)  # Output: 2
# (1) Item - Returns 1 Node
print(my_linked_list.pop().value)  # Output: 1
# (0) Items - Returns None
print(my_linked_list.pop())        # Output: None
