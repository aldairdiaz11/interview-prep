def binary_search_recursive(arr, left_pointer, right_pointer, target):
    if left_pointer >= right_pointer:
        return "value not found"

    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = arr[mid_idx]

    if mid_val == target:
        return mid_idx

    if mid_val > target:
        return binary_search_recursive(arr, left_pointer, mid_idx, target)

    if mid_val < target:
        return binary_search_recursive(arr, mid_idx + 1, right_pointer, target)


def binary_search_iterative(arr, target):
    left_pointer = 0
    right_pointer = len(arr)

    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = arr[mid_idx]

        if mid_val == target:
            return mid_idx

        if target < mid_val:
            right_pointer = mid_idx

        if target > mid_val:
            left_pointer = mid_idx + 1

    return "value not found"


if __name__ == "__main__":
    # For testing:
    sorted_values = [13, 14, 15, 16, 17]
    print("Recursive implementation: ")
    print(binary_search_recursive(sorted_values, 0, len(sorted_values), 17))

    print("Iterative implementation: ")
    print(binary_search_iterative(sorted_values, 12))
