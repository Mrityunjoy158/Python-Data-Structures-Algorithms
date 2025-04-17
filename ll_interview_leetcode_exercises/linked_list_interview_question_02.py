"""
002 LL Find Middle Node ( Interview Question)
Instructions
Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the
second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves
one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow
 pointer should be at the middle node of the list.

The method should return the middle node when the number of nodes is odd or
the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can
only use one loop."""


class Node:
    """
    Represents a node in a singly linked list.

    Each node contains a value and a reference to the next node in the sequence.
    This class is used as the building block for the LinkedList class.

    Attributes:
        value (any): The data stored in the node.
        next (Node or None): A reference to the next node in the list, or None if this is the last node.

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

    def find_middle_node(self):
        """
        Finds and returns the middle node of a singly linked list.

        This method uses the two-pointer technique (also known as the
        tortoise and hare algorithm). It initializes two pointers, `slow`
        and `fast`, both starting at the head of the linked list. The `slow`
        pointer moves one step at a time, while the `fast` pointer moves two
        steps at a time. When the `fast` pointer reaches the end of the list,
        the `slow` pointer will be at the middle.

        Returns:
            Node: The middle node of the linked list. If the list has an
                  even number of nodes, it returns the second middle node.

        Time Complexity:
            O(n) - The list is traversed only once.

        Space Complexity:
            O(1) - Constant space is used regardless of the list size.
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)
