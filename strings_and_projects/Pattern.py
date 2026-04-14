def get_input() -> str:
    return input("Enter name: ")

def matches(value: str, target: str) -> bool:
    return value.strip().lower() == target.lower()

name = get_input()
if matches(name, "admin"):
    print("Access granted")
