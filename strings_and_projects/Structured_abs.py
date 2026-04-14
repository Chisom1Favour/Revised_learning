def get_input() -> str:
    return input("Enter name: ")

def normalize(name: str) -> str:
    return name.strip().lower()

def is_admin(name: str) -> bool:
    return normalize(name) == "admin"

def grant_access():
    print("Accesss granted")

def deny_access():
    print("Access denied")

name = get_input()
if is_admin(name):
    grant_access()
else:
    deny_access()