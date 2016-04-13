
'''
Automate the Boring Stuff
Chapter 7 - Regex

Practice Projects
Regex Version of strip()

write a function that takes a string, and optionally 1 argument
if no argument provided (i.e. default) strip leading and trailing
spaces from string, return string.

if argument provided, then strip the characters specified in the argument
(not sure if characters are stripped from start and end of string,
or removed entirely from the string)
'''

import re

def stripper(stringToStrip, characters = ' '):
	stripRegex = re.compile(characters)

	if characters == ' ':
		stripRegex = re.compile(r'(^\s*)(.*)(\s*$)')
		mo = stripRegex.search(stringToStrip)
		return (mo.group(2))
	else:
		strippedString = stripRegex.sub('',stringToStrip)
		return strippedString


print (stripper('  abcd fgh  '))
print (stripper('  accdggccd', 'c'))