import sqlite3


db = sqlite3.connect("hangman/data/store_guesses.sqlite")

def create_table(): 
    """sqlite table created to store guesses"""
    db.execute("CREATE TABLE IF NOT EXISTS guesses(letter CHAR)")

def store_guessed_letter(guess):
    """ adds the guesses into the table created"""
    db.execute("INSERT INTO guesses VALUES('{}')".format(guess))
    db.commit()

def drop_table():
    """ deletes the table and its db """
    drop_table_query = "DROP TABLE guesses"
    db.execute(drop_table_query)
    db.close()