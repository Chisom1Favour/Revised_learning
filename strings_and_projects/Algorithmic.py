def is_admin(name: str) -> bool:
    # Step 1: normalize
    cleaned = name.strip().lower()
    # Step 2: compare
    if cleaned == "admin":
        return True
    else:
        return False
    

def validate(name: str) -> bool:
    return isinstance(name, str) and len(name.strip()) > 0

def process(name: str):
    if not validate(name):
        print("Invalid input")
        return
    if is_admin(name):
        print("Access granted")
    else:
        print("Access denied")