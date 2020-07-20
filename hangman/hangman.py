import random
my_list = ["I", "eat", "chicken", "and", "turkey"]
random_word = str(random.choice(my_list).upper())
print(random_word)

dic_list = {}
for letters in random_word:
    dic_list[letters] = False
print(dic_list)

word = ""
count = 0
while word != dic_list and word != "!":
    word = input("Kindly type one letter only: ").upper()
    index = 0
    for i in dic_list:
        if word == i:
            dic_list[word] = True
            print("YES in {0} and it only took you {1} tries".format(index, count))
        index += 1
    count += 1
    if word == "!":
        for val in dic_list:
            print(val + ": {} ".format(dic_list[val]))
        break
    elif word not in dic_list:
        print("NO! try again. Type ! to quit")