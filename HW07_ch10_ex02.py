# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# Imports

# Body
def capitalize_nested(inputList):

	# get the lenght of the list
	lenList = len(inputList)

	# loop through the list
	for index in range(0, lenList):
		# check if the element is a list in itself, if it is then re-call the function, else capitalize
		if(type(inputList[index]) == list):
			capitalize_nested(inputList[index])
		else:
			inputList[index] = inputList[index].upper()

def main():
	pass

if __name__ == '__main__':
	main()