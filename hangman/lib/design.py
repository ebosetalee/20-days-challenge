from rich.console import *


console = Console(width=100, color_system="truecolor", emoji=True)

welcome = """WELCOME! to [i #424CDF ]@ebosetalee's[/i #424CDF]
[b #BFBF1B]Hangman Game[/b #BFBF1B]!!!"""

game_info = """ [frame]
    Hangman game just like others, there's a 
    random guess word chosen by the computer.
    Each player gets a different word 
    and given a limited number of guesses.\n
    In that time, the player must guess the word correctly
    Each player can quit the game, OR 
    Keep guessing till all guesses are used.\n [/frame]
    :Sparkles: !!!NOW!!!:Sparkles: \n
    :Sparkles: How do you play the game?:Sparkles:\n  """

game_rules = """ 
[uu red]These are the rules of the game!!!![/uu red]\n [i]
1. You can't type more than one letter at once.\n
2. You can quit with ! anytime you want.\n
3. Numbers or symbols aren't allowed.\n
4. You have limited guesses.\n
5. Don't forget to enjoy the game.[/i] :Winking_face:\n"""


def hangman_design():
    """ A beautiful UI for introduction"""

    console.print(
        "\n:smiley:", "WELCOME!!!!", ":smiley:\n\n", ":Man_dancing: :Woman_dancing: " * 10,
        "\n", style="#386691 on #808080", justify="center")

    print()

    console.rule(welcome)
    console.print(game_info, justify="left")

    console.print(game_rules, justify="center", style="black on #A07E2B")
