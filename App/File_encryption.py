import datetime
import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk
from PIL import Image

import DBconnection as DB
import HomePage as hp
import encryption_functions as fe
import Session as ss

file_path = None
private_key = None
encrypted_content = None
buttonDownload = None

file_name = None


def File_encryption(root):
    def back_home():
        global file_path
        global private_key
        global encrypted_content
        global buttonDownload

        file_path = None
        private_key = None
        encrypted_content = None
        buttonDownload = None

        frameFichEnc.destroy()
        hp.HomePage(root)

    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")

    # Main Frame
    frameFichEnc = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameFichEnc.pack(fill=tk.BOTH, expand=True)

    # Navbar Frame
    NavBarFichEnc = ctk.CTkFrame(master=frameFichEnc, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarFichEnc.pack()

    label_logo_nav_df = ctk.CTkLabel(master=NavBarFichEnc, text="",
                                     image=ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38)))
    label_logo_nav_df.place(x=10, y=10)

    # "File decryption" Label and back button
    button_back = ctk.CTkButton(master=frameFichEnc, text="",
                                image=ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65)), hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=back_home)
    button_back.place(x=36, y=70)

    label_df = ctk.CTkLabel(master=frameFichEnc, text="File Encryption",
                            font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_df.place(x=150, y=88)

    # ******************* les fonctions ************************

    # la fonction qui permet de permettre a l'utilisateur de disposer un fichier
    def load_file():
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            name = os.path.basename(file_path)
            buttonEncrypt.configure(state=tk.NORMAL)
            messagebox.showinfo("load file", f"File {name} Loaded !")

    # fonction qui permet d'afficher les tailles des clés selon l'algorithme choisit
    def printALgo(value):
        if value == "AES":
            keySizeCombox.set(" ")
            keySizeCombox.configure(values=["128", "192", "256"])
        elif value == "RSA":
            keySizeCombox.set(" ")
            keySizeCombox.configure(values=["1024", "2048", "4096"])

    # la fonction qui permet de crypter un fichier celon l'algorithme choisit
    def encrypt_file():
        global file_path
        global private_key
        global encrypted_content

        # afficher un message d'erreur s'il n y a pas de fichier ou algorithme choisi
        if file_path is None:
            messagebox.showerror("Error", "Please select a file and choose an encryption algorithm.")
            return
        if crypteCombox.get() == " " or keySizeCombox.get() == " ":
            messagebox.showerror("Error", "Please select an encryption algorithm and a key size.")
            return

        file_name = os.path.basename(file_path)
        size_key = keySizeCombox.get()
        algorithm = crypteCombox.get()
        # if encrypted_content is None:
        # sinon ouvrir le fichier pour le crypter
        # with open(file_path, 'rb') as file:
        # file_content = file.read()

        # Crypter le contenu du fichier avec l'algorithme choisi
        if algorithm == "AES":
            encrypted_content, private_key = fe.encrypt_file_aes(file_path, int(size_key))
            timedecryptage = time.time()
            # Convertir le timestamp en objet datetime
            date_reparation = datetime.datetime.fromtimestamp(timedecryptage).date()
            print(ss.current_user)
            insert_query = f"INSERT INTO Fichiers_crypte (Date_importation, CLE, NAME, id_user) " \
                           f"VALUES (TO_DATE('{date_reparation}', 'YYYY-MM-DD'), '{str(private_key.hex())}', 'crypt_{file_name}','{ss.current_user}')"
            if DB.execute_query(insert_query):
                print("Fichier ajouté")
            else:
                print("Fichier existant dans la table")
        elif algorithm == "RSA":
            encrypted_content, private_key = fe.encrypt_fileRSA(file_path, int(size_key))
            private_key = fe.encrypt_fileRSA(file_path, int(size_key))[0]
            print(private_key)
            timedecryptage = time.time()
            # Convertir le timestamp en objet datetime
            date_reparation = datetime.datetime.fromtimestamp(timedecryptage).date()
            insert_query = f"INSERT INTO Fichiers_crypte (Date_importation, CLE, NAME, id_user) " \
                           f"VALUES (TO_DATE('{date_reparation}', 'YYYY-MM-DD'), '{str(private_key.hex())}', 'crypt_{file_name}','{ss.current_user}')"
            if DB.execute_query(insert_query):
                print("Fichier ajouté")
            else:
                print("Fichier existant dans la table")

        messagebox.showinfo("Encrypt file", "File Encrypted successfully !")
        buttonDownload.configure(state=tk.NORMAL)
        # return file_content

    def download_encrypted_file():
        global encrypted_content
        global file_path
        # selected_algorithm = crypteCombox.get()

        global buttonDownload
        file_name = os.path.basename(file_path)
        if encrypted_content:
            # Demander à l'utilisateur où enregistrer le fichier crypté
            download_path = filedialog.asksaveasfilename(initialfile=f"{file_name}_encrypted.enc",
                                                         filetypes=[("Encrypted Files", "*.pem ")])
            if download_path:
                # Copier le contenu crypté vers le nouvel emplacement
                with open(download_path, 'wb') as download_file:
                    download_file.write(encrypted_content)

    # *******************************************************************
    image_path = os.path.join(os.path.dirname(__file__), "images", "logo", "crypte2.jpg")
    addFolder_path = os.path.join(os.path.dirname(__file__), "images", "logo", "addFolder.png")
    encrypte_path = os.path.join(os.path.dirname(__file__), "images", "logo", "encrypte3.png")
    download_path = os.path.join(os.path.dirname(__file__), "images", "logo", "download.png")
    image_label = ctk.CTkLabel(frameFichEnc,
                               image=ctk.CTkImage(light_image=Image.open(image_path), size=(690, 660)),
                               text='')
    image_label.place(x=0, y=140)
    addFolder = ctk.CTkImage(Image.open(addFolder_path), size=(35, 35))
    encrypte = ctk.CTkImage(Image.open(encrypte_path), size=(35, 35))
    download = ctk.CTkImage(Image.open(download_path), size=(35, 35))

    labelFile = ctk.CTkLabel(master=frameFichEnc, text="Please enter your file here : ", width=150, height=30,
                             corner_radius=8,
                             text_color="#2628a4",
                             font=('Arial', 25),
                             )
    labelFile.place(relx=0.65, rely=0.26, anchor=tk.W)

    labelAlgorithme = ctk.CTkLabel(master=frameFichEnc, text="Choose the encryption algorithm :", width=150, height=30,
                                   corner_radius=8,
                                   text_color="#2628a4",
                                   font=('Arial', 25), )
    labelAlgorithme.place(relx=0.6, rely=0.43, anchor=tk.W)
    labelAlgorithme = ctk.CTkLabel(master=frameFichEnc, text="Choose the size of the key :", width=150, height=30,
                                   corner_radius=8,
                                   text_color="#2628a4",
                                   font=('Arial', 25), )
    labelAlgorithme.place(relx=0.64, rely=0.59, anchor=tk.W)

    buttonLoad = ctk.CTkButton(master=frameFichEnc, text="load file   ", command=load_file,
                               image=addFolder,
                               corner_radius=8,
                               width=200,
                               height=20,
                               compound="right",
                               anchor="e",
                               font=("Arial", 20),
                               border_spacing=10,
                               fg_color="#7F8CD9",
                               hover_color="#2628a4")
    buttonLoad.place(relx=0.68, rely=0.33, anchor=tk.W)

    crypteCombox = ctk.CTkComboBox(master=frameFichEnc,
                                   values=["RSA", "AES"],
                                   command=printALgo,
                                   dropdown_hover_color="#e4ab7c",
                                   dropdown_fg_color="#b1d9da",
                                   width=200,
                                   height=40,
                                   fg_color="#b1d9da",
                                   corner_radius=8,
                                   font=("Arial", 20),
                                   state="readonly"
                                   )
    crypteCombox.place(relx=0.68, rely=0.51, anchor=tk.W)
    crypteCombox.set(" ")

    keySizeCombox = ctk.CTkComboBox(master=frameFichEnc,
                                    values=[" "],
                                    command=printALgo,
                                    dropdown_hover_color="#e4ab7c",
                                    dropdown_fg_color="#b1d9da",
                                    width=200,
                                    height=40,
                                    fg_color="#b1d9da",
                                    corner_radius=8,
                                    font=("Arial", 20),
                                    state="readonly")
    keySizeCombox.place(relx=0.68, rely=0.68, anchor=tk.W)
    crypteCombox.set(" ")

    buttonEncrypt = ctk.CTkButton(master=frameFichEnc, text="Encrypt   ", command=encrypt_file,
                                  image=encrypte,
                                  state=tk.DISABLED,
                                  corner_radius=8,
                                  width=200,
                                  height=20,
                                  compound="right",
                                  anchor="e",
                                  font=("Arial", 20),
                                  border_spacing=10,
                                  fg_color="#7F8CD9",
                                  hover_color="#2628a4",
                                  cursor="hand2"
                                  )
    buttonEncrypt.place(relx=0.68, rely=0.81, anchor=tk.W)

    buttonDownload = ctk.CTkButton(master=frameFichEnc, text="Download  ",
                                   state=tk.DISABLED,
                                   command=download_encrypted_file,
                                   image=download,
                                   corner_radius=8,
                                   width=200,
                                   height=30,
                                   compound="right",
                                   anchor="e",
                                   font=("Arial", 20),
                                   border_spacing=10,
                                   fg_color="#7F8CD9",
                                   hover_color="#2628a4",
                                   cursor="hand2"
                                   )
    buttonDownload.place(relx=0.68, rely=0.92, anchor=tk.W)

    # Logout after no activity
    # frameFichEnc.bind("<Button-1>", lambda event: ss.on_user_interaction(root, frameFichEnc))
