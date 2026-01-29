s = input("Enter sentence: ")

words = s.split()
reversed_words = words[::-1]

print("Word-wise reversed:", " ".join(reversed_words))
