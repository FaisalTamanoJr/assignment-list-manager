import assignments
import grades
import useful_functions as uf
from useful_functions import print_n
from sys import exit


def main():
    # Exit the Program when the user demands it
    exitProgram = False
    while not exitProgram:
        try:
            userOption = int(input(uf.userOption("Assignments", "Grades")))
            if userOption == 1:
                assignments.assignments()
            elif userOption == 2:
                grades.grades()
            else:
                uf.invIn()
        except ValueError:
            uf.invIn()

        # Option to exit
        try:
            userOption = None
            while userOption not in (1, 2):
                print("Would you like to exit the program?")
                userOption = int(input(uf.userOption("Yes", "No")))
                if userOption == 1:
                    exit()
                elif userOption == 2:
                    print("\n")
                else:
                    uf.invIn()
        except ValueError:
            uf.invIn()

    # Exit Program
    print("\nExiting Program...")


if __name__ == "__main__":
    main()
