def unique_name_collector(count=2):
    unique_names = {}
    while len(unique_names) < count:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty. Try again")
            continue # Don't store garbage
        if len(name) < 2:
            print("Name is too short")
            continue
        if any(char.isdigit() for char in name):
            print("Names shouldn't contain numbers")
            continue
        unique_names[name.lower()] = name
    return list(unique_names.values())

result = unique_name_collector()
print(f"Collected names: {result}")