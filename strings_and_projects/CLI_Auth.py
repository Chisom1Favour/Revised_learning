import bcrypt
import time
# =============================
# CONFIG
# =============================
MAX_ATTEMPTS = 3
LOCKOUT_TIME = 10 # Seconds

# =============================
# PASSWORD UTILS
# =============================

def hash_password()