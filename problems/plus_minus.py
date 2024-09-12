def plus_minus(arr: list) -> None:
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)

    print(f"{positive / len(arr):.6f}")
    print(f"{negative / len(arr):.6f}")
    print(f"{zero / len(arr):.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr_ = list(map(int, input().rstrip().split()))

    plus_minus(arr_)
