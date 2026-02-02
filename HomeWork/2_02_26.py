# --------- MIN & MAX WITH MINIMUM COMPARISONS ---------
def min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if arr[0] < arr[1]:
        min_val = arr[0]
        max_val = arr[1]
    else:
        min_val = arr[1]
        max_val = arr[0]

    for i in range(2, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]

    return min_val, max_val


# --------- REVERSE ARRAY ---------
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# --------- Kth SMALLEST ELEMENT ---------
def kth_smallest(arr, k):
    # Using selection sort idea (partial)
    n = len(arr)
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k - 1]


# --------- SORT 0s, 1s, 2s (DNF) ---------
def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# --------- MOVE NEGATIVES TO BEGINNING ---------
def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


# --------- MENU ---------
while True:
    print("\n----- MENU -----")
    print("1. Find Min and Max")
    print("2. Reverse the Array")
    print("3. Kth Smallest Element")
    print("4. Sort 0s, 1s and 2s")
    print("5. Move Negatives to Beginning")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting program.")
        break

    arr = list(map(int, input("Enter array elements: ").split()))

    if choice == 1:
        mn, mx = min_max(arr)
        print("Minimum:", mn)
        print("Maximum:", mx)

    elif choice == 2:
        print("Reversed Array:", reverse_array(arr))

    elif choice == 3:
        k = int(input("Enter k: "))
        print(f"{k}th smallest element:", kth_smallest(arr, k))

    elif choice == 4:
        print("Sorted Array:", sort012(arr))

    elif choice == 5:
        print("Rearranged Array:", move_negatives(arr))

    else:
        print("Invalid choice!")
