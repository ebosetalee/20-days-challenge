from lib.utils import get_target_word as target_word
from lib.core import Hangman


hangman = Hangman(target_word())

hangman.run()
