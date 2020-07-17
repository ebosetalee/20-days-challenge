import random
my_list = ["I", "eat", "chicken", "and", "turkey"]
random_word = str(random.choice(my_list))
# print(random_word.upper())

word = input("Kindly type one letter only: ")
index = 0
while index < len(random_word):
    if word in random_word[index]:
        print("YES in {}".format(index))
    index += 1
if word not in random_word:
    print("NO")