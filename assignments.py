from tabulate import tabulate
import useful_functions as uf
from datetime import date


def assignments(database):
    userOption = None
    while userOption not in (1, 2, 3, 4,):
        userOption = int(input(uf.userOption("Display Assignment", "Add Assignment",
                                             "Remove Assignment", "Complete Assignment")))
        if userOption == 1:
            displayAssignments(database)
        elif userOption == 2:
            addAssignments(database)
        elif userOption == 3:
            removeAssignments(database)
        elif userOption == 4:
            completeAssignments(database)
        else:
            uf.invIn()


def displayAssignments(database):
    table = [["Assignment", "Status", "Due Date"]]
    with open(database) as assignments:
        assignment = assignments.read()
        assignment = assignment.split("\n")
        for items in assignment:
            i = items.split(",")
            j = [i[0], i[1], i[2]]
            table.append(j)
        assignments.close()
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


def addAssignments(database):
    # Write file if it's empty
    file = open(database, "r")
    if not file.read():
        with open(database, "w") as assignment_list:
            assignment_add = {"name": None,
                              "status": "unfinished",
                              "deadline": None}

            name = input("What do you want to name your assignment? ")
            month = int(input('Enter the month of the deadline: '))
            day = int(input('Enter the day of the deadline: '))
            year = int(input('Enter the year of the deadline: '))
            deadline = date(year, month, day)

            assignment_add["name"] = name
            assignment_add["deadline"] = deadline

            assignment = f"{assignment_add['name']},{assignment_add['status']},{assignment_add['deadline']}"
            assignment_list.write(assignment)
            assignment_list.close()

    # Append file if it's not
    else:
        with open(database, "a") as assignment_list:
            assignment_add = {"name": None,
                              "status": "unfinished",
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
            assignment_list.close()


def removeAssignments(database):
    assignment_dict = {}
    table = [["Assignment No.", "Assignment"]]
    with open(database) as assignments:
        assignment = assignments.read()
        assignment = assignment.split("\n")
        for items, i in zip(assignment, range(len(assignment))):
            j = items.split(",")
            assignment_dict[i] = [j[0], j[1], j[2]]
            row = [i, j[0]]
            table.append(row)
        assignments.close()

    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
    assignment_no = int(input("Type the assignment no. of the assignment you want to remove: "))
    assignment_dict.pop(assignment_no)

    with open(database, "w") as assignment_list:
        output = ""
        for items in assignment_dict:
            output += f"{assignment_dict[items][0]},{assignment_dict[items][1]},{assignment_dict[items][2]}\n"
        output = output.rstrip("\n")
        assignment_list.write(output)
        assignment_list.close()


def completeAssignment(database):
    pass
