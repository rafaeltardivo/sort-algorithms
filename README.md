# Sort Algorithms

A collection of sorting algorithms implemented in pure Python, featuring multiple implementations of each algorithm with different optimizations.

## Implemented Algorithms

### Bubble Sort
Multiple implementations with increasing optimizations:
- `first_bubble_sort`: Basic implementation without optimizations
- `second_bubble_sort`: Optimized by excluding already sorted elements
- `third_bubble_sort`: Further optimized with early termination if no swaps occur
- `recursive_bubble_sort`: Recursive implementation

### Insertion Sort
Multiple implementations with different optimizations:
- `first_insertion_sort`: Basic implementation without optimizations
- `second_insertion_sort`: Optimized by checking if previous element is greater
- `recursive_insertion_sort`: Recursive implementation

## Features

- Each implementation returns both the sorted list and the number of iterations performed
- Comprehensive test cases covering:
  - Empty lists
  - Single-element lists
  - Lists with duplicate elements
  - Reverse-sorted lists
  - Lists with negative numbers
- Input validation to ensure proper data types
- Consistent return values across all implementations
- Detailed docstrings and comments

## Usage

Each sorting algorithm can be imported and used independently:

```python
from bubble_sort import first_bubble_sort, second_bubble_sort, third_bubble_sort, recursive_bubble_sort
from insertion_sort import first_insertion_sort, second_insertion_sort, recursive_insertion_sort

# Example usage
numbers = [6, 3, 7, 8, 9]
sorted_numbers, iterations = first_bubble_sort(numbers.copy())
print(f"Sorted numbers: {sorted_numbers}")
print(f"Iterations: {iterations}")
```

## Running Tests

To run the test cases for all implementations:

```bash
python bubble_sort.py
python insertion_sort.py
```

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.