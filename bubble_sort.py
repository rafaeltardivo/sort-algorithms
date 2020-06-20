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

    for i in range(size -1):
        iterations += 1
        for j in range(size -1):
            iterations += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return iterations


if __name__ == '__main__':
    first_numbers = [7, 3, 6, 2, 0]

    iterations = first_bubble_sort(first_numbers)
    print(
        f'first_bubble_sort result: {first_numbers}.'
        f' Sorted after {iterations} iterations.'
    )