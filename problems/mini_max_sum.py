def mini_max_sum(arr: list[int]) -> None:
    arr.sort()  # time complexity O(n log n), space complexity O(1)
    min_ = sum(arr[:-1])
    max_ = sum(arr[1:])

    print(min_, max_)

    # Alternative solution, time complexity O(n), space complexity O(1)
    min_val = min(arr)
    max_val = max(arr)
    total_sum = sum(arr)

    min_sum = total_sum - max_val
    max_sum = total_sum - min_val

    print(min_sum, max_sum)


if __name__ == '__main__':
    arr_ = list(map(int, input().rstrip().split()))

    mini_max_sum(arr_)
