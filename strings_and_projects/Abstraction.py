def normalize(name: str) -> str:
    return name.strip().lower()

def is_admin(name: str) -> bool:
    return normalize(name) == "admin"

name = input('Enter name: ')
if is_admin(name):
    print("Access granted")
else:
    print("Access denied")