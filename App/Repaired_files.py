import os
import tkinter as tk

import customtkinter as ctk
from PIL import Image

import Settings as st
import StockCryptFiles as scf
import StockDecryptFiles as sdf


def Repaired_files(root):
    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    image_back = ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65))
    logo_nav = ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38))

    # Main Frame
    frameRepFich = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameRepFich.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBarRepFich = ctk.CTkFrame(master=frameRepFich, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarRepFich.pack()

    label_logo_nav_df = ctk.CTkLabel(master=NavBarRepFich, text="", image=logo_nav)
    label_logo_nav_df.place(x=10, y=10)

    # Label and back button
    button_back = ctk.CTkButton(master=frameRepFich, text="", image=image_back, hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: st.back(root, frameRepFich))
    button_back.place(x=36, y=70)

    label_df = ctk.CTkLabel(master=frameRepFich, text="Repaired Files",
                            font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_df.place(x=150, y=88)

    def open_frame(num):
        frameRepFich.destroy()
        match num:
            case 1:
                sdf.StockDecryptFiles(root)
            case 2:
                scf.StockCryptFiles(root)

    # Buttons
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")
    home1_path = os.path.join(os.path.dirname(__file__), "images", "logo", "decrypt.png")
    image_Home_1 = ctk.CTkImage(light_image=Image.open(home1_path), size=(88, 96))
    button1 = ctk.CTkButton(master=frameRepFich, font=ButtonsFont, width=380, height=230,
                            text="Storage of decrypted files", image=image_Home_1, text_color="#000", fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_frame(1))
    button1.place(x=300, y=250)
    home2_path = os.path.join(os.path.dirname(__file__), "images", "logo", "labo.png")
    image_Home_2 = ctk.CTkImage(light_image=Image.open(home2_path), size=(88, 96))
    button2 = ctk.CTkButton(master=frameRepFich, font=ButtonsFont, width=380, height=230,
                            text="Storage of crypted files", image=image_Home_2, text_color="#000", fg_color="#fff",
                            bg_color="transparent", hover_color="#DAE5F4", corner_radius=20,
                            compound="top", cursor="hand2", command=lambda: open_frame(2))
    button2.place(x=700, y=250)
