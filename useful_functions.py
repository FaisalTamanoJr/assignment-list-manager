# usage example, userOption("Assignments", "Exit the program")
def userOption(*args):
    # Assign numbers to the options
    options = {}
    for option, no in zip(args, range(1, len(args)+1)):
        options[no] = option

    prompt = "Select an option:\n"

    # Add options to the string
    for i in options:
        prompt += f"[{i}] {options[i]}\n"

    # Return the prompt string
    prompt += "Input: "
    return prompt


def invIn():
    print("\nerror: invalid option\n")


def print_n(string):
    print(f"\n{string}\n")
