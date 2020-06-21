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
    """Non recursive second implementation of insertion sort.This one contains
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


if __name__ == "__main__":
    numbers, iterations = first_insertion_sort([6, 3, 7, 8, 9])
    print(
        f"first_insertion_sort result:  {numbers}."
        f" Sorted after {iterations} iterations."
    )

    numbers, iterations = second_insertion_sort([6, 3, 7, 8, 9])
    print(
        f"second_insertion_sort result:  {numbers}."
        f" Sorted after {iterations} iterations."
    )
