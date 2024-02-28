import os
import tkinter as tk
import customtkinter as ctk
import Repaired_files as rf
import Session as ss
import DBconnection as DB

from PIL import Image
from tkinter import ttk, messagebox


def StockDecryptFiles(root):
    def back(frame):
        frame.destroy()
        rf.Repaired_files(root)

    def copy_key(event):
        # Get the selected item
        selected_item = table_rf.focus()
        if selected_item:
            # Retrieve the decryption key from the selected item
            decryption_key = table_rf.item(selected_item, "values")[2]
            # Copy the decryption key to clipboard
            root.clipboard_clear()
            root.clipboard_append(decryption_key)
            root.update()  # Manually update clipboard
            messagebox.showinfo("Copied", "Decryption key has been copied to clipboard.")

    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    image_back = ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65))
    logo_nav = ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38))

    # Main frame Home Page
    frameStockDF = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameStockDF.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBar = ctk.CTkFrame(master=frameStockDF, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBar.pack()

    label_logo_nav = ctk.CTkLabel(master=NavBar, text="", image=logo_nav)
    label_logo_nav.place(x=10, y=10)

    # Label and back button
    button_back = ctk.CTkButton(master=frameStockDF, text="", image=image_back, hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: back(frameStockDF))
    button_back.place(x=36, y=70)

    # Inform User about how he can have the key
    info_path = os.path.join(os.path.dirname(__file__), "images", "logo", "info.png")
    image_info = ctk.CTkImage(light_image=Image.open(info_path), size=(30, 30))
    image_label_info = ctk.CTkLabel(frameStockDF, image=image_info, text='')
    image_label_info.place(x=1065, y=100)
    label_download_key = ctk.CTkLabel(master=frameStockDF,
                                      text="Double click to download the key",
                                      font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=12, weight="bold"))
    label_download_key.place(x=1100, y=100)

    # Description of functionality
    label_df = ctk.CTkLabel(master=frameStockDF,
                            text=".......................................",
                            font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19, weight="bold"))
    label_df.place(x=320, y=230)

    # TreeView for repaired files

    frame_tv = ctk.CTkFrame(frameStockDF, fg_color='#DAE5F4', width=1300, height=500)
    frame_tv.place(x=50, y=150)
    table_rf = ttk.Treeview(master=frame_tv, height=25)
    # Define columns
    table_rf["columns"] = ("Filename", "Reparation date", "Decryption key")

    # Format columns
    table_rf.column("#0", width=0, stretch=tk.NO)  # Hide the default column
    table_rf.column("Filename", anchor=tk.CENTER, width=585)
    table_rf.column("Reparation date", anchor=tk.CENTER, width=350)
    table_rf.column("Decryption key", anchor=tk.CENTER, width=585)

    # Create headings
    table_rf.heading("#0", text="", anchor=tk.W)
    table_rf.heading("Filename", text="Filename", anchor=tk.CENTER)
    table_rf.heading("Reparation date", text="Reparation date", anchor=tk.CENTER)
    table_rf.heading("Decryption key", text="Decryption key", anchor=tk.CENTER)

    def add_row():
        pass

    query = f"Select * from Fichiers_Rep where id_user='{ss.current_user}'"
    result = DB.fetchall(query)

    if result:
        data = []
        for row in result:
            file_name = row[2]
            date_reparation = row[1].strftime("%d/%m/%Y")
            Cle = row[3]
            print(data)
            data.append((file_name, date_reparation, Cle))
        print(data)
        for item_id, item in enumerate(data, start=1):
            table_rf.insert("", tk.END, iid=item_id, values=item)
    else:
        print("result null")

    # Bind the TreeviewSelect event to the copy_key function
    table_rf.bind("<Double-1>", copy_key)

    # Place the Treeview inside the ctk.CTkFrame
    table_rf.place(x=50, y=60)

    # Logout after no activity
    frameStockDF.bind("<Button-1>", lambda event: ss.on_user_interaction(root, frameStockDF))
