def linear_search(search_list: list, target_value: int | str) -> int:
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return idx
    raise ValueError(f"{target_value} not in list")


def linear_search_occurrences(search_list: list, target_value: int | str) -> list:
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
    if len(matches) > 0:
        return matches
    raise ValueError(f"{target_value} not in list")


def linear_search_max(search_list: list) -> int:
    max_val_idx = 0
    for idx in range(len(search_list)):
        max_val_idx = idx if search_list[idx] > search_list[max_val_idx] else max_val_idx
    return max_val_idx


if __name__ == "__main__":
    #  tests...
    try:
        values = [54, 22, 46, 99]
        print(linear_search(values, 22))
    except ValueError as errorMessage:
        print(errorMessage)
