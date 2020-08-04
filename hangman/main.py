from lib.utils import get_target_word as target_word
from lib.core import Hangman
from lib.database import create_table, drop_table


hangman = Hangman(target_word())

create_table()

hangman.run()

drop_table()