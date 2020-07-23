import random
def get_target_word():
    """ This function picks a random string from a list"""
    my_list = ["I", "eat", "chicken", "and", "turkey"]
    random_word = str(random.choice(my_list).upper())
    print(random_word)
    return random_word
random_word = get_target_word()

def convert_to_dictionary():
    """ converts the string to dictionary with values as False"""
    dic_list = {}
    for letters in random_word:
        dic_list[letters] = False
    print(dic_list)
    return dic_list    
dic_list = convert_to_dictionary()

def hangman():
    """ 
    Processes the user input, with the target word
    to determine which letter is guessed correctly.
    """
    attempt = 10
    word=""
    count = 0
    while True:
        word = input("\nKindly type one letter or ! to quit: ").upper()
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
            attempt -= 1
            print("NO! you have {} trial(s).".format(attempt))
            if attempt == 0:
                print("The END! You've used up your trials. Try again!")
                for val in dic_list:
                    print(val + ": {} ".format(dic_list[val]))
                break
hangman()   