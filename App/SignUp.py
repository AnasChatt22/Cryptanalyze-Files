import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import Settings as st
import SignIn as si


def SignUp(root):
    # Fonts
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)
    HeadingFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=48, weight="bold")
    labelFont = ctk.CTkFont("Microsoft YaHei UI Light", 14)

    # images
    back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    logo_signUp = ctk.CTkImage(light_image=Image.open(logo_path), size=(451, 97))
    image_back = ctk.CTkImage(light_image=Image.open(back_path), size=(65, 65))

    def sign_up():
        try:
            # Get input values
            username = username_signUp.get()
            lastname = lastname_signUp.get()
            firstname = firstname_signUp.get()
            email = email_signUp.get()
            password1 = password1_signUp.get()
            password2 = password2_signUp.get()

            # Check for empty fields
            if not (username and lastname and firstname and email and password1 and password2):
                messagebox.showerror("Error", "All fields are required.")
                return

            # Check if passwords match
            if password1 != password2:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            # Validate the email pattern
            if not st.validate_email(email):
                messagebox.showerror("Error", "Invalid email address. Please use a Gmail address.")
                return

            # Validate the password strength
            password_error = st.validate_password(password1)
            if password_error:
                messagebox.showerror("Error", password_error)
                return

            # Check if the terms and conditions are accepted
            if check_var.get() != "on":
                messagebox.showerror("Error", "Please accept the Terms and Conditions.")
                return

            # Hash the password before storing it in the database
            hashed_password = st.hash_password(password1)

            # Query to insert a new user
            insert_query = f"INSERT INTO users (username, Nom, Prenom, Email, Password) " \
                           f"VALUES ('{username}', '{lastname}', '{firstname}', '{email}', '{hashed_password}')"

            if DB.execute_query(insert_query):
                messagebox.showinfo("Success", "Registration successful! You can now sign in.")
                open_signin()
            else:
                messagebox.showerror("Error", "Username already exists.")
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error : {e}")

    def open_signin():
        frameSignUp.destroy()
        si.SignIn(root)

    frameSignUp = ctk.CTkFrame(master=root, fg_color="#fff", bg_color="#fff")
    frameSignUp.pack(fill=tk.BOTH, expand=True)

    # Back Button
    button_back = ctk.CTkButton(master=frameSignUp, text="", image=image_back, hover=False,
                                compound="top", cursor="hand2", bg_color="transparent", fg_color="transparent",
                                command=open_signin)
    button_back.place(x=36, y=70)

    # Put Logo
    label_logo_signUp = ctk.CTkLabel(master=frameSignUp, text="", image=logo_signUp)
    label_logo_signUp.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Sign Up Label
    heading_signUp = ctk.CTkLabel(master=frameSignUp, text="Sign Up", font=HeadingFont, text_color="#000")
    heading_signUp.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Name Input
    firstname_signUp = ctk.CTkEntry(master=frameSignUp, width=250, height=40, font=InputFont,
                                    placeholder_text="First name", text_color="#000")
    firstname_signUp.place(relx=0.4, rely=0.43, anchor=tk.CENTER)

    lastname_signUp = ctk.CTkEntry(master=frameSignUp, width=250, height=40, font=InputFont,
                                   placeholder_text="Last name", text_color="#000")
    lastname_signUp.place(relx=0.6, rely=0.43, anchor=tk.CENTER)

    # Email Input
    email_signUp = ctk.CTkEntry(master=frameSignUp, width=250, height=40, font=InputFont,
                                placeholder_text="Email", text_color="#000")
    email_signUp.place(relx=0.4, rely=0.51, anchor=tk.CENTER)

    # UserName Input
    username_signUp = ctk.CTkEntry(master=frameSignUp, width=250, height=40, font=InputFont,
                                   placeholder_text="Username", text_color="#000")
    username_signUp.place(relx=0.6, rely=0.51, anchor=tk.CENTER)

    # Password Input
    password1_signUp = ctk.CTkEntry(master=frameSignUp, width=250, height=40, font=InputFont,
                                    placeholder_text="Password", text_color="#000")
    password1_signUp.place(relx=0.4, rely=0.59, anchor=tk.CENTER)

    password2_signUp = ctk.CTkEntry(master=frameSignUp, width=250, height=40, font=InputFont,
                                    placeholder_text="Confirm password", text_color="#000")
    password2_signUp.place(relx=0.6, rely=0.59, anchor=tk.CENTER)

    # Accept conditions
    check_var = ctk.StringVar(value="off")
    checkbox = ctk.CTkCheckBox(master=frameSignUp, text="I accept Terms and Conditions", checkmark_color="black",
                               fg_color="#7F8CD9",
                               hover_color="#7F8CD9", variable=check_var, onvalue="on", offvalue="off")
    checkbox.place(relx=0.5, rely=0.66, anchor=tk.CENTER)

    # Sign Up Button
    SignUpButton2 = ctk.CTkButton(master=frameSignUp, text="Sign Up", font=InputFont, width=50, height=25,
                                  text_color="#000",
                                  hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2", command=sign_up)
    SignUpButton2.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

    # Do you already have account? Label
    label_signUp = ctk.CTkLabel(master=frameSignUp, text="Do you already have account?", font=labelFont)
    label_signUp.place(relx=0.5, rely=0.79, anchor=tk.CENTER)

    # Sign In Button
    SignInButton2 = ctk.CTkButton(master=frameSignUp, text="Sign In", width=20, fg_color="transparent",
                                  font=ctk.CTkFont(underline=True, weight="bold"),
                                  text_color="#293040", hover=False, cursor="hand2", command=open_signin)
    SignInButton2.place(relx=0.5, rely=0.84, anchor=tk.CENTER)
