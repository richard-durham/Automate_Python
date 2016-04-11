
'''
Automate the boring stuff
chapter 7 - Regex
practice project - strong password evaluation

password must be:
- minimum of 8 characters long
- contain both upper and lower case characters
- contain at least one digit
'''

import re

def passwordChecker(password):
	lengthChecker = re.compile(r'.{8}')
	digitChecker = re.compile(r'\d')
	lowerCaseChecker = re.compile(r'[a-z]')
	upperCaseChecker = re.compile(r'[A-Z]')

	if lengthChecker.search(password) != None:
		if digitChecker.search(password) != None:
			if lowerCaseChecker.search(password) != None:
				if upperCaseChecker.search(password) != None:
					return 'Strong'
				else:
					return 'Include a least 1 upper case character A-Z'
			else:
				return 'Include at least 1 lower case character a-z'
		else:
			return 'Include at least 1 digit 0-9'
	else:
		return 'Must have a length of 8 or more'


def evaluatePassword(password):
	result = passwordChecker(password)
	print (result)

evaluatePassword('1234567')
evaluatePassword('ABCDEFGH')
evaluatePassword('ABCDEFG1')
evaluatePassword('abcdefg2')
evaluatePassword('abcDEF3GH')