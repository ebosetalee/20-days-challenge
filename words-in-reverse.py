words = input("Write a sentence containing 10 words (be creative): ")
length = 10
newwords = words.split(" ")
while True:
    if length == len(newwords):
        print(words[::-1])

        print ("\n AND\n")

        # newwords = words.split(" ")
        sentence = [word[::-1] for word in newwords]
        newSentence = " ".join(sentence)
        print(newSentence)
        break
    else:
        break