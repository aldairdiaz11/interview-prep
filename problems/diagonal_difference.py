
def diagonal_difference(arr: list[list[int]]) -> int:
    size = len(arr)
    first, second = 0, 0
    for n in range(size):
        first = arr[n][n]
        second = arr[n][size - 1 - n]
    return abs(first - second)


if __name__ == "__main__":
    n = int(input().strip())

    arr_ = []

    for _ in range(n):
        arr_.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr_)
