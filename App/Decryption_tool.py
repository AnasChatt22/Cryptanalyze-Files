import os
import tkinter as tk
import webbrowser
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import Settings as st

old_id = 1
new_id = 4


def Decryption_tool(root):
    # Fonts
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")

    def open_link(link):
        webbrowser.open_new(link)

    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    copyright_path = os.path.join(os.path.dirname(__file__), "images", "logo", "copyright.png")

    # Main Frame
    frameDecTool = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameDecTool.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBarDecTool = ctk.CTkFrame(master=frameDecTool, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarDecTool.pack()

    label_logo_nav_df = ctk.CTkLabel(master=NavBarDecTool, text="",
                                     image=ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38)))
    label_logo_nav_df.place(x=10, y=10)

    # Label and back button
    button_back = ctk.CTkButton(master=frameDecTool, text="",
                                image=ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65)), hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: st.back(root, frameDecTool))
    button_back.place(x=36, y=70)

    label_df = ctk.CTkLabel(master=frameDecTool, text="Decryption Tools",
                            font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_df.place(x=150, y=88)

    # Search Bar
    search_box = ctk.CTkEntry(master=frameDecTool, width=400, height=40, font=ButtonsFont,
                              placeholder_text="Search Tool by Ransom name", text_color="#000")
    search_box.place(x=450, y=160)

    def search():
        ransom = search_box.get()
        if ransom == "":
            messagebox.showwarning("Warning", "Please fill the search box")
            return

        query = f"SELECT Name, Description, Guide, Tool, made_by FROM tools where Name LIKE '%{ransom}%'"
        result = DB.fetchall(query)

        if result:
            for i in options_values:
                options_values[i][1].destroy()
                options_values[i][2].destroy()
                options_values[i][3].destroy()
                options_values[i][4].destroy()
                options_values[i][5].destroy()
                options_values[i][0] = False
            button_load.pack_forget()
            Accordion._scrollbar._command("moveto", 0.0)
            print("Ransom found")
            for tool in result:
                add_option(option=tool[0], Tool_name=tool[1], guide_link=tool[2], download_link=tool[3],
                           Tool_maker=tool[4])
        else:
            search_box.delete(0, tk.END)
            messagebox.showinfo("Not Found", "No ransom with this name found")

    # Search Button
    search_button = ctk.CTkButton(master=frameDecTool, text="Search", font=ButtonsFont, width=60, height=41,
                                  text_color="#000",
                                  hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2", command=search)
    search_button.place(x=860, y=160)

    def Reset():
        global old_id, new_id
        old_id = 1
        new_id = 4
        search_box.delete(0, tk.END)
        for i in options_values:
            options_values[i][1].destroy()
            options_values[i][2].destroy()
            options_values[i][3].destroy()
            options_values[i][4].destroy()
            options_values[i][5].destroy()
            options_values[i][0] = False
        Accordion._scrollbar._command("moveto", 0.0)
        Load_tools()

    # Reset Button
    reset_button = ctk.CTkButton(master=frameDecTool, text="Reset", font=ButtonsFont, width=60, height=41,
                                 text_color="#000",
                                 hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2", command=Reset)
    reset_button.place(x=940, y=160)

    # Accordian Frame
    Accordion = ctk.CTkScrollableFrame(master=frameDecTool, fg_color="white", bg_color="transparent",
                                       corner_radius=20, width=1340, height=400)
    Accordion.place(x=10, y=220)

    # Description of functionality
    label_description = ctk.CTkLabel(master=Accordion,
                                     text="IMPORTANT! Before downloading and starting the solution, read the how-to guide. Make sure you remove the malware from your system first, otherwise it will repeatedly lock your system or encrypt files. Any reliable antivirus solution can do this for you.",
                                     font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold"),
                                     wraplength=1000)
    label_description.pack(padx=10, pady=10)

    id = 0
    options_values = {}

    def add_option(option, Tool_name, guide_link, download_link, Tool_maker, wraplength=1000):

        nonlocal id

        option_frame = ctk.CTkFrame(master=Accordion)
        option_frame.pack(fill="x", expand=1, pady=20, padx=20)

        option_label = ctk.CTkLabel(option_frame, text=option, text_color="black", fg_color="white",
                                    bg_color="transparent", anchor="w", cursor="hand2")
        option_label.pack(side="left", anchor="w", expand=1, fill='both')
        option_label.bind("<Enter>", lambda event: option_label.configure(text_color="#7F8CD9"))
        option_label.bind("<Leave>", lambda event: option_label.configure(text_color="black"))

        Tool_name_label = ctk.CTkLabel(master=Accordion, text=Tool_name, fg_color="white", bg_color="transparent",
                                       wraplength=wraplength, justify="left")

        Tool_maker_label = ctk.CTkLabel(master=Accordion, text="  Made by " + Tool_maker, fg_color="white",
                                        bg_color="transparent",
                                        wraplength=wraplength, justify="left",
                                        image=ctk.CTkImage(light_image=Image.open(copyright_path),
                                                           size=(20, 20)), compound="left")

        Download_button = ctk.CTkButton(master=Accordion, text="Download",
                                        width=50, height=25,
                                        text_color="#000",
                                        hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2",
                                        command=lambda: open_link(download_link))

        guide_button = ctk.CTkButton(master=Accordion, text="How-to guide",
                                     width=50, height=25,
                                     text_color="#000",
                                     hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2",
                                     command=lambda: open_link(guide_link))

        x = id
        option_label.bind("<Button-1>", lambda event: open_close(event, x))

        options_values[id] = [False, option_frame, Tool_name_label, guide_button, Download_button, Tool_maker_label]

        id += 1

    def open_close(event, id_):
        if options_values[id_][0]:
            options_values[id_][0] = False
            options_values[id_][2].pack_forget()
            options_values[id_][3].pack_forget()
            options_values[id_][4].pack_forget()
            options_values[id_][5].pack_forget()
            return

        # remove all the options and values and show the value of option currently
        # clicked and then show the removed options again

        for key in options_values:
            if key != id_:
                if options_values[key][0]:
                    options_values[key][2].pack_forget()
                    options_values[key][3].pack_forget()
                    options_values[key][4].pack_forget()
                    options_values[key][5].pack_forget()
                    options_values[key][0] = False
                if key > id_:
                    options_values[key][1].pack_forget()

        options_values[id_][2].pack(anchor="w", expand=1, fill='x', pady=1)
        options_values[id_][3].pack(pady=2)
        options_values[id_][4].pack(pady=2)
        options_values[id_][5].pack(pady=1)
        options_values[id_][0] = True

        for key in range(id_ + 1, len(options_values)):
            options_values[key][1].pack(fill='x', expand=1, pady=20, padx=20)

    global old_id, new_id

    def Load_tools():
        global old_id, new_id
        query = f"SELECT Name, Description, Guide, Tool, made_by FROM tools where Id_tool between {old_id} and {new_id} ORDER BY Name"

        result = DB.fetchall(query)

        if result:
            print("Tools displayed !")
            for tool in result:
                old_id += 1
                new_id += 1
                add_option(option=tool[0], Tool_name=tool[1], guide_link=tool[2], download_link=tool[3],
                           Tool_maker=tool[4])
            button_load.pack_forget()
            button_load.pack(side=tk.BOTTOM, anchor=tk.S)
        else:
            print("Table tools is empty !")

    button_load = ctk.CTkButton(master=Accordion, width=100, height=50, font=ButtonsFont,
                                text="Load More", text_color="#000", fg_color="#B7EAF5",
                                bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                compound="top", cursor="hand2", command=Load_tools)
    Load_tools()
