# 20-days-challenge.

This challenge shows my progress in Python over 20days.
![info](hangman/venv/pictures/Screenshot2020-08-12at12.35.31.png)

The 20 days challenge is engineered by @rtukpe and @yudori (my tutors) with a purpose to help me grow in my understanding and solving of pythons like questions and problems. 

Over the 20 days, I learnt: 
- how to _install pip and check pip version_
- _datetime module_ - in welcome.py, I had little knowledge of the module before now.
- _strip and split command_ - Previously, I didn't know how or when to use it.
- _coversion to base_ - I had only binary, octal and hex knowledege of conversion because it had a standard command to it i.e `x` for hexidecimal and `o` Octal while the normal division for binary.
- More on the _random module_ 
- python doesn't have a symbol for infinity (number)
- more on division (love simple maths)
- more on def funtion, when and how to use the _return_ statement.
- Docstrings, __PEP 8__ python styling - involves the spacing and comments
- a little on _math module_
- more on using _break and continue_ in a while loop
- more on _linking files_ and root directory
- _class and class attributes_ - this took a while but looking back, it seems easy.
- _Importing_ packages and code - I had no idea i could import a file written in python to another file. This brought my understanding of `__init__` and `__pycache__`.
- a new language - I regard this as a major plus, learning sql commands and using them(__SQLite3__) in python.
- more on creating and using a _virtual environment_ - Luckily a week before the challenge I was learning Json and Venv on youtube.
- installing a pyton library
- Majorly, how to use the __Rich API__ - a Python library for rich text and beautiful formatting in the terminal.
- Lastly but not the least __editting Readme__ to have images and different text formats.

The contents of this challenge include:
1. Welcome
2. Words in reverse
3. Convert a number to base n
4. Combine two files
5. Hangman Game.

## WECLOME.py
This requests for firstname, lastname and age and prints them out telling you the year you were born.
![welcome](hangman/venv/pictures/Screenshot2020-08-12at11.07.05.png)

## WORDS IN REVERSE.py
This requests a sentence from the user and prints it in two different reverse forms.
![words in reverse](hangman/venv/pictures/Screenshot2020-08-12at11.14.30.png)

## CONVERT A NUMBER TO BASE N.py
A number between 0 and 1000000000 is randomly selected by the computer and converted to a random base between 2 and 16 except 10.
![convert a number to base n](hangman/venv/pictures/Screenshot2020-08-12at11.20.10.png)

## COMBINE TWO FILES.py
This collects the contents of two files, combines them and writes the comibined data into another file.

## HANGMAN.py
This is a game that the computer chooses a random word from a text file containing 852 words. The player tries to guess the exact word, following the game's introduction.
![Hangman Game](hangman/venv/pictures/Screenshot2020-08-12at11.32.19.png) 

The game uses the rich library to show color and style to the introduction as well as what the game prints out. It runs with the rich console width of 120.
`console = Console(width=120)`

At the start the player gets an introduction and the rules of the game to ensure the player is familiar with the output.
![Hangman Design](hangman/venv/pictures/Screenshot2020-08-12at11.37.23.png)

Then the game tells the player to guess a letter.
If the player doesn't follow the instruction, the following output prints depending on which rule was ignored.
![Hangman Validation](hangman/venv/pictures/Screenshot2020-08-12at11.40.39.png)

Whereas, if a letter is guessed correctly, the game prints the following:
![Hangman](hangman/venv/pictures/Screenshot2020-08-12at11.52.22.png)

See ![hangman]() to play or clone the repository.

See ![20-days-challenge]() for more information. 