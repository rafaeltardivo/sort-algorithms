def first_bubble_sort(numbers):
    """First implementation of bubble sort. This one does not have any
    optimization and it is considered to be the worst one. The iteration
    counter will be present to show the difference between each implemen
    tation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
        iterations (int): number of iterations the algorithm took to sort
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
    return numbers, iterations


def second_bubble_sort(numbers):
    """Second implementation of bubble sort. Contains the first optimization:
    excluding the last sorted item at each iteration. The iteration counter
    will be present to show the difference between each implementation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
        iterations (int): number of iterations the algorithm took to sort
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
    return numbers, iterations


def third_bubble_sort(numbers):
    """Third implementation of bubble sort. Contains the second optimization
    plus a new one: a boolean that indicated if any swap has been made. If
    not, the list is already sorted. The iteration counter will be present
    to show the difference between each implementation.

    Args:
        numbers (list): list of integers to be sorted.
    Returns:
        numbers (list): sorted list.
        iterations (int): number of iterations the algorithm took to sort
        the list.
    """
    size = len(numbers)
    iterations = 0

    for i in range(size - 1):
        swapped = False
        iterations += 1
        for j in range(size - i - 1):
            iterations += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers, iterations


if __name__ == "__main__":
    numbers, iterations = first_bubble_sort([6, 3, 7, 8, 9])
    print(
        f"first_bubble_sort result:  {numbers}."
        f" Sorted after {iterations} iterations."
    )

    numbers, iterations = second_bubble_sort([6, 3, 7, 8, 9])
    print(
        f"second_bubble_sort result: {numbers}."
        f" Sorted after {iterations} iterations."
    )

    numbers, iterations = third_bubble_sort([6, 3, 7, 8, 9])
    print(
        f"third bubble_sort result:  {numbers}."
        f" Sorted after {iterations} iterations."
    )
