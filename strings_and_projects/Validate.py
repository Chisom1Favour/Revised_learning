def validate(name: str) -> bool:
    return isinstance(name, str) and len(name.strip()) > 0

def process(name: str):
    if not validate(name):
        print("Invalid input")
        return
    