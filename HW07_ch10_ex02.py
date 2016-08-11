# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print(anything extraneous!
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
			inputList[index] = inputList[index].capitalize()

	return inputList

def main():
    list_1 = ['apple', ['bear'], 'cat', 'doggy', ['elbow', 'fin', 'garage']]
    list_2 = [[[['apple']], 'bear', 'cat', 'doggy', 
             ['elbow','fin','garage','house','indigo']], 'jump']
    list_3 = []
    list_4 = ["doggy"]
    list_4 = [[[[[[["this"]]]]]]]
    print(capitalize_nested(list_1))
    print(capitalize_nested(list_2))
    print(capitalize_nested(list_3))
    print(capitalize_nested(list_4))

if __name__ == '__main__':
	main()