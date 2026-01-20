n = int(input("Enter a number: "))

if n > 0 and n % 2 != 0:
    print("Number is Positive and Odd")

if n > 0 and n % 2 == 0:
    print("Number is Positive and Even")

if n < 0 and n % 2 != 0:
    print("Number is Negative and Odd")

if n < 0 and n % 2 == 0:
    print("Number is Negative and Even")
