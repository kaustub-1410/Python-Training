

## 1. Star Square Pattern


n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

## 2. Star Right Triangle




n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

## 3. Star Right Triangle (With Spaces)


n = 5
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)

## 4. Number Pattern (Constant)


n = 3
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()

## 5. Increasing Number Pattern


n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


## 6. Alphabet Patterns

#
n = 3
for i in range(1, n+1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

## 7. Merging Patterns (Star + Number)

n = 3
for i in range(1, n+1):
    print("* " * i, end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

## 8. Advanced Pattern – Pyramid



n = 4
for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)


## 9. Taking Input in a List

### A) Space Separated Input


nums = list(map(int, input("Enter numbers: ").split()))
print(nums)

### B) Line Separated Input


n = int(input("Enter number of elements: "))
nums = []
for i in range(n):
    nums.append(int(input()))
print(nums)


## 10. Linear Search Using List


nums = [10, 20, 30, 40]
target = 30
found = False

for i in range(len(nums)):
    if nums[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")


## 11. Concept of Swapping in Python

### Using Temporary Variable


a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)

### Without Temporary Variable (Python way)


a = 5
b = 10
a, b = b, a
print(a, b)

## 12. Demonstrating Reversal

### A) Reverse a Number


num = 1234
rev = 0
while num > 0:
    rev = rev*10 + num%10
    num //= 10
print(rev)


### B) Reverse a List

nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

### C) Reverse a String


s = "python"
print(s[::-1])
