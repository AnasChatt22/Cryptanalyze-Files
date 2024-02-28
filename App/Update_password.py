import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import Profil as pf
import Session as ss
import Settings as st


def Update_password(root):
    def back(framepwd):
        framepwd.destroy()
        pf.Profil(root)

    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    logout_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logout.png")

    image_back = ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65))
    logo_nav = ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38))
    image_logout = ctk.CTkImage(light_image=Image.open(logout_path), size=(33, 36))

    # Main Frame
    framePwd = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    framePwd.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBarPwd = ctk.CTkFrame(master=framePwd, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarPwd.pack()

    label_logo_nav_pwd = ctk.CTkLabel(master=NavBarPwd, text="", image=logo_nav)
    label_logo_nav_pwd.place(x=10, y=10)

    label_logout = ctk.CTkButton(master=NavBarPwd, text="", image=image_logout, hover=False, fg_color="transparent",
                                 width=33, bg_color="transparent", cursor="hand2",
                                 command=lambda: st.logout(root, framePwd))
    label_logout.place(x=1300, y=10)

    # "Profil" Label and back button

    button_back = ctk.CTkButton(master=framePwd, text="", image=image_back, hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: back(framePwd))
    button_back.place(x=36, y=70)

    label_pwd = ctk.CTkLabel(master=framePwd, text="Update Password",
                             font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_pwd.place(x=150, y=88)
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)

    # Existant password
    pwd_exist_label = ctk.CTkLabel(master=framePwd, text="Existing password",
                                   font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    pwd_exist_label.place(relx=0.34, rely=0.31)

    pwd_exist_entry = ctk.CTkEntry(framePwd, width=250, height=40, font=InputFont,
                                   placeholder_text="Existant password", text_color="#000")
    pwd_exist_entry.place(relx=0.55, rely=0.33, anchor=tk.CENTER)

    # New password
    new_pwd_label = ctk.CTkLabel(master=framePwd, text="New password",
                                 font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    new_pwd_label.place(relx=0.34, rely=0.41)

    new_pwd_entry = ctk.CTkEntry(framePwd, width=250, height=40, font=InputFont,
                                 placeholder_text="Nouveau password", text_color="#000")
    new_pwd_entry.place(relx=0.55, rely=0.43, anchor=tk.CENTER)

    # Confirm new password
    conf_pwd_label = ctk.CTkLabel(master=framePwd, text="Confirm password",
                                  font=ctk.CTkFont(family="Microsoft YaHei UI", size=16, weight="bold"))
    conf_pwd_label.place(relx=0.34, rely=0.51)

    conf_pwd_entry = ctk.CTkEntry(framePwd, width=250, height=40, font=InputFont,
                                  placeholder_text="Confirmer password", text_color="#000")
    conf_pwd_entry.place(relx=0.55, rely=0.53, anchor=tk.CENTER)

    # Update Button
    def update_pwd():
        print("Hello")
        exist_pwd = pwd_exist_entry.get()
        new_pwd = new_pwd_entry.get()
        conf_pwd = conf_pwd_entry.get()
        # Check for empty fields
        if not (exist_pwd and new_pwd and conf_pwd):
            messagebox.showerror("Error", "All fields are required.")
            return

        hash_exist_pwd = st.hash_password(exist_pwd)
        query = f"Select password from users where username='{ss.current_user}'"
        result = DB.fetchall(query)
        if result:
            pwd = result[0][0]
            if pwd == hash_exist_pwd:
                # Check if passwords match
                if new_pwd != conf_pwd:
                    messagebox.showerror("Error", "Passwords do not match.")
                    return
                # Validate the password strength
                password_error = st.validate_password(new_pwd)
                if password_error:
                    messagebox.showerror("Error", password_error)
                    return
                hash_new_pwd = st.hash_password(new_pwd)
                query2 = f"UPDATE users SET password='{hash_new_pwd}' WHERE username='{ss.current_user}'"
                if DB.execute_query(query2):
                    messagebox.showinfo("Update Password", "Password updated successfully")
                else:
                    messagebox.showerror("Update Password", "Password not updated!!")
        else:
            messagebox.showerror("Update Password", "Unable to check existing usernames.")

    update_btn = ctk.CTkButton(framePwd, text="Update", font=InputFont, width=75, height=35,
                               text_color="#000", cursor="hand2",
                               hover_color="#DAE5F4", fg_color="#7F8CD9", command=update_pwd)
    update_btn.place(relx=0.48, rely=0.65, anchor=tk.CENTER)

    # Logout after no activity
    framePwd.bind("<Button-1>", lambda event: ss.on_user_interaction(root, framePwd))
