import random


def get_target_word():
    """Selects a random string(target word) from a file"""
    my_list = []
    with open("hangman/data/words.txt", "r") as words:
        for paragraphs in words:
            my_list.append(paragraphs.strip("\n"))
    random_word = str(random.choice(my_list).upper())
    print(random_word)
    return random_word