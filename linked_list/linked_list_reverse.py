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

    def prepend(self, value):
        """
            Adds a new node containing the specified value to the beginning of the linked list.

            This operation updates the head of the list to point to the new node. If the list
            was previously empty, both the head and tail references are set to this new node.

            Parameters:
                value (any): The value to be stored in the new node.

            Behavior:
                - A new Node instance is created with the provided value.
                - If the list is empty (length == 0), the new node becomes both the head and tail.
                - If the list is not empty, the new node's `next` is set to the current head, and
                  then the head is updated to this new node.
                - The length of the list is incremented by 1.

            Returns:
                bool: Returns True to indicate the node was successfully added to the list.

            Time Complexity:
                O(1) — Constant time operation, as it doesn't require traversal of the list.
            """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes and returns the first node's value from the beginning (head) of the linked list.

        This operation updates the head to point to the next node. If the list becomes empty
        after the operation, the tail is also set to None.

        Returns:
            any or None: The value of the removed node. Returns None if the list is already empty.

        Behavior:
            - If the list is empty (length == 0), return None.
            - Otherwise:
                - Store the current head node in a temporary variable.
                - Update the head to the next node.
                - Detach the removed node's `next` reference (for cleanup).
                - Decrement the list's length.
                - If the list becomes empty after the operation, set tail to None.
            - Return the value of the removed node.

        Time Complexity:
            O(1) — Constant time operation, as it only involves updating references.
        """
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # If the list becomes empty after popping
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        """
        Retrieves the value of the node at a specific index in the linked list.

        This method accesses the node located at the provided zero-based index and returns its value.
        If the index is invalid (i.e., less than 0 or greater than or equal to the length of the list),
        the method returns None.

        Parameters:
            index (int): The position of the node whose value is to be retrieved. Indexing starts from 0.

        Returns:
            any or None: The value stored at the specified index if valid; otherwise, None.

        Behavior:
            - Checks if the index is within the valid range [0, length - 1].
            - If the index is invalid, returns None.
            - If the index is valid:
                - Starts from the head node.
                - Traverses the list node-by-node until reaching the target index.
                - Returns the value stored in the corresponding node.

        Time Complexity:
            O(n) — Linear time, as it may require traversal from the head to the specified index.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        Updates the value of the node at the specified index in the linked list.

        This method attempts to access the node at the given index using the `get()` method.
        If the node exists (i.e., the index is within the bounds of the list), it updates
        the node's `value` attribute with the provided value and returns True. If the index
        is out of bounds, or the node does not exist, the method returns False.

        Parameters:
            index (int): The zero-based position of the node in the linked list whose value should be updated.
            value (Any): The new value to assign to the node at the specified index.

        Returns:
            bool:
                - True if the value was successfully updated.
                - False if the index is invalid (e.g., negative or beyond the list's length).
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Removes and returns the node at the specified index in the linked list.

        This method handles removal from three cases:
        1. The head (index == 0): Calls `pop_first()`.
        2. The tail (index == length - 1): Calls `pop()`.
        3. Any middle index: Traverses to the node before the target, updates the pointer to skip the target node.

        Parameters:
        ----------
        index : int
            The position of the node to be removed. Index must be in the range [0, length - 1].

        Returns:
        -------
        Node or None
            The removed node if the index is valid. Returns `None` if the index is out of bounds.

        Side Effects:
        ------------
        Decreases the `length` of the linked list by 1 if a node is successfully removed.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """
        Reverses the order of the linked list in place.

        This method swaps the head and tail of the linked list and then
        iterates through the list, reversing the direction of the `next` pointers
        for each node.

        Example:
            Given a linked list: 1 -> 2 -> 3 -> 4
            After calling reverse(), the list becomes: 4 -> 3 -> 2 -> 1

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1), as the reversal is done in place without using extra memory.

        Returns:
            None
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()
