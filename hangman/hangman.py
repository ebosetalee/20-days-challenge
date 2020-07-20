import random
my_list = ["I", "eat", "chicken", "and", "turkey"]
random_word = str(random.choice(my_list).upper())
print(random_word)

word = ""
while word != random_word and word != "!":
    word = input("Kindly type one letter only: ").upper()
    index = 0
    for i in random_word:
        if word == i:
            print("YES in {}".format(index))
        index += 1
    random_word == i
    # print(random_word)
    if word == "!":
        break
    elif word not in random_word:
        print("NO! try again. Type ! to quit")