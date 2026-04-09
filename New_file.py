def unique_name_collector():
    unique_names = {}
    # Ask for the count first
    while True:
        try:
            count = int(input("How many unique names do you want to collect?")
                        )
            if count > 0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
    print(f"\nPlease enter {count} unique names (case-insensitive)")
    while len(unique_names) < count:
        name = input(f"Enter name #{len(unique_names) + 1}: ").strip()
        if not name:
            print("Name cannot be empty. ")
            continue
        name_lower = name.lower()
        if name_lower in unique_names:
            print(f"'{name} is a duplication of '{unique_names[name_lower]}'. Please enter a different name")
        else:
            unique_names[name_lower] = name
    return list(unique_names.values())

collected = unique_name_collector()
print(f"\nCollected: {collected}")