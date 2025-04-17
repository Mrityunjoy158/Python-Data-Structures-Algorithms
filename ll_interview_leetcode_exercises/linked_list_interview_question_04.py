"""
004 LL Find Kth Node From End ( Interview Question)
Instructions

Implement the find_kth_from_end function, which takes the LinkedList (ll) and
an integer k as input, and returns the k-th node from the end of the linked
list WITHOUT USING LENGTH.

Given this LinkedList:
1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains
the value of 4.

If k=2 then return the second node from the end which contains the value of 3,
etc.

If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

1.The function should utilize two pointers, slow and fast, initialized to the
head of the linked list.

2.The fast pointer should move k nodes ahead in the list.

3.If the fast pointer becomes None before moving k nodes, the function should
return None, as the list is shorter than k nodes.

4.The slow and fast pointers should then move forward in the list at the same
time until the fast pointer reaches the end of the list.

5.The function should return the slow pointer, which will be at the k-th
position from the end of the list.

This is a separate function that is not a method within the LinkedList class.
This means you need to indent the function all the way to the LEFT.
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


def find_kth_from_end(ll, k):
    """
    Finds the k-th node from the end in a singly linked list.

    This method uses the two-pointer technique. It first advances the
    `fast` pointer by `k` nodes. Then, both `slow` and `fast` pointers
    move one node at a time until `fast` reaches the end of the list.
    At this point, the `slow` pointer will be at the k-th node from the end.

    Args:
        ll (LinkedList): The linked list to search in.
        k (int): The position from the end (1-based index). For example,
                 k=1 returns the last node, k=2 returns the second to last, etc.

    Returns:
        Node: The k-th node from the end of the linked list.
              Returns None if k is greater than the length of the list.

    Raises:
        ValueError: If `k` is not a positive integer.

    Time Complexity:
        O(n) - The list is traversed once.

    Space Complexity:
        O(1) - Only two pointers are used.

    Example:
        For linked list: 10 -> 20 -> 30 -> 40 -> 50
        - find_kth_from_end(ll, 2) returns the node with value 40
    """
    if k <= 0:
        raise ValueError("k must be a positive integer")

    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)  # Output: 4
