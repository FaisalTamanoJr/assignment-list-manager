import useful_functions as uf
from useful_functions import print_n


def assignments():
    userOption = None
    while userOption not in (1, 2, 3, 4,):
        userOption = int(input(uf.userOption("Priority Sort", "Display Assignment", "Add Assignment",
                                             "Remove Assignment")))
        if userOption == 1:
            print_n("priority sort")
        elif userOption == 2:
            print_n("display assignment")
        elif userOption == 3:
            print_n("add assignment")
        elif userOption == 4:
            print_n("remove assignment")
        else:
            uf.invIn()


def prioritySort():
    pass
    # code


def displayAssignments():
    pass
    # code


def addAssignments():
    pass
    # code


def removeAssignments():
    pass
    # code
