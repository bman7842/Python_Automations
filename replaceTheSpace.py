#TODO: Create some sort of list which contains all invalid characters (%&\ etc, look it up online, I'm not sure on those), make sure they are not being used as newChar
import os

DEFAULT_CHAR = '_'
TRUE_ALIASES = ['true', 'yes', 'y', 't']
FALSE_ALIASES = ['false', 'no', 'n', 'f']

#########################################################################
# Name: replaceSpaces
# inputs: dir = directory of files, newChar = the new character you'd like to replace spaces with;
#		  expand = True - Alter all child directories of base directory, false - only alter base directory
# Description: A simple function which replaces the spaces in a file name
#########################################################################
def replaceSpaces(baseDir, newChar = DEFAULT_CHAR, expand = False): # use recursion for the altering child directories
	for pathName in os.listdir(os.path.join(baseDir)):
		if os.path.isdir(os.path.join(baseDir,pathName)):
			if expand:
				print(f"expanding into folder {pathName}")
				replaceSpaces(os.path.join(baseDir, pathName), newChar, expand)
		else:
			if ' ' in pathName.split('\\')[-1]:
				newPath = pathName.split('\\')[-1].replace(' ', newChar)
				print(f"Replacing {pathName} with {newPath}")
				os.rename(os.path.join(baseDir, pathName), os.path.join(baseDir, newPath))

#TODO: currently can't handle int, float, only str and bool supported
def askInput(prompt, varType = str, desiredResponses = None):
	response = None

	response = str(input(prompt)).strip(' ')
	if varType == bool:
		if response.lower() in TRUE_ALIASES:
			return True
		elif response.lower() in FALSE_ALIASES:
			return False
		else:
			print("Invalid Response! Please answer Yes or No,")
			askInput(prompt, varType, desiredResponses)
	else:
		if desiredResponses == None or response.lower() in desiredResponses:
			return response
		else:
			print(f"{response} is not a valid response!")
			askInput(prompt, varType, desiredResponses)



replaceSpaces.__doc__ = "Repairs a directory with file names containing spaces"

if __name__ == "__main__":
	baseDir = os.path.expanduser(askInput('Which directory? (Hit enter for current directory)'))
	if (baseDir == ""):
		baseDir = os.getcwd()

	newChar = str(askInput(f"Replacement Character? (Hit enter for default: '{DEFAULT_CHAR}'"))
	if (newChar == ""):
		newChar = DEFAULT_CHAR
	elif len(newChar) > 1:
		newChar = newChar[0:1]

	expand = bool(askInput("Would you like to expand into child directories? (Yes(Y)/No(N)):", bool))

	statusMsg = f"Replacing spaces in {baseDir}"
	if expand:
		statusMsg += f" and all child directories"
	statusMsg += f" with '{newChar}'"
	print(statusMsg)

	#TODO: Add an 'are you sure?' prompt to ensure the user knows changes made can't be undone. Maybe figure out a way to display how many files will be changed
	replaceSpaces(baseDir, newChar, expand)
