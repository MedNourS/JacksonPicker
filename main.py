import random

student_set = set()

def add(name:str):
        if not name in student_set:
            student_set.add(name)
            print(f"{name} added!\n")
            main(True)
        else:
            raise Exception("Student already in list: pick another name")

def remove(name:str):
        try:
                student_set.remove(name)
                print(f"{name} has been removed\n")
        except:
                raise Exception("Specified student is not in the list")
        main(True)

def pick(bool:bool):
        if len(student_set) > 0:
                chosen_student = random.choice(tuple(student_set))
                print(f"{chosen_student}\n")
                if bool == True:
                        student_set.remove(chosen_student)
        else:
                raise Exception("No one to pick!")
        main(True)

def find(name:str):
    if name in student_set:
        print("Student is in list\n")
    else:
        print("Student is not in list\n")
    main(True)

def getListInfo():
        if len(student_set) > 0:
                print(f"{len(student_set)} student(s) in the list:")
                print(f"{student_set}\n")
        else:
                print(f"No students in the list\n")
        main(True)

def stop():
        main(False)

def parser():
        try:
                command = input("~: ")
                split_command = command.split()
                if len(split_command) > 1:
                        if split_command[0].lower() == "add":
                                add(split_command[1])
                        elif split_command[0].lower() == "remove":
                                remove(split_command[1])
                        elif split_command[0].lower() == "pick" and split_command[1].lower() == "-r":
                                pick(True)
                        elif split_command[0].lower() == "find":
                                find(split_command[1])
                elif command == "add":
                        add(input("Student's name:"))
                elif command == "remove":
                        remove(input("Student's name:"))
                elif command == "pick":
                        pick(False)
                elif command == "list":
                        getListInfo()
                elif command == "stop":
                        stop()
                elif command == "help":
                        help()
                else:
                        raise Exception("Invalid command!")
        except Exception as E:
                print(f"{E}\n")
                main(True)
        else:
                print("\n")

def help():
        print("Available commands:\n        -> add [name]\n                 to add a student to the list\n        -> remove [name]\n                to remove a student from the list\n        -> pick [-r]\n                to pick a student from the list (-r to remove them after being chosen)\n        -> list\n                to show all students in the list\n        -> stop\n                to stop the code")
        main(True)

def main(bool:bool):
        if bool == True:        
                parser()                
        else:
                pass

if __name__ == "__main__":
  main(True)