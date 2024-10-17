def sparse_search(data: list, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))

    first, last = 0, len(data) - 1

    while first <= last:
        mid = (first + last) // 2

        if not data[mid]:
            left, right = mid - 1, mid + 1

            while True:

                if left < first and right > last:
                    print("{0} is not in the dataset".format(search_val))
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                else:
                    right, left = right + 1, left - 1

        if data[mid] == search_val:
            print("{0} found at position {1}".format(search_val, mid))
            return
        elif search_val < data[mid]:
            last = mid - 1
        elif search_val > data[mid]:
            first = mid + 1
    print("{0} is not in the dataset".format(search_val))


if __name__ == "__main__":
    sparse_search([""], "Hello")
    sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")
    sparse_search(["A", "B", "", "", "E"], "A")
    sparse_search(["", "X", "", "Y", "Z"], "Z")
    sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")
    sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")
    sparse_search(
        ["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "",
         "", "Parth", "", "", "", "Zachary"], "Parth")
