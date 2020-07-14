words = ["When", "life", "is",\
    "easy,", "do", "hard", "things",
    "and", "be", "you"]

wordString = ""
wordString = " ".join(words)
print(wordString+ "!\n") 

print(wordString[::-1])

print ("\n AND\n")

for word in words:
    print(word[::-1], end = ' ')