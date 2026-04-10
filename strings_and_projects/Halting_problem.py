def problematic_collector(count):
    unique_names = {}

    while len(unique_names) < count:
        name = input("Enter name: ")

        if name.lower() in unique_names:
            print("Duplicate! Try again")

# The halting problem says: No program can detect if this loop will ever finish because it depends on unpredictable 
# user behaviour