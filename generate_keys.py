import pickle
from pathlib import Path
import hashlib

# Define user credentials
names = ["Samir Tarda", "John Martini"]
usernames = ["starda", "jmartini"]
passwords = ["pass815714", "pass4321"]

# Function to hash passwords using hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hash the passwords
hashed_passwords = [hash_password(password) for password in passwords]

# Define the path to save the hashed passwords
file_path = Path("hashed_pw.pkl")

# Save the hashed passwords to a file
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print("Hashed passwords saved successfully.")
