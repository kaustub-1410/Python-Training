# 1. Print natural numbers from 1 to N using FOR loop
N = int(input("Enter a positive integer N: "))

print("Natural numbers using FOR loop:")
for i in range(1, N + 1):
    print(i, end=" ")
print()

# 2. Print natural numbers from 1 to N using WHILE loop
print("Natural numbers using WHILE loop:")
i = 1
while i <= N:
    print(i, end=" ")
    i += 1
print()

# 3. Print digits of N from right to left
temp = N
print("Digits of the number from right to left:")
while temp > 0:
    print(temp % 10)
    temp = temp // 10

# 4. Print all factors of N
print("Factors of the number:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")
print()

# 5. Count the factors of N
count = 0
for i in range(1, N + 1):
    if N % i == 0:
        count += 1
print("Count of factors:", count)

# 6. Check whether N is Prime or not
if count == 2:
    print("The number is Prime")
else:
    print("The number is Not Prime")

# 7. Find GCD / HCF of two numbers
a = int(input("Enter first number for GCD/LCM: "))
b = int(input("Enter second number for GCD/LCM: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("GCD is:", gcd)

# 8. Find LCM of two numbers
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print("LCM is:", lcm)
