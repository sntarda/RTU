import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names: ["Samir Tarda", "John Martini"]
usernames: ["starda", "jmartini"]
passwords: ["pass815714", "pass4321"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
