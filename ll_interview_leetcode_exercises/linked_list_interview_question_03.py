"""
003 LL Has Loop ( Interview Question)
Instructions

Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the
linked list.

You are required to use Floyd's cycle-finding algorithm (also known as the
"tortoise and the hare" algorithm) to detect the loop.

This algorithm uses two pointers: a slow pointer and a fast pointer. The slow
pointer moves one step at a time, while the fast pointer moves two steps at a
time. If there is a loop in the linked list, the two pointers will eventually
meet at some point. If there is no loop, the fast pointer will reach the end
of the list.

The method should follow these guidelines:



1.Create two pointers, slow and fast, both initially pointing to the head of
the linked list.

2.Traverse the list with the slow pointer moving one step at a time, while the
fast pointer moves two steps at a time.

3.If there is a loop in the list, the fast pointer will eventually meet the
slow pointer. If this occurs, the method should return True.

4.If the fast pointer reaches the end of the list or encounters a None value,
it means there is no loop in the list. In this case, the method should
return False.



If your Linked List contains a loop, it indicates a flaw in its implementation.
This situation can manifest in several ways:
"""


class Node:
    """
    Represents a node in a singly linked list.

    Each node contains a value and a reference to the next node in the sequence.
    This class is used as the building block for the LinkedList class.

    Attributes:
        value (any): The data stored in the node.
        next (Node or None): A reference to the next node in the list, or
        None if this is the last node.
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

    def has_loop(self):
        """
        Detects whether the singly linked list contains a loop (cycle).

        This method implements Floyd’s Cycle-Finding Algorithm, also known
        as the "tortoise and hare" algorithm. It uses two pointers:
        - `slow` moves one node at a time.
        - `fast` moves two nodes at a time.

        If there is no loop in the list, the `fast` pointer will eventually
        reach the end (`None`). However, if a loop exists, the `fast` pointer
        will eventually meet the `slow` pointer within the loop, and the
        method will return True.

        Returns:
            bool: True if a loop is detected in the linked list,
                  False otherwise.

        Time Complexity:
            O(n) - In the worst case, each node is visited at most once.

        Space Complexity:
            O(1) - Only two pointers are used, no additional memory is required.
        """
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)

my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())  # Returns True

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False
