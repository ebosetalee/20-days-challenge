import random
def get_target_word():
    my_list = ["I", "eat", "chicken", "and", "turkey"]
    random_word = str(random.choice(my_list).upper())
    # str() to convert my_list from list to string
    print(random_word)
    return random_word
random_word = get_target_word()
# After trying to use random_word outide the function, an error occured as random_word is defined only in the function 
# Thus, reassigning the function to random_word and also for dic_list as seen below.

def convert_to_dictionary():
    # this function helps determine which letter from the target word is guessed correctly. 
    # Each letter is passed with a false boolean and converts to true in the hangman_function().
    dic_list = {}
    for letters in random_word:
        dic_list[letters] = False
    print(dic_list) # to show the results for practise purpose.
    return dic_list  # still don't know why I'm to return a parameter.  
dic_list = convert_to_dictionary()

def hangman_function():
    word = ""
    count = 0
    while True:
        word = input("Kindly type one letter only: ").upper()
        # Using .upper to ensure the input aligns with random_word, whether the input is in capital or small letter.
        index = 0 # to determine where the correct guessed letter is located in the string.
        count += 1 # to determine how many times the function is run
        for i in random_word:
            if word == i:
                dic_list[word] = True
                print("YES in {0} after {1} tries".format(index, count))
            index += 1 
        if word == "!":
            for val in dic_list:
                print(val + ": {} ".format(dic_list[val]))
                # using .format to add the boolean to the string. 
            break
        elif word not in dic_list:
            # using not in because != works on integer only.
            print("NO! try again. Type ! to quit")
hangman_function()