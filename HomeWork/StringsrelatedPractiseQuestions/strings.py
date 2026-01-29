# ================= STRING PROGRAMS =================

# 1. Count occurrences of a character in a string
def count_char(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count


# 2. Replace all vowels with *
def replace_vowels(s):
    result = ""
    for ch in s:
        if ch.lower() in "aeiou":
            result += "*"
        else:
            result += ch
    return result


# 3. Reverse string WITHOUT creating a new string
def reverse_in_place(s):
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)


# 4. Reverse string using function and store in new string
def reverse_string(s):
    return s[::-1]


# 5. Palindrome check using function
def is_palindrome(s):
    return s == s[::-1]


# 6. Convert string to Title Case
def to_title_case(s):
    words = s.split()
    result = []
    for w in words:
        result.append(w.capitalize())
    return " ".join(result)


# 7. deleteChar() function
def deleteChar(s, ch):
    new_str = ""
    for c in s:
        if c != ch:
            new_str += c
    return new_str


# 8. Sum of digits in a string
def sum_of_digits(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total


# ================= LIST PROGRAMS =================

# 1. Increment elements by 5
def increment_list(lst):
    for i in range(len(lst)):
        lst[i] += 5


# 2. Count occurrences in list
def count_occurrence(lst, element):
    count = 0
    for x in lst:
        if x == element:
            count += 1
    return count


# 3. Separate positive and negative numbers
def separate_positive_negative(lst):
    positive = []
    negative = []
    for num in lst:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    return positive, negative


# 4. Largest element using function
def largest_element(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


# 5. Second largest element
def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


# 6. Median of a list
def find_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]
