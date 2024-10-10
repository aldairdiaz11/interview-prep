from random import randrange, shuffle


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


# Quick Sort
def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_idx = randrange(start, end)
    array[-1], array[pivot_idx] = array[pivot_idx], array[-1]

    lesser_than_pointer = start
    for idx in range(start, end):
        if array[idx] < array[lesser_than_pointer]:
            array[lesser_than_pointer], array[idx] = array[idx], array[lesser_than_pointer]
            lesser_than_pointer += 1
    array[end], array[lesser_than_pointer] = array[lesser_than_pointer], array[end]

    quick_sort(array, start, lesser_than_pointer - 1)
    quick_sort(array, lesser_than_pointer + 1, end)


# Radix Sort
def radix_sort(array):
    max_value = max(array)
    max_exponent = len(str(max_value))
    being_sorted = array[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for _ in range(10)]

        for number in being_sorted:
            try:
                digit = int(str(number)[index])
            except IndexError:
                digit = 0
            digits[digit].append(number)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted


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

    # Quick sort
    unsorted_list = [3, 7, 12, 24, 36, 42]
    shuffle(unsorted_list)
    print(unsorted_list)
    # use quicksort to sort the list, then print it out!
    quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    print(unsorted_list)

    # Radix Sort
    unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
    print(radix_sort(unsorted_list))
