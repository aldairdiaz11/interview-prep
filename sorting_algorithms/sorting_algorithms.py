# Bubble sort
def bubble_sort(array):
    for i in range(len(array)):
        for idx in range(len(array) - i - 1):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]


# Merge sort
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid_idx = len(array) // 2
    left = array[:mid_idx]
    right = array[mid_idx:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(array1, array2):
    result = []

    while array1 and array2:
        result.append(array1.pop(0)) if array1[0] <= array2[0] else result.append(array2.pop(0))

    if array1:
        result += array1
    elif array2:
        result += array2

    return result


if __name__ == '__main__':
    # Bubble sort
    nums = [5, 2, 9, 1, 5, 6]
    bubble_sort(nums)
    print(nums)

    # Merge Sort
    unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
    unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770,
                       595, 571, 268, 373]
    unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

    ordered_list1 = merge_sort(unordered_list1)
    ordered_list2 = merge_sort(unordered_list2)
    ordered_list3 = merge_sort(unordered_list3)

    print(ordered_list1)
    print(ordered_list2)
    print(ordered_list3)
