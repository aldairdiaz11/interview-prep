def lonely_integer(arr: list[int]) -> int:
    count = {}
    for item in arr:
        count[item] = 1 if item not in count else count[item] + 1

    for item in count:
        if count[item] == 1:
            return item
    return 0


if __name__ == "__main__":
    test_case = [1, 2, 3, 4, 3, 2, 1]

    print(lonely_integer(test_case))
