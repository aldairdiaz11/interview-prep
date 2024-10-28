# Radix Sort Project - A Sorted Tale
import csv
import random


# Helper function to read csv file
def load_books(filename) -> list[dict | str]:
    bookshelf_ = []
    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            book['author_lower'] = book['author'].lower()
            book['title_lower'] = book['title'].lower()
            bookshelf_.append(book)
    return bookshelf_


# Sorts
def bubble_sort(arr, comparison_function):
    swaps = 0
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for idx in range(len(arr) - 1):
            if comparison_function(
                    arr[idx], arr[idx + 1]):
                sorted_ = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr


def quicksort(list_, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = list_[pivot_idx]
    list_[end], list_[pivot_idx] = list_[pivot_idx], list_[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, list_[i]):
            list_[i], list_[less_than_pointer] = list_[less_than_pointer], list_[i]
            less_than_pointer += 1
    list_[end], list_[less_than_pointer] = list_[less_than_pointer], list_[end]
    quicksort(list_, start, less_than_pointer - 1, comparison_function)
    quicksort(list_, less_than_pointer + 1, end, comparison_function)


def print_shelf_content(arr, key):
    for shelf in arr:
        print(shelf[key])


# ############### Comparison Functions
def by_title_ascending(book_a, book_b):
    return book_a["title_lower"] > book_b["title_lower"]


def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


def by_total_length(book_a, book_b):
    return (len(book_a['title_lower']) + len(book_a['author_lower']) >
            len(book_b['title_lower']) + len(book_b['author_lower']))


bookshelf = load_books('books_small.csv')
sort_1 = bubble_sort(bookshelf, by_title_ascending)
print_shelf_content(sort_1, 'title_lower')

bookshelf_v1 = bookshelf.copy()
sort_2 = bubble_sort(bookshelf_v1, by_author_ascending)
print_shelf_content(sort_2, 'author_lower')

bookshelf_v2 = bookshelf.copy()
quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print("\n\nQuick Sort - Sorting by author")
print_shelf_content(bookshelf_v2, 'author_lower')

bookshelf_v3 = bookshelf.copy()
sort_3 = bubble_sort(bookshelf_v3, by_total_length)
print("\n\nBubble Sort - Sorting by length")
print_shelf_content(bookshelf_v2, 'author_lower')
