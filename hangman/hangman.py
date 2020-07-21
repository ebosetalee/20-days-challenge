import random
def get_target_word():
    my_list = ["I", "eat", "chicken", "and", "turkey"]
    random_word = str(random.choice(my_list).upper())
    print(random_word)
    return random_word
random_word = get_target_word()

def convert_to_dictionary():
    dic_list = {}
    for letters in random_word:
        dic_list[letters] = False
    print(dic_list)
    return dic_list    
dic_list = convert_to_dictionary()

def hangman_function():
    word = ""
    count = 0
    while True:
        word = input("Kindly type one letter only: ").upper()
        index = 0
        count += 1
        for i in random_word:
            if word == i:
                dic_list[word] = True
                print("YES in {0} after {1} tries".format(index, count))
            index += 1 
        if word == "!":
            for val in dic_list:
                print(val + ": {} ".format(dic_list[val]))
            break
        elif word not in dic_list:
            print("NO! try again. Type ! to quit")
hangman_function()