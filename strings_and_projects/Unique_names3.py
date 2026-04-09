def unique_names_collector(count=2):
    unique_names = {}

    if count <= 0:
        print("Count must be positive")
        return []
    print(f"Please enter {count} unique names (case-insensitive):")

    while len(unique_names) < count:
        name = input(f"Enter name #{len(unique_names) + 1}: ").strip()

        if not name:
            print("Name cannot be empty. Please try again")
            continue

        name_lower = name.lower()

        if name_lower in unique_names:
            print(f"'{name}' is a duplicate. Please enter a different name")
        else:
            unique_names[name_lower] = name


    return list(unique_names.values())


names3 = unique_names_collector(2)
names6 = unique_names_collector(2)
names_default = unique_names_collector()