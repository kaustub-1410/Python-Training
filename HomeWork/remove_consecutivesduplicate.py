s = input("Enter string: ")

result = s[0]

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        result += s[i]

print("After removing duplicates:", result)
