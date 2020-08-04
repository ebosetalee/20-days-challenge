import sqlite3


contents = sqlite3.connect("hangman/data/store_guesses.sqlite")
contents.execute("CREATE TABLE IF NOT EXISTS guesses(letter CHAR)")

def guesses_table(guess):
    """ adds the guesses into the table created"""
    contents.execute("INSERT INTO guesses VALUES('{}')".format(guess))
    cursor = contents.cursor()
    cursor.execute("SELECT * FROM guesses")
    print(cursor.fetchall())
    contents.commit()

def drop_table():
    """ deletes the table and its contents """
    drops = "DROP TABLE guesses"
    contents.execute(drops)
    contents.close()