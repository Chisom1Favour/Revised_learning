# GIGO in action
def unique_name_collector(count=2):
    unique_names = {}
    while len(unique_names) < count:
        name = input("Enter name: ")
        unique_names[name.lower()] = name
    return list(unique_names.values())

result = unique_name_collector()
print(f"Collected names: {result}")
