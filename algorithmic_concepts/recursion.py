# Define sum_to_one() below...
def sum_to_one(n: int) -> int:
    if n == 1:
        return n
    return n + sum_to_one(n - 1)


def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


def power_set(my_list: list) -> list:
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    # return combination of the two
    return with_first + power_set_without_first


def flatten(list_: list) -> list:
    result = []

    for curr in list_:
        if isinstance(curr, list):
            print("List found!")
            flat_list = flatten(curr)
            result += flat_list
        else:
            result.append(curr)
    return result


# define the fibonacci() function below...
def fibonacci(n: int) -> int:
    if n == 1:
        return n
    elif n == 0:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Recursive binary tree
def build_bst(list_: list) -> dict | str:
    if len(list_) == 0:
        return "No Child"

    middle_idx = len(list_) // 2
    middle_value = list_[middle_idx]

    print(f"Middle index: {middle_idx}")
    print(f"Middle value: {middle_value}")

    tree_node = {"data": middle_value, "left_child": build_bst(list_[:middle_idx]),
                 "right_child": build_bst(list_[middle_idx + 1:])}

    return tree_node


if __name__ == '__main__':
    # uncomment when you're ready to test
    print(sum_to_one(7))
    print(factorial(5))
    universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
    power_set_of_universities = power_set(universities)

    for set_ in power_set_of_universities:
        print(set_)

    print(fibonacci(6))
    # set the appropriate runtime:
    # 1, logN, N, N^2, 2^N, N!
    fibonacci_runtime = "2^N"

    sorted_list = [12, 13, 14, 15, 16]
    binary_search_tree = build_bst(sorted_list)
    print(binary_search_tree)

    # fill in the runtime as a string
    # 1, logN, N, N*logN, N^2, 2^N, N!
    runtime = "N*logN"
