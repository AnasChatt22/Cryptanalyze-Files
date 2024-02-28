import os
import struct
import time
import tkinter as tk
from tkinter import filedialog, ttk, WORD, messagebox
import matplotlib.pyplot as plt
import customtkinter as ctk
import faker as fk
import pandas as pd
from PIL import Image
from gmpy2 import gmpy2
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import Settings as st
from labo_implementation import fonctions


import os
import struct
import time
import tkinter as tk
from tkinter import filedialog, ttk, WORD, messagebox

import customtkinter as ctk
import faker as fk
import pandas as pd
from PIL import Image
from gmpy2 import gmpy2

import Settings as st
from labo_implementation import fonctions

image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
icon_path = os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico")

def Implementation_lab(root):
    # Fonts
    labelFont = ctk.CTkFont("Microsoft YaHei UI Light", 14)
    laboLabel = ctk.CTkFont("Microsoft YaHei UI Light", 16, weight="bold")
    ButtonsFont = ctk.CTkFont("Microsoft YaHei UI Light", size=14, weight="bold")

    # images

    image_back = ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65))
    logo_nav = ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38))

    # generate randon firstname and lastname
    fake1 = fk.Faker()
    # Generate a random first name
    random_first_name1 = fake1.first_name_male()
    # Generate a random last name
    random_last_name1 = fake1.last_name()

    fake2 = fk.Faker()
    # Generate a random first name
    random_first_name2 = fake2.first_name_male()
    # Generate a random last name
    random_last_name2 = fake2.last_name()

    # Main Frame for "Implementation Lab" Page
    frameLabo = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameLabo.pack(fill=tk.BOTH, expand=True)

    # Variables
    message_var = ctk.StringVar(master=frameLabo)  # First Step
    taille_var = ctk.StringVar(master=frameLabo)  # Second Step
    attaque_var = ctk.StringVar(master=frameLabo)  # third Step

    # Navbar Frame
    NavBarLabo = ctk.CTkFrame(master=frameLabo, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarLabo.pack()

    label_logo_nav_df = ctk.CTkLabel(master=NavBarLabo, text="", image=logo_nav)
    label_logo_nav_df.place(x=10, y=10)

    # "Implementation Lab" Label and back button
    button_back = ctk.CTkButton(master=frameLabo, text="", image=image_back, hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=lambda: st.back(root, frameLabo))
    button_back.place(x=36, y=70)

    label_df = ctk.CTkLabel(master=frameLabo, text="Implementation Lab",
                            font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_df.place(x=150, y=88)

    # Expediteur et Destinataire
    img_exp_path = os.path.join(os.path.dirname(__file__), "images", "logo", "person.jpeg")
    img_des_path = os.path.join(os.path.dirname(__file__), "images", "logo", "person2.jpeg")

    img_exp_label = ctk.CTkLabel(master=frameLabo, text="",
                                 image=ctk.CTkImage(light_image=Image.open(img_exp_path), size=(88, 96)))
    img_exp_label.place(x=150, y=160)
    exp_label = ctk.CTkLabel(master=frameLabo, text=f"{random_first_name1} {random_last_name1}", font=labelFont)
    exp_label.place(x=150, y=260)

    img_des_label = ctk.CTkLabel(master=frameLabo, text="",
                                 image=ctk.CTkImage(light_image=Image.open(img_des_path), size=(88, 96)))
    img_des_label.place(x=1090, y=160)
    des_label = ctk.CTkLabel(master=frameLabo, text=f"{random_first_name2} {random_last_name2}", font=labelFont)
    des_label.place(x=1090, y=260)

    # taille Label
    taille_label = ctk.CTkLabel(master=frameLabo, text="Taille (bits):", font=laboLabel)
    taille_label.place(x=650, y=150)

    # Select taille
    def taille_selection(choice):
        taille_var.set(choice)

    taille_select = ctk.CTkComboBox(master=frameLabo, values=["16", "64", "128", "256", "512", "1024", "2048"],
                                    state="readonly", variable=taille_var, command=taille_selection)
    taille_select.place(x=632, y=200)

    # Génération de cryptosystème RSA Button
    # taille = taille_var , message = message_var , command=lambda: generatab(taille.get(), dataFrame, message.get())
    def generatecryptosys():

        start_time_gk = time.perf_counter()
        result = fonctions.generate_Key(int(taille_var.get()))
        end_time_gk = time.perf_counter()
        temp_de_gk = end_time_gk - start_time_gk

        # Convertir le message en octets à l'aide de struct.pack
        # convertit le message en octets qui ont une longueur fixe et qui représentent exactement les octets du message
        start_time_cryptage = time.perf_counter()
        message_bytes = struct.pack('!{}s'.format(len(message_var.get())), message_var.get().encode())

        # Convertir chaque octet en son code ASCII
        asc = [str(b) for b in message_bytes]

        # Remplir chaque code ASCII avec des zéros en tête pour les rendre tous longs de 3 chiffres
        for i, k in enumerate(asc):
            if len(k) < 3:
                while len(k) < 3:
                    k = '0' + k
                asc[i] = k
        asc = ''.join(asc)
        d, f = 0, 3
        while len(asc) % f != 0:
            asc = asc + '0'
        h = []
        while f <= len(asc):
            h.append(asc[d:f])
            d, f = f, f + 3
        crypt = []
        for i in h:
            num = int(i)
            a = gmpy2.powmod(num, result[3], result[2])
            crypt.append(str(a))
        end_time_cryptage = time.perf_counter()
        temp_de_cryptage = end_time_cryptage - start_time_cryptage
        print(crypt)

        start_time_decryptage = time.perf_counter()

        # Déchiffrement des blocs
        decrypt = [str(gmpy2.powmod(int(i), result[4], result[2])) for i in crypt]
        for i, s in enumerate(decrypt):
            if len(s) < 3:
                while len(s) < 3:
                    s = '0' + s
                decrypt[i] = s
        # Convertir les codes ASCII déchiffrés en octets à l'aide de struct.pack
        decrypted_bytes = struct.pack('!{}s'.format(len(decrypt)), bytes([int(s) for s in decrypt]))
        asci2 = decrypted_bytes.decode()
        end_time_decryptage = time.perf_counter()
        temp_de_decryptage = end_time_decryptage - start_time_decryptage

        # afficher les information de cle et de cryptage dans une fenetre :

        results = ({'temp_de_gk': str(temp_de_gk), 'temp_de_cryptage': str(temp_de_cryptage),
                    'temp_de_decryptage': str(temp_de_decryptage)})
        df = pd.DataFrame(results, index=[0])
        df_rows = df.to_numpy().tolist()
        # Insert rows in treeView
        for row in df_rows:
            table_rsa.insert("", "end", values=row)

        inf_window = tk.Toplevel()
        inf_window.title("Table")
        inf_window.geometry("1400x850")
        inf_window.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico"))
        text_gener_rsa = ctk.CTkTextbox(inf_window, height=600, width=1000)
        label_gener_rsa = ctk.CTkLabel(inf_window, text="information sur le cryptosystème")
        label_gener_rsa.configure(font=("Courier", 14))
        label_gener_rsa.pack()
        Fact = ('p:' + str(result[0]) + " \n" + " \n" + 'q:' + str(result[1]) + " \n" + " \n" + 'n:' + str(
            result[2]) + " \n" + " \n" + 'e:' + str(result[3]) + " \n" + " \n" + 'd:' + str(
            result[4]) + " \n" + " \n" + '\u03C6:' + str(result[5]) + " \n" + " \n" + "Message chiffré : \n" + str(
            crypt) + "\n" + " \n" + "message dechiffrer :\n " + str(asci2))

        text_gener_rsa.insert(tk.END, Fact)
        text_gener_rsa.place(x=30, y=60)

    gene_crypt_RSA_btn = ctk.CTkButton(master=frameLabo, text="Génération de cryptosystème RSA", width=300,
                                       cursor="hand2", command=generatecryptosys)
    gene_crypt_RSA_btn.place(x=550, y=240)

    def reset_inputs():
        taille_var.set("")
        attaque_var.set("")
        button_send.configure(state=tk.DISABLED, cursor="arrow")
        message_arrived.configure(state=tk.DISABLED, cursor="arrow", fg_color="#c2d6d6")
        n_label.place_forget()
        n_entry.place_forget()
        e_label.place_forget()
        e_entry.place_forget()
        c_label.place_forget()
        c_entry.place_forget()
        fi_label.place_forget()
        fi_entry.place_forget()
        cryptanalyse_button.place_forget()
        button_import.place(x=140, y=370)
        file_name_label.place_forget()

    def afficher_utilisation_ressources():
        # Créer une fenêtre Tkinter
        fenetre = tk.Tk()
        fenetre.geometry("1200x400")
        fenetre.title("Utilisation des ressources")
        fenetre.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico"))

        # Créer des figures pour chaque type de ressource
        fig_cpu = plt.figure(figsize=(5, 3))
        fig_ram = plt.figure(figsize=(5, 3))

        # Ajouter des sous-graphiques aux figures
        ax_cpu = fig_cpu.add_subplot(111)
        ax_ram = fig_ram.add_subplot(111)

        # Définir les titres des graphiques
        fig_cpu.suptitle("Utilisation du CPU", fontsize=16)
        fig_ram.suptitle("Utilisation de la RAM", fontsize=16)

        # Définir les labels des axes
        ax_cpu.set_xlabel("Temps (s)", fontsize=12)
        ax_cpu.set_ylabel("Pourcentage (%)", fontsize=12)
        ax_ram.set_xlabel("Temps (s)", fontsize=12)
        ax_ram.set_ylabel("Pourcentage (%)", fontsize=12)

        # Créer des variables pour stocker les données
        cpu_utilisations = []
        ram_utilisations = []

        # Définir la fonction de mise à jour des graphiques
        def update_graphiques():
            # Récupérer les données d'utilisation des ressources
            cpu_utilisation = psutil.cpu_percent()
            ram_utilisation = psutil.virtual_memory().percent

            # Stocker les données
            cpu_utilisations.append(cpu_utilisation)
            ram_utilisations.append(ram_utilisation)

            # Mettre à jour les données des graphiques
            ax_cpu.plot(cpu_utilisations, 'b-', label='CPU')
            ax_ram.plot(ram_utilisations, 'r-', label='RAM')

            # Redessiner les figures
            fig_cpu.canvas.draw()
            fig_ram.canvas.draw()

            # Mettre à jour la fenêtre après 1 seconde
            fenetre.after(100, update_graphiques)

        # Créer des canevas pour afficher les graphiques dans la fenêtre Tkinter
        canvas_cpu = FigureCanvasTkAgg(fig_cpu, master=fenetre)
        canvas_cpu.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10)
        canvas_ram = FigureCanvasTkAgg(fig_ram, master=fenetre)
        canvas_ram.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10)

        # Démarrer la mise à jour des graphiques
        update_graphiques()

        # Afficher la fenêtre
        fenetre.mainloop()

    def check_ram_usage_threshold(threshold_percent):
        # Obtenir l'utilisation actuelle de la mémoire
        ram_percent = psutil.virtual_memory().percent

        # Vérifier si l'utilisation de la mémoire dépasse le seuil spécifié
        if ram_percent >= threshold_percent:
            messagebox.showinfo(title="Alerte", message="Les ressources matérielles utilisées sont insuffisantes.")

        else:
            messagebox.showinfo(title="Alerte", message="Les ressources matérielles utilisées sont suffisantes.")
            afficher_utilisation_ressources()

    def checked():
        check_ram_usage_threshold(87)

        # vider les cases Button

    vider_cases_btn = ctk.CTkButton(master=frameLabo, text="vider les cases", cursor="hand2", command=reset_inputs)
    vider_cases_btn.place(x=630, y=280)

    # changer les roles Button
    '''vider_cases_btn = ctk.CTkButton(master=frameLabo, text="changer les roles", cursor="hand2")
    vider_cases_btn.place(x=710, y=280)'''

    # Les attaques label
    attaque_label = ctk.CTkLabel(master=frameLabo, text="Les attaques :", font=laboLabel)
    attaque_label.place(x=640, y=320)
    button_resources = ctk.CTkButton(master=frameLabo,
                                     text="afficher Ressources", command=afficher_utilisation_ressources)
    button_resources.place(x=500, y=88)
    button_checked = ctk.CTkButton(master=frameLabo,
                                   text="Check Ressources", command=checked)
    button_checked.place(x=650, y=88)

    # Define variables and
    e_publique = ctk.IntVar()
    cryptogramme = ctk.StringVar()
    n_publique = ctk.IntVar()
    fi_publique =ctk.IntVar()

    def validate_integer(value):
        if value == "":
            return True  # Allow empty string
        try:
            int(value)
            return True  # Validation successful
        except ValueError:
            return False  # Validation failed




    def factorisation():
        for widget in frameLabo.winfo_children():
            if isinstance(widget, ctk.CTkProgressBar):
                widget.destroy()
        # n = n_publique_val / cypher.get() = cryptogramme_val
        e_publique_val = e_publique.get()
        n_publique_val = n_publique.get()
        cryptogramme_val = cryptogramme.get()
        if e_publique_val and n_publique_val and cryptogramme_val:
            # code existant pour la factorisation

            start_time = time.time()

            p_crack, q_crack = fonctions.factorize(int(n_publique_val))
            end_time = time.time()
            if p_crack is not None and q_crack is not None:

                temp = end_time - start_time
                fact_window = tk.Toplevel()
                fact_window.title("Table")
                fact_window.geometry("1000x600")
                fact_window.resizable(False, False)
                fact_window.iconbitmap(icon_path)
                fact_text = ctk.CTkTextbox(fact_window, height=600, width=700)
                fact_label = ctk.CTkLabel(fact_window, text="information sur la factorisation")
                fact_label.configure(font=("Courier", 14))
                fact_label.pack()
                Fact = (
                    'Clé privée trouvée :\n\nn: {}\n\np: {}\n\nq: {}\n\nTemps total de factorisation : {} secondes'.format(
                        n_publique_val,
                        p_crack,
                        q_crack,
                        temp))
                b2 = ctk.CTkButton(fact_window, text="Exit", corner_radius=20, command=fact_window.destroy)
                b2.place(x=32, y=25)
                fact_text.insert(tk.END, Fact)
                fact_text.place(x=30, y=60)
                print('calculer d ')
                d = fonctions.findModInverse(int(e_publique.get()), (p_crack - 1) * (q_crack - 1))
                n=p_crack*q_crack
                # Split and process the cryptogramme values
                cryptogramme_values = cryptogramme_val.strip('[]').split(',')

                decrypt = []
                for i in cryptogramme_values:
                    try:
                        # Attempt to convert each value to an integer
                        decrypted_value = gmpy2.powmod(int(i.strip().strip("'")), d, n)
                        decrypt.append(str(decrypted_value))
                    except ValueError:
                        print(f"Skipping invalid value: {i.strip().strip('')}")

                for i, s in enumerate(decrypt):
                    if len(s) < 3:
                        while len(s) < 3:
                            s = '0' + s
                        decrypt[i] = s
                # Convertir les codes ASCII déchiffrés en octets à l'aide de struct.pack
                decrypted_bytes = struct.pack('!{}s'.format(
                    len(decrypt)), bytes([int(s) for s in decrypt]))
                asci2 = decrypted_bytes.decode()
                # Afficher le résultat dans une boîte de dialogue
                messagebox.showinfo("Résultat du déchiffrement", "Le message déchiffré est:\n{}".format(asci2))
                root.mainloop()
                for widget in frameLabo.winfo_children():
                    if isinstance(widget, ctk.CTkProgressBar):
                        widget.destroy()
            else:
                messagebox.showinfo("La cryptanalyse a échoué.",
                                    "Veuillez réessayer avec un autre algorithme de factorisation.")
        else:
            messagebox.showwarning("Error", "All fields must be filled")


    def connaissant_phi():
        for widget in frameLabo.winfo_children():
            if isinstance(widget, ctk.CTkProgressBar):
                widget.destroy()
        # Get the values from the GUI elements
        n_publique_val = n_publique.get()
        e_publique_val = e_publique.get()
        fi_publique_val = fi_publique.get()
        cryptogramme_val = cryptogramme.get()

        # Check if all necessary values are provided
        if n_publique_val and e_publique_val and fi_publique_val:

            # Implement your logic for the "connaissant_phi" attack here

            # Example: Perform some calculations using the provided values
            d = fonctions.findModInverse(int(e_publique_val), int(fi_publique_val))
            # Split and process the cryptogramme values
            cryptogramme_values = cryptogramme_val.strip('[]').split(',')

            decrypt = []
            for i in cryptogramme_values:
                try:
                    # Attempt to convert each value to an integer
                    decrypted_value = gmpy2.powmod(int(i.strip().strip("'")), d, n_publique_val)
                    decrypt.append(str(decrypted_value))
                except ValueError:
                    print(f"Skipping invalid value: {i.strip().strip('')}")

            for i, s in enumerate(decrypt):
                if len(s) < 3:
                    while len(s) < 3:
                        s = '0' + s
                    decrypt[i] = s
            # Convertir les codes ASCII déchiffrés en octets à l'aide de struct.pack
            decrypted_bytes = struct.pack('!{}s'.format(
                len(decrypt)), bytes([int(s) for s in decrypt]))
            asci2 = decrypted_bytes.decode()
            # Afficher le résultat dans une boîte de dialogue
            messagebox.showinfo("Résultat du déchiffrement", "Le message déchiffré est:\n{}".format(asci2))
            root.mainloop()

        else:
            messagebox.showwarning("Error", "All fields must be filled")

    def on_button_click():

        selected_attack = attaque_var.get()
        # Créer une barre de progression
        progress_bar = ctk.CTkProgressBar(master=frameLabo, mode='indeterminate')
        progress_bar.place(x=630, y=130)
        progress_bar.start()
        if selected_attack == "Factorisation":
            frameLabo.after(40000, lambda: factorisation())

        elif selected_attack == "connaissant φ(N)":
            frameLabo.after(6000, lambda: connaissant_phi())



    n_label = ctk.CTkLabel(master=frameLabo, text='Clé publique (n):', font=('cursive', 10))
    n_entry = ctk.CTkEntry(master=frameLabo, textvariable=n_publique, validate="key",
                           validatecommand=(frameLabo.register(validate_integer), "%P"))

    e_label = ctk.CTkLabel(master=frameLabo, text="Clé publique (e):", font=('cursive', 10))
    e_entry = ctk.CTkEntry(master=frameLabo, textvariable=e_publique, validate="key",
                           validatecommand=(frameLabo.register(validate_integer), "%P"))
    fi_label = ctk.CTkLabel(master=frameLabo, text="φ(N):", font=('cursive', 10))
    fi_entry = ctk.CTkEntry(master=frameLabo, textvariable=fi_publique)

    c_label = ctk.CTkLabel(master=frameLabo, text="Cryptogramme:", font=('cursive', 10))
    c_entry = ctk.CTkEntry(master=frameLabo, textvariable=cryptogramme)

    cryptanalyse_button = ctk.CTkButton(master=frameLabo, text='cryptanalyser', command=on_button_click)

    # Select attaque ComboBox
    def show_choice(choice):
        try:
            attaque_var.set(choice)
            if choice == " ":
                n_label.place_forget()
                n_entry.place_forget()
                e_label.place_forget()
                e_entry.place_forget()
                c_label.place_forget()
                c_entry.place_forget()
                fi_label.place_forget()
                fi_entry.place_forget()
                cryptanalyse_button.place_forget()
            elif choice == "connaissant φ(N)":
                n_label.place(x=800, y=310)
                n_entry.place(x=800, y=330)
                e_label.place(x=800, y=350)
                e_entry.place(x=800, y=370)
                c_label.place(x=800, y=390)
                c_entry.place(x=800, y=410)
                fi_label.place(x=800, y=430)
                fi_entry.place(x=800, y=450)
                cryptanalyse_button.place(x=965, y=445)
            elif choice == "Factorisation":
                n_label.place(x=800, y=310)
                n_entry.place(x=800, y=335)
                e_label.place(x=800, y=365)
                e_entry.place(x=800, y=390)
                c_label.place(x=800, y=420)
                c_entry.place(x=800, y=445)
                fi_label.place_forget()
                fi_entry.place_forget()
                cryptanalyse_button.place(x=965, y=445)



        except Exception as ex:
            print(f"Error show_choice : {ex}")

    attaque_select = ctk.CTkComboBox(master=frameLabo, values=[" ", "Factorisation","connaissant φ(N)","Hastad ","Wiener","Pollard"], state="readonly",
                                     command=show_choice, variable=attaque_var)
    attaque_select.place(x=632, y=370)






    # Message Label (First step)
    message = ctk.CTkLabel(master=frameLabo, text="Message:", font=laboLabel)
    message.place(x=140, y=330)
    file_name_label = ctk.CTkLabel(frameLabo, font=laboLabel,
                                   anchor="center",
                                   bg_color="transparent", fg_color="#0088cc", text_color="white",
                                   corner_radius=20)

    def open_file():
        try:
            file_path = filedialog.askopenfilename(title="Choose a .txt file", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                message_var.set(file_content)
                # Hide the button
                button_import.place_forget()
                # configure button_send
                button_send.configure(state='normal', cursor='hand2')
                # Get the file name from the full path
                file_name = os.path.basename(file_path)
                # Create and place a label with the file name
                file_name_label.configure(text=f"Selected File: {file_name}")
                file_name_label.place(x=140, y=370)

        except Exception as ex:
            print(f"Error open_file : {ex}")

    button_import = ctk.CTkButton(master=frameLabo, font=ButtonsFont, width=150, height=35,
                                  text="Select file", text_color="#fff", corner_radius=20,
                                  compound="top", cursor="hand2",
                                  command=open_file)
    button_import.place(x=140, y=370)

    # message arrived
    message_arrived = ctk.CTkButton(master=frameLabo, text="message arrived!", state="disabled",
                                    fg_color="#c2d6d6", command=lambda: show_message(message_var))
    message_arrived.place(x=1070, y=300)

    # send button
    button_send = ctk.CTkButton(master=frameLabo, font=ButtonsFont, width=100, height=20,
                                text="Send message", text_color="#fff", corner_radius=20,
                                compound="top", state="disabled", command=lambda: message_send(message_arrived))
    button_send.place(x=150, y=420)

    temps_gene_cryp = ctk.CTkLabel(master=frameLabo, text="Temps de Génération des cryptosystème RSA", font=laboLabel,
                                   fg_color='#fff', text_color='black', width=1400)
    temps_gene_cryp.place(x=0, y=475)

    # Temps RSA Treeview (Table)
    fr3 = ctk.CTkFrame(frameLabo, bg_color='#D5F5E3', width=1400)
    fr3.pack(side="bottom", fill="both")
    table_rsa = ttk.Treeview(master=fr3, columns=('temp_de_gk', 'temp_de_cryptage', 'temp_de_decryptage'),
                             show='headings')
    # Scroll bars
    scrollx = ttk.Scrollbar(fr3, orient='horizontal')
    scrolly = ttk.Scrollbar(fr3, orient='vertical')
    scrollx.pack(side='bottom', fill='x')
    scrolly.pack(side='left', fill='y')

    table_rsa.pack(side='bottom', fill='both', expand=True)
    scrollx.config(command=table_rsa.xview)
    scrolly.config(command=table_rsa.yview)

    table_rsa.heading('temp_de_gk', text='temp_de_gk', anchor='center')
    table_rsa.heading('temp_de_cryptage', text='temp_de_cryptage', anchor='center')
    table_rsa.heading('temp_de_decryptage', text='temp_de_decryptage', anchor='center')

    # Center the text in each column
    for col in table_rsa['columns']:
        table_rsa.column(col, anchor='center')


def show_message(message_var):
    try:
        message = message_var.get()

        # Create a new window to display the message
        message_window = tk.Toplevel()
        message_window.title("Message")
        message_window.geometry("1700x700")
        message_window.iconbitmap(icon_path)
        message_window.resizable(False, False)

        # Create a Text widget for displaying the message
        message_text = ctk.CTkTextbox(message_window, wrap=WORD, height=20, width=80)
        message_text.pack(padx=20, pady=20, fill="both", expand=True)

        # Insert the message content into the Text widget
        message_text.insert("1.0", message)
    except Exception as ex:
        print(f"Error show_message : {ex}")


def message_send(message_arrived):
    try:
        messagebox.showinfo("Message Sent", "Your message has been sent successfully!")
        message_arrived.configure(state="normal", fg_color="#5c5cd6", text_color="white")
    except Exception as ex:
        print(f"Error message_send : {ex}")
