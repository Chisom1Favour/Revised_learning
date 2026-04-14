def safe_collector(count=2, max_attempts=10):
    unique_names = {}
    attempts = 0

    while len(unique_names) < count and attempts < max_attempts:
        name = input("Enter name: ").strip()

       if not name:
        print('Empty name! Try again') 

        if name.lower() in unique_names:
            print(f"Duplicate! {max_attempts - attempts} attempts left")
            attempts += 1
        else:
            unique_names[name.lower()] = name

    if len(unique_names) < count:
        print("Maximum attemost reached. Exiting")

    return list(unique_names.values())

result = safe_collector()
print(f"Names collected {result}")
