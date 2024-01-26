import random

student_set = set()

def add(name):
	student_set.add(name)
	main()

def pick():
	chosen_student = random.choice(tuple(student_set))
	print(chosen_student)
	student_set.remove(chosen_student)
	main()

def main():
	command = input("Yo")
	
	command = list(command)
	
	if len(command) > 1 and command[0] == "add":
		add(command[1])
	else:
		if "add" in command:
			add(input("Who do you want to add?"))
		elif "pick" in command:
			pick()
		else:
			print("Insert a valid command!")


if __name__ == "__main__":
	main()
	
