words = "When life is easy, do hard things and be you"

print(words[::-1])

print ("\n AND\n")

newwords = words.split(" ")
sentence = [word[::-1] for word in newwords]
newSentence = " ".join(sentence)
print(newSentence)