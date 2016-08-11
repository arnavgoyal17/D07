# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(inputList):
	sortedList = sorted(inputList)

	if(sortedList == inputList):
		return True
	else:
		return False


def main():
	pass

if __name__ == '__main__':
	main()