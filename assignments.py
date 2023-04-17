import useful_functions as uf
from datetime import date


def assignments(database):
    userOption = None
    while userOption not in (1, 2, 3, 4,):
        userOption = int(input(uf.userOption("Priority Sort", "Display Assignment", "Add Assignment",
                                             "Remove Assignment")))
        if userOption == 1:
            displaySorted(database)
        elif userOption == 2:
            displayAssignments(database)
        elif userOption == 3:
            addAssignments(database)
        elif userOption == 4:
            removeAssignments(database)
        else:
            uf.invIn()


def displaySorted(database):
    pass
    # code


def displayAssignments(database):
    pass
    # code


def addAssignments(database):
    with open(database, "a") as assignment_list:
        assignment_add = {"name": None,
                          "status": "finished",
                          "deadline": None}

        name = input("What do you want to name your assignment? ")
        month = int(input('Enter the month of the deadline: '))
        day = int(input('Enter the day of the deadline: '))
        year = int(input('Enter the year of the deadline: '))
        deadline = date(year, month, day)


        assignment_add["name"] = name
        assignment_add["deadline"] = deadline

        assignment = f"\n{assignment_add['name']},{assignment_add['status']},{assignment_add['deadline']}"
        assignment_list.write(assignment)


def removeAssignments(database):
    pass
    # code
