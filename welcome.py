from datetime import datetime

firstname = input("What is your Firstname: ")
lastname = input("What is your Lastname: ")
age = int(input("How old are you today? "))

today = datetime.now()
birthday = today.year - age

print("WELCOME!!! {0} {1}, Born year {2}".format(firstname, lastname, birthday))