import bcrypt

def hash_password(password: str) -> bytes:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)

def verify_password(password: str, hashed: bytes):
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed)

stored_username = "admin"
stored_password_hash = hash_password("admin123")

def login():
    username = input("Username: ").strip().lower()
    password = input("Password: ")

    if username != stored_username:
        print("Access denied")
        return
    if verify_password(password, stored_password_hash):
        print("Access granted")
    else:
        print("Access denied")

login()
