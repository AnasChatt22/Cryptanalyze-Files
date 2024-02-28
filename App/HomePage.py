import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
import requests
from PIL import Image

import Decryption_tool as dt
import FAQ
import File_decryption as fd
import File_encryption as fe
import Implementation_lab as il
import Profil as pl
import Repaired_files as rf
import Session as ss
import Settings as st


def HomePage(root):
    # Fonts
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")
    # images
    profil_path = os.path.join(os.path.dirname(__file__), "images", "logo", "profil.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    home1_path = os.path.join(os.path.dirname(__file__), "images", "logo", "decrypt.png")
    home2_path = os.path.join(os.path.dirname(__file__), "images", "logo", "labo.png")
    home3_path = os.path.join(os.path.dirname(__file__), "images", "logo", "tool.png")
    home4_path = os.path.join(os.path.dirname(__file__), "images", "logo", "filerep.png")
    home5_path = os.path.join(os.path.dirname(__file__), "images", "logo", "crypt.png")
    logout_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logout.png")
    help_path = os.path.join(os.path.dirname(__file__), "images", "logo", "help.png")

    logo_nav = ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38))
    profil = ctk.CTkImage(light_image=Image.open(profil_path), size=(33, 28))
    image_Home_1 = ctk.CTkImage(light_image=Image.open(home1_path), size=(88, 96))
    image_Home_2 = ctk.CTkImage(light_image=Image.open(home2_path), size=(88, 96))
    image_Home_3 = ctk.CTkImage(light_image=Image.open(home3_path), size=(88, 96))
    image_Home_4 = ctk.CTkImage(light_image=Image.open(home4_path), size=(100, 96))
    image_Home_5 = ctk.CTkImage(light_image=Image.open(home5_path), size=(88, 96))
    image_logout = ctk.CTkImage(light_image=Image.open(logout_path), size=(33, 36))
    help = ctk.CTkImage(light_image=Image.open(help_path), size=(53, 50))

    def get_file_report():
        url = 'https://www.google.com'
        response = requests.get(url)
        print(response)
        return response

    def open_tool(num):
        frameHome.destroy()
        match num:
            case 1:
                if get_file_report():
                    messagebox.showinfo('Error', "No connection to internet !")
                else:
                    fd.File_decryption(root)
            case 2:
                il.Implementation_lab(root)
            case 3:
                dt.Decryption_tool(root)
            case 4:
                rf.Repaired_files(root)
            case 5:
                fe.File_encryption(root)
            case 6:
                FAQ.FAQ(root)
            case 7:
                pl.Profil(root)

    # Main frame Home Page
    frameHome = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameHome.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBar = ctk.CTkFrame(master=frameHome, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBar.pack()

    label_logo_nav = ctk.CTkLabel(master=NavBar, text="", image=logo_nav)
    label_logo_nav.place(x=10, y=10)

    label_profil = ctk.CTkButton(master=NavBar, text="", image=profil, hover=False, fg_color="transparent",
                                 width=33, bg_color="transparent", cursor="hand2", command=lambda: open_tool(7))
    label_profil.place(x=1230, y=12)

    label_logout = ctk.CTkButton(master=NavBar, text="", image=image_logout, hover=False, fg_color="transparent",
                                 width=33, bg_color="transparent", cursor="hand2",
                                 command=lambda: st.logout(root, frameHome))
    label_logout.place(x=1300, y=10)

    # Buttons
    button1 = ctk.CTkButton(master=frameHome, font=ButtonsFont, width=380, height=230,
                            text="File Decryption", image=image_Home_1, text_color="#000", fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_tool(1))
    button1.place(x=100, y=100)

    button2 = ctk.CTkButton(master=frameHome, font=ButtonsFont, width=380, height=230,
                            text="Implementation Lab", image=image_Home_2, text_color="#000", fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_tool(2))
    button2.place(x=510, y=100)

    button3 = ctk.CTkButton(master=frameHome, font=ButtonsFont, width=380, height=230,
                            text="Decryption Tools", image=image_Home_3, text_color="#000",
                            fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_tool(3))
    button3.place(x=920, y=100)

    button4 = ctk.CTkButton(master=frameHome, font=ButtonsFont, width=380, height=230,
                            text="Repaired Files", image=image_Home_4, text_color="#000",
                            fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_tool(4))
    button4.place(x=100, y=360)

    button5 = ctk.CTkButton(master=frameHome, font=ButtonsFont, width=380, height=230,
                            text="File Encryption", image=image_Home_5, text_color="#000", fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_tool(5))
    button5.place(x=510, y=360)

    # FAQ
    label_FAQ = ctk.CTkButton(master=frameHome, text="", image=help, hover=False, fg_color="transparent",
                              width=33, bg_color="transparent", cursor="hand2", command=lambda: open_tool(6))
    label_FAQ.place(x=1300, y=600)

    # Logout after no activity
    frameHome.bind("<Button-1>", lambda event: ss.on_user_interaction(root, frameHome))
