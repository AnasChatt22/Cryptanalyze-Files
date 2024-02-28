import hashlib
import random
import re
import string
import tkinter as tk

import customtkinter as ctk

import HomePage as hp
import SignIn as si
import Session as ss


def alert_box(root, message):
    frame = ctk.CTkFrame(master=root, fg_color="#fff", bg_color="transparent",
                         corner_radius=50, width=300, height=200)
    frame.place(x=550, y=250)
    message = ctk.CTkLabel(master=frame, text=message, text_color="#000")
    message.place(x=275, y=125, anchor=tk.CENTER)


def hash_password(password):
    # Use a strong hashing algorithm (e.g., SHA-256)
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()


def generate_token(length=20):
    # Generate a random token using letters and digits
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def logout(root, frame):
    ss.end_session()
    frame.destroy()
    si.SignIn(root)


def back(root, frame):
    frame.destroy()
    hp.HomePage(root)


def validate_email(email):
    # Define a regular expression pattern for a Gmail email address
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email)


def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    # Check if the password contains at least one digit (number)
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."

    # Check if the password contains at least one special character
    special_characters = set("!@#$%^&*()_-+=<>?/{}[]|")
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."

    # If all checks pass, the password is valid
    return None
