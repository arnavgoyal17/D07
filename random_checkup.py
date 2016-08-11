import random

# open roster
def open_roster():
	with open("roster.txt", "r") as roster:
		list_names = []
		for line in roster:
			line_item = line.split()
			line_item.pop()
			list_names.append(" ".join(line_item))

			# # initialise the variable that will hold the name of the person
			# person_name = ''

			# # split the line on white spaces
			# line_items = line.strip().split()

			# # get the lenght of line_items
			# len_item = len(line_items)

			# for n in range(0, len_item - 1):
			# 	person_name = person_name + line_items[n] + " "

			# person_name = person_name.strip()
			# list_names.append(person_name)

	return list_names

def remove_absents(inputList):

	userAns = input("Is anyone absent today? Y or N?: ")
	if(userAns.lower() == "y"):
		while True:
			print("Roster:")
			for index, name in enumerate(inputList):
				print("{}: {}".format(index, name))

			list_absent = []

			
			absent_idx = input("Enter index of absent (comma separated): ")
			if(absent_idx == 'done'):
				break
			list_absent_idx = absent_idx.split(",")
			
			for index, name in enumerate(inputList):
				if str(index) in list_absent_idx:
					list_absent.append(name)

			for names in list_absent:
				inputList.remove(names)
			
			print("\n".join(inputList))
			break
	else:
		print("Roster:")
		print("\n".join(inputList))

def random_number(inputList):
	while True:
		usrInput = input("Do you want to ask a question? Y or N? ")
		if(usrInput.lower() == "y"):
			randNum = random.randint(0, len(inputList) - 1)
			print("Name: " + inputList[randNum])

			inputList.pop(randNum)
		else:
			break

def main():
	studentList = open_roster()
	remove_absents(studentList)
	random_number(studentList)

if __name__ == '__main__':
	main()