import datetime
import hashlib
import os
import socket
import time
import tkinter as tk
from collections import Counter
from tkinter import filedialog, messagebox

import customtkinter as ctk
import matplotlib.pyplot as plt
import psutil
import requests
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import ALG
import DBconnection as DB
import Decryption_tool as dt
import HomePage as hp
import Session as ss

api_key = '150d6964434b7a63ad80a94e2be62165455afcc36042cde0aa9ecb88e03d3634'


def get_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_file_report(file_hash):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': file_hash}
    response = requests.get(url, params=params)
    return response.json()


def upload_file(file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    files = {'file': (file_path, open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)
    return response.json()


file_path1 = None
file_path2 = None
file_name = None


def File_decryption(root):
    # Fonts
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")

    # images
    # images
    image_back_path = os.path.join(os.path.dirname(__file__), "images", "logo", "back.png")
    logo_nav_path = os.path.join(os.path.dirname(__file__), "images", "logo", "logo.png")
    icon_path = os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico")

    def back_home():
        global file_path1
        global file_path2

        file_path1 = None
        file_path2 = None
        frameDecFich.destroy()
        hp.HomePage(root)

    def open_file(method):
        global file_path1, file_path2, file_name

        def ask_for_file(title, filetypes):
            return filedialog.askopenfilename(title=title, filetypes=filetypes)

        def update_label(label, file_path):
            label.configure(text=f"Selected file : {os.path.basename(file_path)}")

        if method == "method1":
            file_path1 = ask_for_file("Choose encrypted File",
                                      [("All files", ".*"), ("Text files", ".txt"), ("PDF files", ".pdf")])
            if file_path1:
                update_label(label_selected_file, file_path1)
        elif method == "method2":
            file_path1 = None
            file_path1 = ask_for_file("Choose encrypted File",
                                      [("All files", ".*"), ("Text files", ".txt"), ("PDF files", ".pdf")])
            if file_path1:
                update_label(label_selected_file1, file_path1)
        elif method == "method2+":
            file_path2 = ask_for_file("Choose Healthy File",
                                      [("All files", ".*"), ("Text files", ".txt"), ("PDF files", ".pdf")])
            if file_path2:
                update_label(label_selected_file2, file_path2)
            # Récupérer le nom de fichier à partir du chemin d'accès
            file_name = os.path.basename(file_path2)

    def is_connected_to_internet():
        try:
            # Attempt to create a socket connection to a reliable server
            socket.create_connection(("www.google.com", 80), timeout=2)
            return True
        except OSError:
            # Failed to connect to the server
            return False

    def Scan():
        global file_path1
        is_connected_to_internet()
        if file_path1:
            frameImportFile.destroy()
            # Display a message indicating the file is being scanned
            frameReport.place(x=10, y=140)

            label_scan_status.pack(pady=20)

            # Créer une barre de progression

            progress_bar1.pack(pady=20)
            progress_bar1.start()

            # Get the file hash
            file_hash = get_file_hash(file_path1)

            # Upload the file for scanning
            upload_response = upload_file(file_path1)
            print(upload_response)

            # Fetch the report after a short delay (you might need to adjust the delay based on the API response time)
            root.after(5000, lambda: display_scan_result(frameReport, file_hash))
        else:
            messagebox.showerror(title="File Error", message="Please upload a file")

    def display_scan_result(parent_frame, file_hash):
        global file_path1
        try:
            # Get the report after uploading or if the file has been scanned before
            report = get_file_report(file_hash)

            progress_bar1.destroy()
            label_scan_status.destroy()

            if report['response_code'] == 0 or 'verbose_msg' in report and 'Scan request successfully queued' in report[
                'verbose_msg']:
                # If the scan is queued, display a message
                messagebox.showinfo(title="Scan Queued",
                                    message="Scan request successfully queued. Come back later for the report.")
                back_home()

            elif report['response_code'] == 1:

                label_title = ctk.CTkLabel(master=frameReport, text="Scan Result :",
                                           font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                            weight="bold"))
                label_title.pack()
                label_positives = ctk.CTkLabel(master=frameReport, text="Positives : " + str(report['positives']),
                                               font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                                weight="bold"))
                label_positives.pack()
                label_total_scans = ctk.CTkLabel(master=frameReport, text="Total Scans : " + str(report['total']),
                                                 font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                                  weight="bold"))
                label_total_scans.pack()

                # Check if 'scan_engine' key exists in the report dictionary
                if 'scan_engine' in report:
                    label_scanned_by = ctk.CTkLabel(master=frameReport,
                                                    text="Scanned by : " + str(report['scan_engine']),
                                                    font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                                     weight="bold"))
                else:
                    label_scanned_by = ctk.CTkLabel(master=frameReport, text="Scanned by : VirusTotal",
                                                    font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                                     weight="bold"))
                label_scanned_by.pack()

                # Add more details as needed
                label_scan_date = ctk.CTkLabel(master=frameReport,
                                               text="Scan Date : " + str(report.get('scan_date', 'N/A')),
                                               font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                                weight="bold"))
                label_scan_date.pack()

                # Add a graph presenting the statistics of the report (Placeholder)

                generate_report_graph(parent_frame, report)

                # Check if 'scans' key exists in the report dictionary
                if 'scans' in report:
                    def rapportDetails():
                        fact_window = tk.Toplevel()
                        fact_window.title("Scan")
                        fact_window.geometry("1000x600")
                        fact_window.resizable(False, False)
                        fact_window.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico"))

                        fact_label = ctk.CTkLabel(fact_window, text="Information sur le scan")
                        fact_label.configure(font=("Courier", 14))
                        fact_label.pack()

                        fact_text = ctk.CTkTextbox(fact_window, height=600, width=700)
                        fact_text.pack()

                        # Boucle pour récupérer les informations de chaque scan
                        for scan, result in report['scans'].items():
                            # Création d'une chaîne de caractères pour chaque scan
                            fact_str = "{} : Detected - {} , Result - {}\n".format(scan, result.get('detected', 'N/A'),
                                                                                   result.get('result', 'N/A'))
                            # Ajout de cette chaîne à l'objet Textbox
                            fact_text.insert(tk.END, fact_str)

                button_results = ctk.CTkButton(master=parent_frame, text="Show details",
                                               command=lambda: rapportDetails())
                button_results.pack(side=tk.LEFT, padx=10)
                button_results_analyse = ctk.CTkButton(master=parent_frame, text="Afficher analyse fréquentielle",
                                                       command=lambda: show_analyse_frequentielle(file_path1))
                button_results_analyse.pack(side=tk.LEFT, padx=10)
                button_kasiski = ctk.CTkButton(master=parent_frame, text="Attaque kasiski",
                                               command=lambda: kasiski_from_file(file_path1))
                button_kasiski.pack(side=tk.LEFT, padx=10)
                button_next.pack(side=tk.RIGHT)
            else:
                messagebox.showerror(title="Scan Error", message="An error occurred during the scan.")
        except requests.exceptions.ConnectionError as e:
            messagebox.showerror(title="Connection Error",
                                 message="Failed to establish a connection to VirusTotal.")
            print(f"Failed to establish a connection to VirusTotal : {e}")

    def generate_report_graph(parent_frame, report):
        labels = ['Positives', 'Negatives']
        values = [report['positives'],
                  report['total'] - report['positives']]

        fig, ax = plt.subplots()
        ax.bar(labels, values)

        ax.set_xlabel('Scan Result')
        ax.set_ylabel('Number of Scans')
        ax.set_title('Scan Result Statistics')

        graph_frame = ctk.CTkFrame(parent_frame)
        graph_frame.pack()
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def indice_coincidence_mutuelle(frequencies):
        # Calcul de la somme des fréquences
        total = sum(frequencies.values())

        # Calcul de l'indice de coïncidence simple
        IC_simple = sum(freq * (freq - 1) for freq in frequencies.values()) / (total * (total - 1))

        # Calcul de l'IMC
        IMC = IC_simple - (1 / total)

        return IMC

    def analyse_frequentielle(path):
        frequencies = {}
        with open(path, 'rb') as file:
            contenu = file.read()
            for char in contenu:
                if char in frequencies:
                    frequencies[char] += 1
                else:
                    frequencies[char] = 1

        liste_frequences = [(chr(char), freq) for char, freq in frequencies.items()]
        liste_frequences.sort(key=lambda x: x[1], reverse=True)

        # Calcul de l'IMC
        IMC = indice_coincidence_mutuelle(frequencies)

        return liste_frequences, IMC

    def resultatAnalyseFrequentielle(resultats, IMC):
        fact_window = tk.Toplevel()
        fact_window.title("Analyse Frequentielle")
        fact_window.geometry("1000x650")
        fact_window.resizable(True, True)
        fact_window.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico"))

        fact_label = ctk.CTkLabel(fact_window, text="Information sur l'analyse fréquentielle")
        fact_label.configure(font=("Courier", 14))
        fact_label.pack()

        fact_text = tk.Text(fact_window, height=15, width=60)
        fact_text.pack()
        # Affichage de l'IMC
        fact_text.insert(tk.END, f"Indice de Coïncidence Mutuelle (IMC) : {IMC}\n")
        # Affichage des résultats d'analyse dans le widget Text
        for char, freq in resultats:
            fact_text.insert(tk.END, f"Caractère : {char}, Fréquence : {freq}\n")

        # Création d'un canvas pour le graphique
        fact_canvas = tk.Canvas(fact_window, height=300, width=800)
        fact_canvas.pack()

        # Calcul de la hauteur maximale pour normaliser les barres
        max_freq = max(freq for char, freq in resultats)

        # Dessin des barres pour les fréquences des caractères
        x_start = 50
        y_start = 250
        bar_width = 20
        for i, (char, freq) in enumerate(resultats):
            bar_height = (freq / max_freq) * 200
            fact_canvas.create_rectangle(x_start + i * 40, y_start - bar_height,
                                         x_start + i * 40 + bar_width, y_start,
                                         fill="blue")
            fact_canvas.create_text(x_start + i * 40 + bar_width / 2, y_start + 10,
                                    text=char, font=("Courier", 10))

        # Dessiner la ligne pour représenter l'IMC
        imc_line_y = y_start - IMC * 200  # IMC est normalisé entre 0 et 1
        fact_canvas.create_line(x_start, imc_line_y, x_start + len(resultats) * 40, imc_line_y, fill="red", width=2)
        fact_canvas.create_text(x_start + (len(resultats) * 40) + 20, imc_line_y, text=f"IMC: {IMC:.2f}", fill="red")

    def show_analyse_frequentielle(file_path):
        resultat, IMC = analyse_frequentielle(file_path)
        if resultat:
            resultatAnalyseFrequentielle(resultat, IMC)
        else:
            print("Aucun résultat d'analyse disponible.")

    from collections import defaultdict

    def find_repeats(text, min_length=3):
        repeats = defaultdict(list)
        for i in range(len(text) - min_length):
            for j in range(i + min_length, len(text)):
                if text[i:i + min_length] == text[j:j + min_length]:
                    repeats[text[i:i + min_length]].append((i, j))
        return repeats

    def calculate_distances(repeats):
        distances = defaultdict(list)
        for repeat, positions in repeats.items():
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    distances[repeat].append(positions[j][0] - positions[i][0])
        return distances

    def find_key_length(distances):
        factors = defaultdict(int)
        for distances_list in distances.values():
            for distance in distances_list:
                for i in range(2, distance):
                    if distance % i == 0:
                        factors[i] += 1
        return max(factors, key=factors.get)

    def decrypt(text, key_length):
        key = ''
        for i in range(key_length):
            group = ''
            for j in range(i, len(text), key_length):
                group += str(text[j])
            most_common_letter = max(set(group), key=group.count)
            key += chr((ord(most_common_letter) - ord('E')) % 26 + ord('A'))  # Assuming English language
        decrypted_text = ''
        for i, char in enumerate(text):
            if not key:
                break  # Prevent IndexError if the key is empty
            decrypted_text += chr((ord(char) - ord(key[i % key_length])) % 26 + ord('A'))
        return decrypted_text

    def kasiski_from_file(file_path):
        with open(file_path, 'rb') as file:
            cipher_text = file.read()
        repeats = find_repeats(cipher_text)
        distances = calculate_distances(repeats)
        key_length = find_key_length(distances)

        decrypted_text = decrypt(cipher_text.decode('utf-8'), key_length)

        fact_window = tk.Toplevel()
        fact_window.title("kasiski")
        fact_window.geometry("1000x650")
        fact_window.resizable(True, True)
        fact_window.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico"))

        fact_label = ctk.CTkLabel(fact_window, text="kasiski found key")
        fact_label.configure(font=("Courier", 14))
        fact_label.pack()

        fact_text = tk.Text(fact_window, height=15, width=60)
        fact_text.pack()
        # Affichage de key_length
        fact_text.insert(tk.END, f"Estimated key length: {key_length}\n")
        # Affichage des résultats d'analyse dans le widget Text
        fact_text.insert(tk.END, f"Decrypted text:: {decrypted_text}\n")

    def Next():
        frameReport.place_forget()
        frameReport.destroy()
        frameAlgo.pack(fill="both", expand=True, padx=80, pady=80)

    def generate_progressbar(button_name):
        if file_path1 and file_path2:
            if progress_bar.winfo_ismapped():
                messagebox.showinfo("Info", "Wait for other process to finish ...")
                return
            progress_bar.pack(pady=20)
            progress_bar.start()
            match button_name:
                case "motifs":
                    frameAlgo.after(11000, lambda: motifs())
                case "freq_oct_cipher":
                    frameAlgo.after(11000, lambda: afficher_frequence_octets())
                case "freq_oct_claire":
                    frameAlgo.after(11000, lambda: afficher_frequence_octets2())
                case "freq_oct_rsa":
                    frameAlgo.after(11000, lambda: afficher_frequence_octets_rsa())
                case "freq_oct_aes":
                    frameAlgo.after(11000, lambda: afficher_frequence_octets_aes())
        else:
            messagebox.showerror("Error", "Upload files first.")

    def motifs():
        if file_path1:
            resultat = ALG.recherche_motifs(file_path1)
            progress_bar.pack_forget()
            # Sélectionner les 6 motifs les plus fréquents
            motifs_freq = sorted(resultat.items(), key=lambda x: x[1], reverse=True)[:6]
            motifs_labels = [motif[0] for motif in motifs_freq]
            motifs_occurrences = [motif[1] for motif in motifs_freq]

            # Création de la fenêtre
            fact_window = tk.Toplevel()
            fact_window.title("recherche motifs")
            fact_window.geometry("1000x600")
            fact_window.resizable(True, True)
            fact_window.iconbitmap(icon_path)

            # Ajout du texte d'information
            fact_label = tk.Label(fact_window, text="Information sur les motifs", font=("Courier", 14))
            fact_label.pack()

            fact_text = tk.Text(fact_window, height=15, width=60)
            fact_text.pack()

            # Affichage des résultats
            for motif, occurrence in resultat.items():
                fact_text.insert(tk.END, f"motif : {motif}, Fréquence : {occurrence}\n")

            # Création du graphique
            fig = plt.figure(figsize=(6, 2))
            plt.bar(motifs_labels, motifs_occurrences, color='skyblue')
            plt.xlabel('Motifs')
            plt.ylabel('Fréquence')
            plt.title('Les 6 motifs les plus fréquents')
            plt.xticks(rotation=0)
            plt.tight_layout()

            # Création d'un canvas pour afficher le graphique dans la fenêtre Tkinter
            canvas = FigureCanvasTkAgg(fig, master=fact_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            messagebox.showwarning(title="Warning", message="select file")

    def afficher_frequence_octets():
        if file_path1:
            resultat = ALG.analyse_frequence_octets(file_path1)
            progress_bar.pack_forget()

            # Trier les octets par fréquence
            octets_freq1 = sorted(resultat.items(), key=lambda x: x[1], reverse=True)
            octets_labels = [octet[0] for octet in octets_freq1]
            octets_occurrences = [octet[1] for octet in octets_freq1]
            # Sélectionner les 6 premiers octets les plus fréquents
            octets_freq = Counter(resultat).most_common(6)
            octets_labels = [octet[0] for octet in octets_freq]
            octets_occurrences = [octet[1] for octet in octets_freq]

            # Création de la fenêtre
            fact_window = tk.Toplevel()
            fact_window.title("Analyse de la fréquence des octets")
            fact_window.geometry("1000x600")
            fact_window.resizable(True, True)
            # fact_window.iconbitmap(icon_path) # Assurez-vous que votre chemin d'icône est correct

            # Ajout du texte d'information
            fact_label = tk.Label(fact_window, text="Analyse de la fréquence des octets", font=("Courier", 14))
            fact_label.pack()

            fact_text = tk.Text(fact_window, height=15, width=60)
            fact_text.pack()

            # Affichage des résultats triés par fréquence
            for octet, occurrence in octets_freq1:
                fact_text.insert(tk.END, f"Octet : {octet}, Fréquence : {occurrence:.2f}%\n")

            # Création du graphique
            fig = plt.figure(figsize=(6, 2))
            plt.bar(octets_labels, octets_occurrences, color='skyblue')
            plt.xlabel('Octets')
            plt.ylabel('Fréquence')
            plt.title('Les octets les plus fréquents')
            plt.tight_layout()

            # Création d'un canvas pour afficher le graphique dans la fenêtre Tkinter
            canvas = FigureCanvasTkAgg(fig, master=fact_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            messagebox.showwarning(title="Warning", message="Select file")

    def afficher_frequence_octets2():
        if file_path2:
            resultat = ALG.generer_profil_frequence(file_path2)
            progress_bar.pack_forget()

            # Trier les octets par fréquence
            octets_freq1 = sorted(resultat.items(), key=lambda x: x[1], reverse=True)

            # Sélectionner les 6 premiers octets les plus fréquents
            octets_freq = Counter(resultat).most_common(6)
            octets_labels = [octet[0] for octet in octets_freq]
            octets_occurrences = [octet[1] for octet in octets_freq]

            # Création de la fenêtre
            fact_window = tk.Toplevel()
            fact_window.title("Analyse de la fréquence des octets")
            fact_window.geometry("1000x600")
            fact_window.resizable(True, True)
            # fact_window.iconbitmap(icon_path) # Assurez-vous que votre chemin d'icône est correct

            # Ajout du texte d'information
            fact_label = tk.Label(fact_window, text="Analyse de la fréquence des octets", font=("Courier", 14))
            fact_label.pack()

            fact_text = tk.Text(fact_window, height=15, width=60)
            fact_text.pack()

            # Affichage des résultats triés par fréquence
            for octet, occurrence in octets_freq1:
                fact_text.insert(tk.END, f"Octet : {octet}, Fréquence : {occurrence:.2f}%\n")

            # Création du graphique
            fig = plt.figure(figsize=(6, 2))
            plt.bar(octets_labels, octets_occurrences, color='skyblue')
            plt.xlabel('Octets')
            plt.ylabel('Fréquence')
            plt.title('Les octets les plus fréquents')
            plt.tight_layout()

            # Création d'un canvas pour afficher le graphique dans la fenêtre Tkinter
            canvas = FigureCanvasTkAgg(fig, master=fact_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            messagebox.showwarning(title="Warning", message="Select file")

    def afficher_frequence_octets_rsa():
        if file_path2:
            resultat = ALG.generer_profil_frequence_rsa(file_path2)
            progress_bar.pack_forget()

            # Trier les octets par fréquence
            octets_freq1 = sorted(resultat.items(), key=lambda x: x[1], reverse=True)

            # Sélectionner les 6 premiers octets les plus fréquents
            octets_freq = Counter(resultat).most_common(6)
            octets_labels = [octet[0] for octet in octets_freq]
            octets_occurrences = [octet[1] for octet in octets_freq]

            # Création de la fenêtre
            fact_window = tk.Toplevel()
            fact_window.title("Analyse de la fréquence des octets rsa")
            fact_window.geometry("1000x600")
            fact_window.resizable(True, True)
            # fact_window.iconbitmap(icon_path) # Assurez-vous que votre chemin d'icône est correct

            # Ajout du texte d'information
            fact_label = tk.Label(fact_window, text="Analyse de la fréquence des octets rsa", font=("Courier", 14))
            fact_label.pack()

            fact_text = tk.Text(fact_window, height=15, width=60)
            fact_text.pack()

            # Affichage des résultats triés par fréquence
            for octet, occurrence in octets_freq1:
                fact_text.insert(tk.END, f"Octet : {octet}, Fréquence : {occurrence:.2f}%\n")

            # Création du graphique
            fig = plt.figure(figsize=(6, 2))
            plt.bar(octets_labels, octets_occurrences, color='skyblue')
            plt.xlabel('Octets')
            plt.ylabel('Fréquence')
            plt.title('Les octets les plus fréquents')
            plt.tight_layout()

            # Création d'un canvas pour afficher le graphique dans la fenêtre Tkinter
            canvas = FigureCanvasTkAgg(fig, master=fact_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            messagebox.showwarning(title="Warning", message="Select file")

    def afficher_frequence_octets_aes():
        if file_path2:
            resultat = ALG.generer_profil_frequence_aes(file_path2)
            progress_bar.pack_forget()

            # Trier les octets par fréquence
            octets_freq1 = sorted(resultat.items(), key=lambda x: x[1], reverse=True)

            # Sélectionner les 6 premiers octets les plus fréquents
            octets_freq = Counter(resultat).most_common(6)
            octets_labels = [octet[0] for octet in octets_freq]
            octets_occurrences = [octet[1] for octet in octets_freq]

            # Création de la fenêtre
            fact_window = tk.Toplevel()
            fact_window.title("Analyse de la fréquence des octets aes")
            fact_window.geometry("1000x600")
            fact_window.resizable(True, True)
            # fact_window.iconbitmap(icon_path) # Assurez-vous que votre chemin d'icône est correct

            # Ajout du texte d'information
            fact_label = tk.Label(fact_window, text="Analyse de la fréquence des octets aes", font=("Courier", 14))
            fact_label.pack()

            fact_text = tk.Text(fact_window, height=15, width=60)
            fact_text.pack()

            # Affichage des résultats triés par fréquence
            for octet, occurrence in octets_freq1:
                fact_text.insert(tk.END, f"Octet : {octet}, Fréquence : {occurrence:.2f}%\n")

            # Création du graphique
            fig = plt.figure(figsize=(6, 2))
            plt.bar(octets_labels, octets_occurrences, color='skyblue')
            plt.xlabel('Octets')
            plt.ylabel('Fréquence')
            plt.title('Les octets les plus fréquents')
            plt.tight_layout()

            # Création d'un canvas pour afficher le graphique dans la fenêtre Tkinter
            canvas = FigureCanvasTkAgg(fig, master=fact_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        else:
            messagebox.showwarning(title="Warning", message="Select file")

    def comparer():
        if file_path1 and file_path2:
            messagebox.showinfo(title="Information", message=ALG.comparer_profils(file_path1, file_path2))
        else:
            messagebox.showerror("Error", "Upload files first.")

    def afficher_utilisation_ressources():
        # Créer une fenêtre Tkinter
        fenetre = tk.Tk()
        fenetre.geometry("1600x600")
        fenetre.title("Utilisation des ressources")
        fenetre.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "logo", "icon.ico"))

        # Créer des figures pour chaque type de ressource
        fig_cpu = plt.figure(figsize=(6, 4))
        fig_ram = plt.figure(figsize=(6, 4))

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
        canvas_ram.get_tk_widget().pack(side=tk.RIGHT, padx=10, pady=10)

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
            afficher_utilisation_ressources()

    def find_key():
        try:
            if file_path1 and file_path2:
                check_ram_usage_threshold(87)
                start_time = time.time()
                keys = ALG.generatedKeys(file_path1, file_path2)  # Appel de la fonction generatedKeys du module ALG
                end_time = time.time()
                if keys is not None:
                    # Calcul de la durée totale de génération des clés
                    total_time = end_time - start_time

                    # Création de la fenêtre
                    fact_window = tk.Toplevel()
                    fact_window.title("Generation of keys")
                    fact_window.geometry("1000x600")
                    fact_window.resizable(False, False)
                    fact_window.iconbitmap(icon_path)

                    # Étiquette d'information
                    fact_label = ctk.CTkLabel(fact_window, text="Possible keys for decryption",
                                              font=("Courier", 14))
                    fact_label.pack()

                    # Textbox pour afficher les informations
                    fact_text = ctk.CTkTextbox(fact_window, height=600, width=700)
                    fact_text.place(x=30, y=60)

                    # Affichage du temps total de génération des clés
                    fact_text.insert(tk.END, f"Total time : {total_time} secondes\n")

                    # Affichage de chaque clé générée
                    for key in keys:
                        fact_text.insert(tk.END, f"Key : {key}\n")
                else:
                    print("Clés non touvés")

                # Trouver la clé utilisée
                key = ALG.find_private_key(file_path1, file_path2)
                if key is not None:
                    messagebox.showinfo(title="Key",
                                        message="Key of decryption is :" + key.hex())
                else:
                    messagebox.showwarning("Warning", "Keys not generated, please check decryption tools")
                    frameDecFich.destroy()
                    dt.Decryption_tool(root)
                timedecryptage = time.time()
                # Convertir le timestamp en objet datetime
                date_reparation = datetime.datetime.fromtimestamp(timedecryptage).date()
                insert_query = f"INSERT INTO Fichiers_rep (Date_reparation, CLE, NAME_FILE, id_user) " \
                               f"VALUES (TO_DATE('{date_reparation}', 'YYYY-MM-DD'), '{str(key.hex())}', '{file_name}'),'{ss.current_user}'"
                if DB.execute_query(insert_query):
                    print("ajouter avec succes dans DB")
                else:
                    print("fichiers non ajoutés dans DB")
            else:
                messagebox.showerror("Files Error", "Upload both files")
        except Exception as e:
            print(f" error : {e}")

    # Main Frame
    frameDecFich = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameDecFich.pack(fill=tk.BOTH, expand=True)

    # Label and back button
    button_back = ctk.CTkButton(master=frameDecFich, text="",
                                image=ctk.CTkImage(light_image=Image.open(image_back_path), size=(65, 65)), hover=False,
                                compound="top", cursor="hand2", bg_color="transparent",
                                fg_color="transparent", command=back_home)
    button_back.place(x=36, y=70)

    label_dec_file = ctk.CTkLabel(master=frameDecFich, text="File Decryption",
                                  font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=25, weight="bold"))
    label_dec_file.place(x=150, y=88)

    # Navbar Frame
    NavBarDecFich = ctk.CTkFrame(master=frameDecFich, fg_color="#fff", bg_color="#fff", width=1400, height=60)
    NavBarDecFich.pack()

    label_logo_nav_df = ctk.CTkLabel(master=NavBarDecFich, text="",
                                     image=ctk.CTkImage(light_image=Image.open(logo_nav_path), size=(179, 38)))
    label_logo_nav_df.place(x=10, y=10)

    # Importing File Frame
    frameImportFile = ctk.CTkFrame(master=frameDecFich, fg_color="white", bg_color="transparent", corner_radius=20,
                                   width=1000, height=400)
    frameImportFile.pack(fill="both", expand=True, padx=150, pady=150)
    progress_bar1 = ctk.CTkProgressBar(master=root, mode='indeterminate')

    label_addfile = ctk.CTkLabel(master=frameImportFile,
                                 text="Converting an encrypted (unreadable) file into a readable and understandable format",
                                 font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19, weight="bold"))
    label_addfile.pack(padx=20, pady=20)

    button_import = ctk.CTkButton(master=frameImportFile, font=ButtonsFont, width=300, height=50,
                                  text=f"Select file", text_color="#000", fg_color="#B7EAF5",
                                  bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                  compound="top", cursor="hand2", command=lambda: open_file("method1"))
    button_import.pack(padx=20, pady=20)

    label_selected_file = ctk.CTkLabel(master=frameImportFile, text="",
                                       font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                        weight="bold"))
    label_selected_file.pack(side=tk.TOP, expand=True)

    button_scan = ctk.CTkButton(master=frameImportFile, font=ButtonsFont, width=100, height=50,
                                text="Scan", text_color="#000", fg_color="#B7EAF5",
                                bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                compound="top", cursor="hand2", command=Scan)
    button_scan.pack(side=tk.RIGHT, anchor=tk.S, padx=10, pady=10)

    frameReport = ctk.CTkScrollableFrame(master=frameDecFich, fg_color="white", bg_color="transparent",
                                         corner_radius=20, width=1340, height=500)

    button_next = ctk.CTkButton(master=frameReport, font=ButtonsFont, width=100, height=50,
                                text="Next", text_color="#000", fg_color="#B7EAF5",
                                bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                compound="top", cursor="hand2", command=Next)
    label_scan_status = ctk.CTkLabel(master=frameReport, text="Scanning file, please wait...",
                                     font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                      weight="bold"))
    ##################################
    # Importing decrypted and healthy files Frame
    frameAlgo = ctk.CTkFrame(master=frameDecFich, fg_color="white", bg_color="transparent", corner_radius=20,
                             width=1200, height=600)
    progress_bar = ctk.CTkProgressBar(master=root, mode='indeterminate')

    label_algo = ctk.CTkLabel(master=frameAlgo,
                              text="Unfortunately,VirusTotal was unable to identify this ransomware.However,if you have another affected file different from the one you want to decrypt,and if there is an unaffected version of this file located elsewhere,you could provide us with that alternative version.Your contribution could be crucial in assisting us to develop a decryption process.",
                              font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=12, weight="bold"),
                              anchor="center", justify="center", wraplength=1000)

    label_algo.pack(padx=10, pady=10)
    button_import2 = ctk.CTkButton(master=frameAlgo, font=ButtonsFont, width=300, height=50,
                                   text="Select encrypted file", text_color="#000", fg_color="#B7EAF5",
                                   bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                   compound="top", cursor="hand2", command=lambda: open_file("method2"))
    button_import2.pack(padx=15, pady=15)
    label_selected_file1 = ctk.CTkLabel(master=frameAlgo, text="",
                                        font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                         weight="bold"))
    label_selected_file1.pack(padx=5, pady=5)

    button_import3 = ctk.CTkButton(master=frameAlgo, font=ButtonsFont, width=300, height=50,
                                   text="Select healthy file", text_color="#000", fg_color="#B7EAF5",
                                   bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                   compound="top", cursor="hand2", command=lambda: open_file("method2+"))
    button_import3.pack(padx=15, pady=15)
    label_selected_file2 = ctk.CTkLabel(master=frameAlgo, text="",
                                        font=ctk.CTkFont(family="Microsoft YaHei UI Light", size=19,
                                                         weight="bold"))
    label_selected_file2.pack(padx=5, pady=5)

    # Add the "Find Key" button after the import statements
    button_find_key = ctk.CTkButton(master=frameAlgo, font=ButtonsFont, width=200, height=50,
                                    text="Find Key", text_color="#000", fg_color="#B7EAF5",
                                    bg_color="#fff", hover_color="#78d7ed", corner_radius=20,
                                    compound="top", cursor="hand2", command=find_key)
    button_find_key.pack(anchor=tk.E, padx=20)
    button_resources = ctk.CTkButton(master=frameAlgo,
                                     text="Check Ressources", command=afficher_utilisation_ressources)
    button_resources.pack(side=tk.LEFT, padx=10)

    button_motifs = ctk.CTkButton(master=frameAlgo,
                                  text="motifs", command=lambda: generate_progressbar("motifs"))
    button_motifs.pack(side=tk.LEFT, padx=10)

    button_octes = ctk.CTkButton(master=frameAlgo,
                                 text="frq_oct_cipher", command=lambda: generate_progressbar("freq_oct_cipher"))
    button_octes.pack(side=tk.LEFT, padx=10)

    button_octes2 = ctk.CTkButton(master=frameAlgo,
                                  text="frq_oct_claire", command=lambda: generate_progressbar("freq_oct_claire"))
    button_octes2.pack(side=tk.LEFT, padx=10)

    button_octes3 = ctk.CTkButton(master=frameAlgo,
                                  text="frq_oct_rsa", command=lambda: generate_progressbar("freq_oct_rsa"))
    button_octes3.pack(side=tk.LEFT, padx=10)

    button_octes4 = ctk.CTkButton(master=frameAlgo,
                                  text="frq_oct_aes", command=lambda: generate_progressbar("freq_oct_aes"))
    button_octes4.pack(side=tk.LEFT, padx=10)

    button_CMP = ctk.CTkButton(master=frameAlgo,
                               text="comparer", command=comparer)
    button_CMP.pack(side=tk.LEFT, padx=10)
