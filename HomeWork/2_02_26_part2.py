# --------- FACTORIAL (RECURSIVE) ---------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# --------- CHECK SORTED USING SLICING ---------
def is_sorted_slicing(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted_slicing(arr[1:])


# --------- CHECK SORTED USING INDEX (NO EXTRA SPACE) ---------
def is_sorted_index(arr, i=0):
    if i == len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return is_sorted_index(arr, i + 1)


# --------- MENU ---------
while True:
    print("\n----- MENU -----")
    print("1. Find Factorial (Recursive)")
    print("2. Check if list is sorted (Using slicing)")
    print("3. Check if list is sorted (Using index, no extra space)")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Exiting program.")
        break

    elif choice == 1:
        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))

    elif choice == 2:
        arr = list(map(int, input("Enter list elements: ").split()))
        print(is_sorted_slicing(arr))

    elif choice == 3:
        arr = list(map(int, input("Enter list elements: ").split()))
        print(is_sorted_index(arr))

    else:
        print("Invalid choice!")
