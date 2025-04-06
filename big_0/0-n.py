def print_item(n):
    """
    Prints integers from 0 up to n-1 in O(n) linear time.

    Args:
        n (int): The upper bound (exclusive) for the range of numbers to print.

    Returns:
        None

    Time Complexity:
        O(n): Linear time, directly proportional to the input size n.
    """
    for i in range(n):
        print(i)


print(print_item(10))