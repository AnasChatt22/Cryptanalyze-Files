import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import Session as ss
import Settings as st
import Update_password as up

email = None
firstName = None
lastName = None


def Profil(root):
    global email, firstName, lastName

    def collect_infs():
        global email, firstName, lastName
        query = f"Select email,prenom,nom from users where username = '{ss.current_user}'"
        result = DB.fetchall(query)
        if result:
            email = result[0][0]
            firstName = result[0][1]
            lastName = result[0][2]

    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    logout_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logout.png")
    image_back = ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65))
    logo_nav = ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38))
    image_logout = ctk.CTkImage(light_image=Image.open(logout_path), size=(33, 36))

    # Main Frame
    frameProfil = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameProfil.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBarProfile = ctk.CTkFrame(master=frameProfil, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarProfile.pack()

    label_logo_nav_pf = ctk.CTkLabel(master=NavBarProfile, text="", image=logo_nav)
    label_logo_nav_pf.place(x=10, y=10)

    label_logout = ctk.CTkButton(master=NavBarProfile, text="", image=image_logout, hover=False, fg_color="transparent",
                                 width=33, bg_color="transparent", cursor="hand2",
                                 command=lambda: st.logout(root, frameProfil))
    label_logout.place(x=1300, y=10)

    # "Profil" Label and back button
    button_back = ctk.CTkButton(master=frameProfil, text="", image=image_back, hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: st.back(root, frameProfil))
    button_back.place(x=36, y=70)

    label_pf = ctk.CTkLabel(master=frameProfil, text="Profil Informations",
                            font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_pf.place(x=150, y=88)

    # Labels and Entries
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)

    # Firstname
    collect_infs()
    firstname_label = ctk.CTkLabel(master=frameProfil, text="First name",
                                   font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    firstname_label.place(relx=0.24, rely=0.31)

    firstname_var = ctk.StringVar(master=frameProfil)
    if firstName:
        firstname_var.set(firstName)

    firstname_entry = ctk.CTkEntry(frameProfil, width=250, height=40, font=InputFont, textvariable=firstname_var,
                                   placeholder_text="Prénom", text_color="#000")
    firstname_entry.place(relx=0.4, rely=0.33, anchor=tk.CENTER)

    # LastName
    lastname_var = ctk.StringVar(master=frameProfil)
    if lastName:
        lastname_var.set(lastName)

    lastname_label = ctk.CTkLabel(master=frameProfil, text="Last name",
                                  font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    lastname_label.place(relx=0.54, rely=0.31)

    lastname_entry = ctk.CTkEntry(frameProfil, width=250, height=40, font=InputFont, textvariable=lastname_var,
                                  placeholder_text="Nom", text_color="#000")
    lastname_entry.place(relx=0.7, rely=0.33, anchor=tk.CENTER)

    # Email Input
    email_var = ctk.StringVar(master=frameProfil)
    if email:
        email_var.set(email)

    email_label = ctk.CTkLabel(master=frameProfil, text="Email",
                               font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    email_label.place(relx=0.24, rely=0.39)

    email_entry = ctk.CTkEntry(frameProfil, width=250, height=40, font=InputFont, textvariable=email_var,
                               placeholder_text="Email", text_color="#000")
    email_entry.place(relx=0.4, rely=0.41, anchor=tk.CENTER)

    # UserName Input
    username_var = ctk.StringVar(master=frameProfil)
    if ss.current_user:
        username_var.set(ss.current_user)

    username_label = ctk.CTkLabel(master=frameProfil, text="Username",
                                  font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    username_label.place(relx=0.54, rely=0.39)

    username_entry = ctk.CTkEntry(frameProfil, width=250, height=40, font=InputFont, textvariable=username_var,
                                  placeholder_text="Nom utilisateur", text_color="#000")
    username_entry.place(relx=0.7, rely=0.41, anchor=tk.CENTER)

    # Update button
    def update_pf():
        new_username = username_entry.get()
        query = (f"UPDATE users SET username='{new_username}', "
                 f"nom='{lastname_entry.get()}', prenom='{firstname_entry.get()}', email='{email_entry.get()}' "
                 f"WHERE username='{ss.current_user}'")
        query2 = f"SELECT username FROM users"
        result = DB.fetchall(query2)

        if not result:
            # Handle the case where the result is empty
            messagebox.showerror("Update failed!", "Unable to check existing usernames.")
            return

        existing_usernames = [row[0] for row in result]

        if new_username != ss.current_user and new_username in existing_usernames:
            messagebox.showerror("Update failed!", "Username is already existing!")
        else:
            if DB.execute_query(query):
                lastname_var.set(lastname_entry.get())
                firstname_var.set(firstname_entry.get())
                email_var.set(email_entry.get())
                username_var.set(username_var.get())
                ss.current_user = username_var.get()
                messagebox.showinfo("Update Success", "Profile updated successfully!")
            else:
                messagebox.showerror("Update Error", "Check again the information")

    update_btn = ctk.CTkButton(frameProfil, text="Update", font=InputFont, width=75, height=35,
                               text_color="#000", cursor="hand2",
                               hover_color="#DAE5F4", fg_color="#7F8CD9", command=update_pf)
    update_btn.place(relx=0.5, rely=0.58, anchor=tk.CENTER)

    # Modify password
    def update_pwd():
        frameProfil.destroy()
        up.Update_password(root)

    update_pwd_btn = ctk.CTkButton(frameProfil, text="Update password?", width=20, fg_color="transparent",
                                   font=ctk.CTkFont(family="Cabin", underline=True, size=17, weight="bold"),
                                   text_color="#293040", hover=False, cursor="hand2", command=update_pwd)
    update_pwd_btn.place(relx=0.5, rely=0.67, anchor=tk.CENTER)

    # Logout after no activity
    frameProfil.bind("<Button-1>", lambda event: ss.on_user_interaction(root, frameProfil))
