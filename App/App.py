import os
from ctypes import windll
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import SignIn as si

windll.shcore.SetProcessDpiAwareness(1)

app_width = 1400
app_height = 700
x = 80
y = 80
logo_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
icon_path = os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico")

# Create a splash screen window
splash_root = ctk.CTk()
splash_root.geometry(f"600x250+580+400")
splash_root.wm_overrideredirect(True)
splash_root.configure(fg_color="black")
splash_label = ctk.CTkLabel(master=splash_root, text=" ",
                            image=ctk.CTkImage(light_image=Image.open(logo_path), size=(569, 116)))
splash_label.pack(expand=True)


def close_splash():
    if DB.toConnect():
        splash_root.destroy()  # Close the splash screen
        # Now create the main app window
        root = ctk.CTk()
        root.title("FileCipher")
        root.iconbitmap(icon_path)
        root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        root.resizable(False, False)

        def on_close():
            # Disconnect from the database when the application is closed
            DB.disconnect()
            root.destroy()

        si.SignIn(root)
        root.protocol("WM_DELETE_WINDOW", on_close)
        root.mainloop()
    else:
        splash_root.destroy()  # Close the splash screen
        messagebox.showerror("Connection error", "No connection to database")


# Schedule the splash screen to close after 3 seconds (3000 milliseconds)
splash_root.after(1000, close_splash)
print(logo_path)
# Display the splash screen
splash_root.mainloop()
