import time  # Importing the time module to measure execution time

"""
--------------------------------------------------------
Sorting and Searching Algorithms with Timing
--------------------------------------------------------

This program now measures and prints the time taken for each operation.
--------------------------------------------------------
"""

# Main program function
def main():
    print("Welcome to the Sorting and Searching Program with Timing!")
    print("Choose an operation:")
    print("1. Search")
    print("2. Sort")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        search_menu()
    elif choice == 2:
        sort_menu()
    else:
        print("Invalid choice. Exiting.")

# Search Menu
def search_menu():
    print("\nSearch Options:")
    print("1. Linear Search")
    print("2. Binary Search (requires a sorted list)")

    search_choice = int(input("Enter your choice (1 or 2): "))

    if search_choice == 1:
        linear_search()
    elif search_choice == 2:
        binary_search()
    else:
        print("Invalid choice. Returning to main menu.")

# Sorting Menu
def sort_menu():
    print("\nSorting Options:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Radix Sort")

    sort_choice = int(input("Enter your choice (1-6): "))

    if sort_choice == 1:
        bubble_sort()
    elif sort_choice == 2:
        insertion_sort()
    elif sort_choice == 3:
        selection_sort()
    elif sort_choice == 4:
        merge_sort_handler()
    elif sort_choice == 5:
        quick_sort_handler()
    elif sort_choice == 6:
        radix_sort()
    else:
        print("Invalid choice. Returning to main menu.")

# 1. Linear Search
def linear_search():
    print("\nYou selected Linear Search.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    key = int(input("Enter the number to search for: "))

    start_time = time.time()  # Start timing
    for i, value in enumerate(lst):
        if value == key:
            end_time = time.time()  # End timing
            print(f"Element found at index {i}. Time taken: {end_time - start_time:.6f} seconds.")
            return
    end_time = time.time()  # End timing
    print(f"Element not found. Time taken: {end_time - start_time:.6f} seconds.")

# 2. Binary Search
def binary_search():
    print("\nYou selected Binary Search.")
    lst = sorted(list(map(int, input("Enter the sorted list of numbers separated by spaces: ").split())))
    key = int(input("Enter the number to search for: "))

    start_time = time.time()  # Start timing
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            end_time = time.time()  # End timing
            print(f"Element found at index {mid}. Time taken: {end_time - start_time:.6f} seconds.")
            return
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    end_time = time.time()  # End timing
    print(f"Element not found. Time taken: {end_time - start_time:.6f} seconds.")

# 3. Bubble Sort
def bubble_sort():
    print("\nYou selected Bubble Sort.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    n = len(lst)

    start_time = time.time()  # Start timing
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(f"Pass {i+1}: {lst}")
    end_time = time.time()  # End timing

    print(f"Sorted list: {lst}. Time taken: {end_time - start_time:.6f} seconds.")

# 4. Insertion Sort
def insertion_sort():
    print("\nYou selected Insertion Sort.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    
    start_time = time.time()  # Start timing
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        print(f"Pass {i}: {lst}")
    end_time = time.time()  # End timing

    print(f"Sorted list: {lst}. Time taken: {end_time - start_time:.6f} seconds.")

# 5. Selection Sort
def selection_sort():
    print("\nYou selected Selection Sort.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    
    start_time = time.time()  # Start timing
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        print(f"Pass {i+1}: {lst}")
    end_time = time.time()  # End timing

    print(f"Sorted list: {lst}. Time taken: {end_time - start_time:.6f} seconds.")

# 6. Merge Sort
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_handler():
    print("\nYou selected Merge Sort.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    start_time = time.time()  # Start timing
    merge_sort(lst)
    end_time = time.time()  # End timing
    print(f"Sorted list: {lst}. Time taken: {end_time - start_time:.6f} seconds.")

# 7. Quick Sort
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less_than_pivot = [x for x in lst[1:] if x <= pivot]
        greater_than_pivot = [x for x in lst[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def quick_sort_handler():
    print("\nYou selected Quick Sort.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    start_time = time.time()  # Start timing
    sorted_lst = quick_sort(lst)
    end_time = time.time()  # End timing
    print(f"Sorted list: {sorted_lst}. Time taken: {end_time - start_time:.6f} seconds.")

# 8. Radix Sort
def radix_sort():
    print("\nYou selected Radix Sort.")
    lst = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

    start_time = time.time()  # Start timing
    max_num = max(lst)
    exp = 1
    while max_num // exp > 0:
        counting_sort(lst, exp)
        exp *= 10
        print(f"Pass with exp {exp // 10}: {lst}")
    end_time = time.time()  # End timing

    print(f"Sorted list: {lst}. Time taken: {end_time - start_time:.6f} seconds.")
if __name__ == "__main__":
    main()
1
