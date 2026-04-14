import bcrypt
password = b"mysecretpassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)