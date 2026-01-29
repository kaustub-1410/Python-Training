Below are **clean Python programs with user-defined functions** for **all string and list questions** you asked. These are written in a simple, student-friendly way.

---

# ✅ STRING PROGRAMS

---

## 1. Count occurrences of a character in a string

```python
def count_char(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

s = input("Enter string: ")
ch = input("Enter character to count: ")

print("Occurrences:", count_char(s, ch))
```

---

## 2. Replace all vowels with `*`

```python
def replace_vowels(s):
    result = ""
    for ch in s:
        if ch.lower() in "aeiou":
            result += "*"
        else:
            result += ch
    return result

s = input("Enter string: ")
print("Modified string:", replace_vowels(s))
```

---

## 3. Reverse string WITHOUT creating a new string

```python
s = list(input("Enter string: "))

i, j = 0, len(s) - 1
while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1

print("Reversed string:", "".join(s))
```

---

## 4. Reverse string using function and store in new string

```python
def reverse_string(s):
    return s[::-1]

s = input("Enter string: ")
rev = reverse_string(s)

print("Reversed string:", rev)
```

---

## 5. Palindrome check using function

```python
def is_palindrome(s):
    return s == s[::-1]

s = input("Enter string: ")

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

## 6. Convert string to Title Case

```python
def to_title_case(s):
    words = s.split()
    result = []
    for w in words:
        result.append(w.capitalize())
    return " ".join(result)

s = input("Enter string: ")
print("Title Case:", to_title_case(s))
```

---

## 7. deleteChar() function

```python
def deleteChar(s, ch):
    new_str = ""
    for c in s:
        if c != ch:
            new_str += c
    return new_str

s = input("Enter string: ")
ch = input("Enter character to delete: ")

print("New string:", deleteChar(s, ch))
```

---

## 8. Sum of digits in a string

```python
def sum_of_digits(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total

s = input("Enter string: ")
print("Sum of digits:", sum_of_digits(s))
```

---

# ✅ LIST PRACTICE PROGRAMS

---

## 1. Increment elements by 5

```python
def increment_list(lst):
    for i in range(len(lst)):
        lst[i] += 5

lst = list(map(int, input("Enter list elements: ").split()))
increment_list(lst)

print("Updated list:", lst)
```

---

## 2. Count occurrences in list

```python
def count_occurrence(lst, element):
    count = 0
    for x in lst:
        if x == element:
            count += 1
    return count

lst = list(map(int, input("Enter list: ").split()))
el = int(input("Enter element: "))

print("Occurrences:", count_occurrence(lst, el))
```

---

## 3. Separate positive and negative numbers

```python
lst = list(map(int, input("Enter numbers: ").split()))

positive = []
negative = []

for num in lst:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Original list:", lst)
print("Positive list:", positive)
print("Negative list:", negative)
```

---

## 4. Largest element using function

```python
def largest_element(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

lst = list(map(int, input("Enter list: ").split()))
print("Largest element:", largest_element(lst))
```

---

## 5. Second largest element

```python
def second_largest(lst):
    first = second = float('-inf')

    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

lst = list(map(int, input("Enter list: ").split()))
print("Second largest:", second_largest(lst))
```

---

## 6. Median of a list

```python
def find_median(lst):
    lst.sort()
    n = len(lst)

    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

lst = list(map(int, input("Enter list: ").split()))
print("Median:", find_median(lst))
```

---

If you want, I can also provide:

✅ All programs in **one menu-driven file**
✅ With **comments for exam writing**
✅ Or convert to **class-based programs**
✅ Or make a **PDF-style formatted notes version**

Just tell me 😊
