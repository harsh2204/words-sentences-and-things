from datamuse import datamuse
import sys
import inquirer
import os

# Class taken from https://stackoverflow.com/a/287944
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

api = datamuse.Datamuse()

text = input("Starting word:\t")
sentence = text
while(1):
	nouns = api.words(rel_jja=text, max=10)
	words = [data['word'] for data in nouns]
	questions = [
  	inquirer.List('word',
					message=f"Current sentence: {bcolors.WARNING + sentence + bcolors.ENDC}",
					choices=words,
				),
	]
	inquirer.render.ConsoleRender().clear_eos()
	os.system('cls||clear')
	answers = inquirer.prompt(questions)
	# print_out(nouns)
	# print(answers)
	if answers == None:
		os.system('cls||clear')
		print(f"Your final sentence was:\n{bcolors.OKGREEN + sentence + bcolors.ENDC}")
		raise SystemExit
	text = answers['word']
	sentence += " " + text