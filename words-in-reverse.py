words = input("Write a sentence containing 10 words (be creative): ")
length = 10
new_words = words.split(" ")

if length == len(new_words):
    print(words[::-1])

    print ("\n AND\n")

    sentence = [word[::-1] for word in new_words]
    new_sentence = " ".join(sentence)
    print(new_sentence)