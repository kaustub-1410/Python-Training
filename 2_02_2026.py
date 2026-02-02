# --------- 1 to n ---------
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)


# --------- n to 1 ---------
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)


# --------- Sum of first n natural numbers ---------
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


# --------- Sum of array elements ---------
def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)


# --------- Recursive search in array ---------
def search(arr, n, x):
    if n == 0:
        return False
    if arr[n - 1] == x:
        return True
    return search(arr, n - 1, x)


# --------- MENU ---------
while True:
    print("\n----- MENU -----")
    print("1. Print 1 to n")
    print("2. Print n to 1")
    print("3. Sum of first 10 natural numbers")
    print("4. Sum of array elements")
    print("5. Search element in array")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting program.")
        break

    elif choice == 1:
        n = int(input("Enter n: "))
        print_1_to_n(n)

    elif choice == 2:
        n = int(input("Enter n: "))
        print_n_to_1(n)

    elif choice == 3:
        print("Sum of first 10 natural numbers:", sum_n(10))

    elif choice == 4:
        n = int(input("Enter number of elements: "))
        arr = list(map(int, input("Enter elements: ").split()))
        print("Sum of array elements:", sum_array(arr, n))

    elif choice == 5:
        n = int(input("Enter number of elements: "))
        arr = list(map(int, input("Enter elements: ").split()))
        x = int(input("Enter element to search: "))
        print(search(arr, n, x))

    else:
        print("Invalid choice!")
