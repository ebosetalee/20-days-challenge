import sqlite3


def create_table():
    db = sqlite3.connect("hangman/data/store_guesses.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS guesses(letter CHAR)")

def guesses_table(guessed_letter):
    """ adds the guesses into the table created"""
    db.execute("INSERT INTO guesses VALUES('{}')".format(guessed_letter))
    db.commit()

def drop_table():
    """ deletes the table and its db """
    drop_table_query = "DROP TABLE guesses"
    db.execute(drop_table_query)
    db.close()