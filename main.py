import inquirer
import toml
from termcolor import cprint
from pprint import pprint

def main():
    cprint("Welcome to eXCape", 'green')

    questions = [
            inquirer.List(
            'actions',
            message="What would you like to do?",
            choices=[
                'Show all configs',
                'Add new config',
            ]
        ),
    ]

    answers = inquirer.prompt(questions)

    pprint(answers)

main()