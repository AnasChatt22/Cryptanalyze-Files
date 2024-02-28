import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import HomePage as hp
import Session as ss
import Settings as st
import SignUp as su


def SignIn(root):
    # Fonts
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)
    HeadingFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=48, weight="bold")
    labelFont = ctk.CTkFont("Microsoft YaHei UI Light", 14)

    # images
    logo_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")

    logo_signIn = ctk.CTkImage(light_image=Image.open(logo_path), size=(569, 116))

    def sign_in():
        user = username_signIn.get()
        pwd = pwd_signIn.get()

        if user == "" or pwd == "":
            messagebox.showerror("Invalid Inputs", "Error! Username/Password cannot be empty")
            return

        entered_password_hash = st.hash_password(pwd)

        try:
            # Replace 'your_user_table' and 'your_password_column' with your actual table and column names
            query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{entered_password_hash}'"

            result = DB.fetchall(query)

            if result:
                # User exists with the provided username and password
                token = st.generate_token()
                # Update user token in database
                ss.update_user_token(user, token)
                # Log user connection
                ss.log_user_connection(user, token)
                # Start user session
                ss.start_session(user)

                frameSignIn.destroy()
                hp.HomePage(root)
            else:
                messagebox.showerror("Invalid Inputs", "Error! Username/Password incorrect")
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error : {e}")

    def open_signup():
        frameSignIn.destroy()
        su.SignUp(root)

    frameSignIn = ctk.CTkFrame(master=root, fg_color="#fff", bg_color="#fff")
    frameSignIn.pack(fill=tk.BOTH, expand=True)

    frameFormSignIn = ctk.CTkFrame(master=frameSignIn, width=700, fg_color="#fff")
    frameFormSignIn.pack(side=tk.RIGHT, fill=tk.Y)

    frameImage_signIn = ctk.CTkFrame(master=frameSignIn, width=690, height=690, fg_color="#000000")
    frameImage_signIn.place(x=350, y=350, anchor=tk.CENTER)

    # Image Widget
    label_logo_signIn = ctk.CTkLabel(master=frameImage_signIn, text="", image=logo_signIn)
    label_logo_signIn.place(x=80, y=277)

    # Sign In Heading
    heading_signIn = ctk.CTkLabel(master=frameFormSignIn, text="Sign In", font=HeadingFont, text_color="#000")
    heading_signIn.place(x=340, y=120, anchor=tk.CENTER)

    # UserName Input
    username_signIn = ctk.CTkEntry(master=frameFormSignIn, width=250, height=40, font=InputFont,
                                   placeholder_text="Username", text_color="#000")
    username_signIn.place(x=340, y=250, anchor=tk.CENTER)

    # Password
    pwd_signIn = ctk.CTkEntry(master=frameFormSignIn, width=250, height=40, font=InputFont,
                              placeholder_text="Password", show="•", text_color="#000")
    pwd_signIn.place(x=340, y=320, anchor=tk.CENTER)

    # Sign in Button
    SignInButton = ctk.CTkButton(master=frameFormSignIn, text="Sign In", font=InputFont, width=55, height=30,
                                 text_color="#000",
                                 hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2", command=sign_in)
    SignInButton.place(x=340, y=380, anchor=tk.CENTER)
    frameSignIn.bind("<Return>", lambda event=None: SignInButton.invoke())

    # Sign up Button
    label_signIn = ctk.CTkLabel(master=frameFormSignIn, text="Don't have an account yet ?", font=labelFont)
    label_signIn.place(x=340, y=430, anchor=tk.CENTER)

    SignUpButton = ctk.CTkButton(master=frameFormSignIn, text="Sign Up", width=20, fg_color="transparent",
                                 font=ctk.CTkFont(underline=True, weight="bold"),
                                 text_color="#293040", hover=False, cursor="hand2", command=open_signup)
    SignUpButton.place(x=340, y=460, anchor=tk.CENTER)
