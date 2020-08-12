from lib.utils import get_target_word as target_word
from lib.database import create_table, drop_table
from lib.design import hangman_design as introduction
from lib.core import Hangman


print()
create_table()

introduction()
hangman = Hangman(target_word())

hangman.run()

drop_table()
