import random
def get_target_word():
    """Selects a random string from a file"""
    my_list = []
    with open("/Users/ella/20-days-challenge/hangman/data/words.txt", "r") as words:
        for paragraphs in words:
            my_list.append(paragraphs.strip("\n"))
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
    guessed_letter=""
    count = 0
    while True:
        guessed_letter = input("\nKindly type one letter or ! to quit: ").upper()
        index = 0 
        count += 1      
        for i in random_word:
            if guessed_letter == i:
                dic_list[guessed_letter] = True
                print("YES in {0} after {1} tries".format(index, count))            
            index += 1 
        if guessed_letter == "!":
            for val in dic_list:
                print(val + ": {} ".format(dic_list[val]))
            break
        elif guessed_letter not in dic_list:
            attempt -= 1
            print("NO! you have {} trial(s).".format(attempt))
            if attempt == 0:
                print("The END! You've used up your trials. Try again!")
                for val in dic_list:
                    print(val + ": {} ".format(dic_list[val]))
                break
        display_current_guess(dic_list, random_word) 
        dic_values = dic_list.values()
        if all(dic_values):
            print("Yayyy!!!! Congratulations!!!!!")
            break
        
def display_current_guess(correct_guess, target_word):
    """ Prints out the correctly guessed target word"""
    outputs = ""
    for letters in target_word:
        if correct_guess[letters] == True:
            outputs += letters
        else:
            outputs += "_"    
    print(outputs)

hangman()   