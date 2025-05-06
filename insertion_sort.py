def first_insertion_sort(numbers):
    """Non recursive first implementation of insertion sort.This one does
    not have any optimization and it is considered to be the worst one. The
    iteration counter will be present to show the difference between each
    implementation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
        iterations (int): number of iterations the algorithm took to sort
        the list.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
    """
    size = len(numbers)
    iterations = 0

    for i in range(size):
        iterations += 1
        j = i
        while j > 0:
            iterations += 1
            if numbers[j] < numbers[j - 1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
    return numbers, iterations


def second_insertion_sort(numbers):
    """Non recursive second implementation of insertion sort. This one contains
    the first optimization which checks if previous element is greater than
    current. iteration counter will be present to show the difference between
    each implementation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
        iterations (int): number of iterations the algorithm took to sort
        the list.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
    """
    size = len(numbers)
    iterations = 0

    for i in range(size):
        iterations += 1
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            iterations += 1
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
    return numbers, iterations


def recursive_insertion_sort(numbers, size=None, iterations=0):
    """Recursive implementation of insertion sort.
    
    Args:
        numbers (list): list of integers to be sorted.
        size (int, optional): size of the list. If None, will be calculated.
        iterations (int, optional): number of iterations performed.
    Returns:
        tuple: (sorted list, number of iterations)
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if size is None:
        size = len(numbers)
    
    if size == 1:
        return numbers, iterations

    iterations += 1
    for i in range(size):
        iterations += 1
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            iterations += 1
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
    return recursive_insertion_sort(numbers, size - 1, iterations)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [],  # Empty list
        [1],  # Single element
        [1, 1, 1],  # Duplicate elements
        [9, 8, 7, 6, 5],  # Reverse sorted
        [-1, -5, 3, 0, 2],  # Negative numbers
        [6, 3, 7, 8, 9],  # Original test case
    ]
    
    for test in test_cases:
        print(f"\nTesting with input: {test}")
        
        numbers, iterations = first_insertion_sort(test.copy())
        print(f"first_insertion_sort result: {numbers}. Sorted after {iterations} iterations.")

        numbers, iterations = second_insertion_sort(test.copy())
        print(f"second_insertion_sort result: {numbers}. Sorted after {iterations} iterations.")

        numbers, iterations = recursive_insertion_sort(test.copy())
        print(f"recursive_insertion_sort result: {numbers}. Sorted after {iterations} iterations.")
