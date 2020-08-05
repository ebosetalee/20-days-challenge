from lib.database import store_guessed_letter
import re
import math


class Hangman():

    def __init__(self, target_word):
        """This stores the target word variable in the 
        class Hangman"""
        self.target_word = target_word
        self.dict_list = self.convert_to_dictionary()

    def convert_to_dictionary(self):
        """ converts the string to dictionary with values as False"""
        dict_list = {}
        for letters in self.target_word:
            dict_list[letters] = False
        return dict_list

    def display_current_guess(self):
        """ Prints out the correctly guessed target word"""
        outputs = ""
        for letters in self.target_word:
            if self.dict_list[letters] == True:
                outputs += letters
            else:
                outputs += "_"
        print(outputs)

    def input_validation(self, guessed_letter):
        """ Uses regular expression to check
        1. Not an alphabet (lower or uppercase)
        2. Not a single character
        3. Not the quit character (!)
        """
        validation = re.search("^([a-zA-Z]|!)$", guessed_letter)
        return validation

    def run(self):
        """This runs through all the Hangman methods while asking 
        the user for a guessed letter. """
        attempt = math.ceil(len(self.target_word) * 1.5)
        count = 0
        while True:
            try:
                guessed_letter = input(
                    "\nKindly type one letter or ! to quit: ")
            except KeyboardInterrupt:
                print("\nThe correct word is {}. Bye.....".format(self.target_word))
                break
            if not self.input_validation(guessed_letter):
                print("Please type a single character alphabet or '!' to quit")
                continue
            guessed_letter = guessed_letter.upper()
            store_guessed_letter(guessed_letter)
            index = 0
            count += 1
            for i in self.target_word:
                if guessed_letter == i:
                    self.dict_list[guessed_letter] = True
                    print("YES in {0} after {1} tries".format(index, count))
                index += 1
            if guessed_letter == "!":
                print("The correct word is {}. Bye.....".format(self.target_word))
                break
            elif guessed_letter not in self.dict_list:
                attempt -= 1
                print("NO! you have {} trial(s).".format(attempt))
                if attempt == 0:
                    print("The END! You've used up your trials. Try again!")
                    print("The correct word is {}. Bye.....".format(
                        self.target_word))
                    break
            self.display_current_guess()
            dic_values = self.dict_list.values()
            if all(dic_values):
                print("Yayyy!!!! Congratulations!!!!!")
                break
