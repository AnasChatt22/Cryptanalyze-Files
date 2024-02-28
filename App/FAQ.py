import os
import tkinter as tk

import customtkinter as ctk
from PIL import Image

import Settings as st


def FAQ(root):
    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")

    # Main Frame
    frameContact = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameContact.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBarCom = ctk.CTkFrame(master=frameContact, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarCom.pack()

    label_logo_nav = ctk.CTkLabel(master=NavBarCom, text="",
                                  image=ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38)))
    label_logo_nav.place(x=10, y=10)

    # Label and back button
    button_back = ctk.CTkButton(master=frameContact, text="",
                                image=ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65)), hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: st.back(root, frameContact))
    button_back.place(x=36, y=70)

    label_comment = ctk.CTkLabel(master=frameContact, text="FAQ",
                                 font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_comment.place(x=150, y=88)

    # Accordian Frame
    Accordion = ctk.CTkScrollableFrame(master=frameContact, fg_color="white", bg_color="transparent",
                                       corner_radius=20, width=1340, height=500)
    Accordion.place(x=10, y=140)

    # Description of functionality
    label_description = ctk.CTkLabel(master=Accordion,
                                     text="Our support team answers these questions almost every day",
                                     font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=24, weight="bold"))
    label_description.pack()
    label_advice = ctk.CTkLabel(master=Accordion,
                                text="The general advice is not to pay the ransom. By sending your money to cybercriminals you’ll only confirm that ransomware works, and there’s no guarantee you’ll get the decryption key you need in return.",
                                font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold"),
                                wraplength=1000)
    label_advice.pack(pady=20, padx=20)

    id = 0
    options_values = {}

    def add_option(option, value, wraplength=1000):

        nonlocal id

        option_frame = ctk.CTkFrame(master=Accordion)

        option_label = ctk.CTkLabel(option_frame, text=option, text_color="black", fg_color="white",
                                    bg_color="transparent", anchor="w", cursor="hand2")
        option_label.pack(side="left", anchor="w", expand=1, fill='both')
        option_label.bind("<Enter>", lambda event: option_label.configure(text_color="#7F8CD9"))
        option_label.bind("<Leave>", lambda event: option_label.configure(text_color="black"))

        option_frame.pack(fill="x", expand=1, pady=20, padx=20)

        value_label = ctk.CTkLabel(Accordion, text=value, fg_color="white", bg_color="transparent",
                                   wraplength=wraplength, justify="left")
        x = id
        option_label.bind("<Button-1>", lambda event: open_close(event, x))

        options_values[id] = [False, option_frame, value_label]

        id += 1

    def open_close(event, id_):
        if options_values[id_][0]:
            options_values[id_][0] = False
            options_values[id_][2].pack_forget()
            return

        # remove all the options and values and show the value of option currently
        # clicked and then show the removed options again

        for key in options_values:
            if key != id_:
                if options_values[key][0]:
                    options_values[key][2].pack_forget()
                    options_values[key][0] = False
                if key > id_:
                    options_values[key][1].pack_forget()

        options_values[id_][2].pack(anchor="w", expand=1, fill='x', pady=1)
        options_values[id_][0] = True

        for key in range(id_ + 1, len(options_values)):
            options_values[key][1].pack(fill='x', expand=1, pady=20, padx=20)

    # FAQ
    Q1 = "How to encrypt a file with FileCipher?"
    R1 = "To encrypt a file, select the encryption option from the main menu, choose the encryption algorithm, then follow the instructions to select the target file and perform encryption."

    Q2 = "Does FileCipher support decryption of files encrypted by other applications?"
    R2 = "Yes, FileCipher supports decryption of files encrypted by other applications, provided you have the appropriate decryption key or the encryption used is supported by FileCipher."

    Q3 = "How can I cryptanalyze a ransomware infected file with FileCipher?"
    R3 = "To cryptanalyze a file affected by ransomware, select the File Decryption option from the main menu, then follow the instructions to select the target file and perform cryptanalysis."

    Q4 = "What encryption algorithms are recommended to ensure file security?"
    R4 = "FileCipher offers several encryption algorithms, such as RSA and AES. It is recommended to use reputable algorithms to ensure the security of encrypted files."

    add_option(option=Q1, value=R1)
    add_option(option=Q2, value=R2)
    add_option(option=Q3, value=R3)
    add_option(option=Q4, value=R4)
