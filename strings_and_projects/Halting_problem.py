# Halting problem 1
def problematic_collector(count):
    unique_names = {}

    while len(unique_names) < count:
        name = input("Enter name: ")

        if name.lower() in unique_names:
            print("Duplicate! Try again")

# The halting problem says: No program can detect if this loop will ever finish because it depends on unpredictable 
# user behaviour

# Halting problem 2

def mystery_function():
    names = []
    while True:
        user_input = input("Type 'stop' to stop, or anything else to continue")
        if user_input == "stop":
            break
        names.append(user_input)
    return names
