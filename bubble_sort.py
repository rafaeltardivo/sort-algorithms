def first_bubble_sort(numbers):
    """First implementation of bubble sort. This one does not have any
    optimization and it is considered to be the worst one. The iteration
    counter will be present to show the difference between each implemen
    tation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        iterations (int): number of iterations the algorithm took to order
        the list.
    """
    size = len(numbers)
    iterations = 0

    for i in range(size - 1):
        iterations += 1
        for j in range(size - 1):
            iterations += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return iterations


def second_bubble_sort(numbers):
    """Second implementation of bubble sort. Contains the first optimization:
    excluding the last sorted item at each iteration. The iteration counter
    will be present to show the difference between each implementation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        iterations (int): number of iterations the algorithm took to order
        the list.
    """
    size = len(numbers)
    iterations = 0

    for i in range(size - 1):
        iterations += 1
        for j in range(size - i - 1):
            iterations += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return iterations


if __name__ == "__main__":
    first_numbers = [6, 3, 7, 8, 9]

    iterations = first_bubble_sort(first_numbers)
    print(
        f"first_bubble_sort result: {first_numbers}."
        f" Sorted after {iterations} iterations."
    )

    second_numbers = [6, 3, 7, 8, 9]

    iterations = second_bubble_sort(second_numbers)
    print(
        f"second_bubble_sort result: {second_numbers}."
        f" Sorted after {iterations} iterations."
    )
