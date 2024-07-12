import pickle
from pathlib import Path

import streamlit_authenticator as stauth

# Define user details
names = ["Samir Tarda", "John Martini"]
usernames = ["starda", "jmartini"]
passwords = ["pass815714", "pass4321"]  # Replace with actual passwords

# Generate hashed passwords
hashed_passwords = stauth.Hasher(passwords).generate()

# Save hashed passwords to a file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
