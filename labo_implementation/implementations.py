import os
import struct
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import gmpy2
import pandas as pd
from PIL import Image, ImageTk

import fonctions

window = Tk()
# ---------------------------------------------------------------------------------------les variables d'entrer
e_publique = IntVar()
cypher = StringVar()
n_publique = IntVar()
attaque = StringVar()
message = StringVar()
taille = IntVar()
value = [0, 0, 0, 0, 0, 0]
name = ['p', 'q', 'n', 'e', 'd', 'phi']
dataFrame = pd.DataFrame(data=name, index=value)
expediteur = StringVar()
Destinataire = StringVar()
expediteur.set('Expéditeur')
Destinataire.set('Destinataire')


# ------------------------------------------------------------------------------------------------------fonction

# ////////////////////// la fonctin qui permet de changer le role entre alice et bob/////////////////////

def chg():
    if expediteur.get() == "Destinataire":
        expediteur.set('Expéditeur')
        lb7.place(x=60, y=240)
        en2.place(x=70, y=270)
        bttt.place(x=185, y=270)

    else:
        expediteur.set('Destinataire')
        lb7.place_forget()
        en2.place_forget()
        bttt.place_forget()
    if Destinataire.get() == "Destinataire":
        Destinataire.set('Expéditeur')
        lb8.place(x=810, y=240)
        enn.place(x=820, y=270)
        bt2.place(x=935, y=270)
    else:
        Destinataire.set('Destinataire')
        lb8.place_forget()
        enn.place_forget()
        bt2.place_forget()


# ////////////////la fonction qui deplace le message d'expéditeur vers le Destinataire/////////////////////

def send_message():
    # create image
    im_path = os.path.join(os.path.dirname(__file__), "images", "logo", "mi.gif")
    im = Image.open(im_path).resize((60, 60))  # resize image to 60x60 pixels
    photo = ImageTk.PhotoImage(im)

    # create label to show image
    lb = Label(window, image=photo)
    lb.image = photo

    if expediteur.get() == "Expéditeur":  # Alice est l'expéditeur
        # animate image moving from alice to bob
        lb.place(x=50, y=50)

        def animate(x, y):
            lb.place(x=x, y=y)
            if x < 800:
                window.after(10, animate, x + 5, y)
            else:
                lb.bind("<Button-1>", display_message)  # bind the label to the click event

        def display_message(event):
            msg = message.get()
            messagebox.showinfo("Message from Alice", msg)
            lb.place_forget()

        animate(50, 50)

    else:  # Alice est le destinataire
        lb.place(x=700, y=50)

        def animate(x, y):
            lb.place(x=x, y=y)
            if x > 130:
                window.after(10, animate, x - 5, y)
            else:
                lb.bind("<Button-1>", display_message)  # bind the label to the click event

        def display_message(event):
            msg = message.get()
            messagebox.showinfo("Message from Bob", msg)
            lb.place_forget()

        animate(700, 50)


# //////////////////////// Fonction pour afficher/masquer l'Entry////////////////////////////////
def show_entry():
    if cbx_attaque.current() == 0:
        n_label.place_forget()
        n_entry.place_forget()
        e_label.place_forget()
        e_entry.place_forget()
        c_label.place_forget()
        c_entry.place_forget()
        cryptanalyse_button.place_forget()
    else:
        n_label.place(x=600, y=190)
        n_entry.place(x=600, y=210)
        e_label.place(x=600, y=230)
        e_entry.place(x=600, y=250)
        c_label.place(x=600, y=270)
        c_entry.place(x=600, y=290)
        cryptanalyse_button.place(x=730, y=208)


# ------------------------------------------------------------------------------------------------window gui

# ///////////////////////style//////////////////////


s = ttk.Style(window)
s.theme_use('clam')
s.configure('Treeview', background='#2E4053', fieldbackground='#2E4053', foreground='white')
s.configure("my.Treeview.Heading", background='#82E0AA', foreground='black', relief='flat')

# ////////////////detaille window/////////////////////


window.title('RSA')
window.geometry('1000x600')
window.config(bg='white')
window.resizable(False, False)
copyright = u"\u00A9"
font1 = ('Times', 7, 'bold')
title = Label(window, text=' cryptosystème RSA', font='tajawal,11', fg='black', bg='#3498DB')
title.pack(fill=X)
title = Label(window, text=copyright + '  ', font=font1, bg='#3498DB')
title.place(x=799, y=0)
# Get the full path to the icon file
# icon_path = os.path.abspath("icon.ico")
# Set the icon for the main window using the full path
# window.iconbitmap(icon_path)
# window.iconbitmap('icone.ico')

img_path = os.path.abspath("img.png")
im = PhotoImage(img_path)
lb = Label(window, image=im)
lb.pack()
lb6 = Label(window, text='taille(bits) :', font=('cursive', 10), fg='black', bg='white')
lb6.place(x=450, y=50)
cbx1 = ttk.Combobox(window, textvariable=taille)
cbx1['value'] = (16, 32, 64, 128, 256, 512, 1024, 2048)
cbx1.place(x=450, y=70)
cry_RSA = Button(window, text='Génération de cryptosystème RSA ',
                 command=lambda: generatab(taille.get(), dataFrame, message.get()), fg='white', bg='#2ECC71')
cry_RSA.place(x=420, y=93)

changer_role = Button(window, text='changer les roles',
                      fg='white', bg='#7B7D7D', command=chg)
changer_role.place(x=510, y=130)

attaque_label = Label(window, text='Les attaques :', font=(
    'cursive', 10), fg='black', bg='white')
attaque_label.place(x=450, y=170)
n_label = Label(window, text='Clé publique (n):',
                font=('cursive', 10), fg='black', bg='white')
# Créer une Entry
n_entry = Entry(window, bg='#F9E79F', textvariable=n_publique)
e_label = Label(window, text="Clé publique (e):", font=('cursive', 10), fg='black', bg='white')
e_entry = Entry(window, bg='#F9E79F', textvariable=e_publique)
c_label = Label(window, text="Cryptogramme:", font=('cursive', 10), fg='black', bg='white')
c_entry = Entry(window, bg='#F9E79F', textvariable=cypher)
cryptanalyse_button = Button(window, text='cryptanalyser', fg='white',
                             bg='#E74C3C', command=lambda: factorisation(n_publique.get()))
cbx_attaque = ttk.Combobox(window, textvariable=attaque)
cbx_attaque['value'] = (" ", "factorisation")
cbx_attaque.place(x=450, y=190)
# Associer la fonction à la ComboBox
cbx_attaque.bind("<<ComboboxSelected>>", lambda e: show_entry())

# ----------------------------------------------------------------------------------------------alice gui

fr1 = Frame(window)
fr1.place(x=50, y=50, width=100, height=100)
img2_path = os.path.abspath("img2.png")
im = PhotoImage(img2_path)
im2 = PhotoImage(img2_path)
lb2 = Label(fr1, image=im2, text='Alice')
lb2.pack()
lb3 = Label(window, text='Alice', font=('fantasy', 15), fg='black', bg='white')
lb3.place(x=72, y=160)
lbr0 = Label(window, textvariable=expediteur)
lbr0.place(x=62, y=210)

lb7 = Label(window, text='Message :', font=('cursive', 10), fg='black', bg='white')
en2 = Entry(window, bg='#F9E79F', font=('cursive', 15), width=10, textvariable=message)

# create button to send message
bttt = Button(window, text='Envoyer', fg='white', bg='#E74C3C', command=send_message)

# ----------------------------------------------------------------------------------------------Bob gui

fr2 = Frame(window)
fr2.place(x=850, y=50, width=100, height=100)
img3_path = os.path.abspath("img3.png")
im3 = PhotoImage(img3_path)
lb4 = Label(fr2, image=im3, text='Bob')
lb4.pack()
lb5 = Label(window, text='Bob', font=('fantasy', 15), fg='black', bg='white')
lb5.place(x=872, y=160)
lbr = Label(window, textvariable=Destinataire)
lbr.place(x=862, y=210)

lb8 = Label(window, text='Message :', font=(
    'cursive', 10), fg='black', bg='white')
enn = Entry(window, bg='#F9E79F', font=(
    'cursive', 15), width=10, textvariable=message)

bt2 = Button(window, text='Envoyer', fg='white', bg='#E74C3C', command=send_message)

# ------------------------------------------------------------------------------------ gui treeview

fr3 = Frame(window, bg='#D5F5E3')
fr3.place(x=1, y=430, width=999, height=170)
title1 = Label(fr3, text='Temp de Génération des cryptosystème RSA', fg='black', bg='#3498DB')
title1.pack(fill=X)
scrollx = ttk.Scrollbar(fr3, orient=HORIZONTAL)
scrolly = ttk.Scrollbar(fr3, orient=VERTICAL)
trv = ttk.Treeview(fr3, columns=('temp_de_gk', 'temp_de_cryptage', 'temp_de_decryptage'), style='my.Treeview',
                   xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
trv.place(x=15, y=21, width=983, height=137)
scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=LEFT, fill=Y)
scrollx.config(command=trv.xview)
scrolly.config(command=trv.yview)
trv['show'] = 'headings'

trv.heading('temp_de_gk', text='temp_de_gk')
trv.heading('temp_de_cryptage', text='temp_de_cryptage')
trv.heading('temp_de_decryptage', text='temp_de_decryptage')

trv.column('temp_de_gk', width=320)
trv.column('temp_de_cryptage', width=320)
trv.column('temp_de_decryptage', width=320)


# ////////// appelle de generateur des cles premier et cryptage & affichage d'information de cle de cryptage//////////


def generatab(keySize, df, message):
    start_time_gk = time.perf_counter()
    result = fonctions.generate_Key(keySize)
    end_time_gk = time.perf_counter()
    temp_de_gk = end_time_gk - start_time_gk

    # Convertir le message en octets à l'aide de struct.pack
    # convertit le message en octets qui ont une longueur fixe et qui représentent exactement les octets du message
    start_time_cryptage = time.perf_counter()
    message_bytes = struct.pack('!{}s'.format(len(message)), message.encode())

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
    trv["column"] = list(df.columns)
    trv["show"] = "headings"
    for column in trv["column"]:
        trv.heading(column, text=column)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        trv.insert("", "end", values=row)
    trv.pack()
    root = Tk()
    root.title("Table")
    root.geometry("1000x600")
    root.resizable(False, False)
    T = Text(root, height=600, width=1000)
    l = Label(root, text="information sur le cryptosystème")
    l.config(font=("Courier", 14))
    l.pack()
    Fact = ('p:' + str(result[0]) + " \n" + " \n" + 'q:' + str(result[1]) + " \n" + " \n" + 'n:' + str(
        result[2]) + " \n" + " \n" + 'e:' + str(result[3]) + " \n" + " \n" + 'd:' + str(
        result[4]) + " \n" + " \n" + '\u03C6:' + str(result[5]) + " \n" + " \n" + "Message chiffré : " + str(
        crypt) + "\n" + " \n" + "message dechiffrer : " + str(asci2))
    b2 = Button(root, text="Exit", bg='#3498DB', command=root.destroy)
    b2.place(x=0, y=30, width=1000)
    T.insert(END, Fact)
    T.place(x=30, y=60, width=930, height=500)
    scrollbar2 = ttk.Scrollbar(root, orient=HORIZONTAL)
    scrollbar1 = ttk.Scrollbar(root, orient=VERTICAL)
    scrollbar1.pack(side=RIGHT, fill=Y)
    scrollbar2.pack(side=BOTTOM, fill=X)
    scrollbar2.config(command=T.xview)
    scrollbar1.config(command=T.yview)


# ---------------------------------------------------------------------------------------------cryptanalye rsa


def factorisation(n):
    # code existant pour la factorisation

    start_time = time.time()
    p_crack, q_crack = fonctions.factorize(n)
    end_time = time.time()
    if p_crack is not None and q_crack is not None:
        temp = end_time - start_time
        root = Tk()
        root.title("Table")
        root.geometry("1000x600")
        root.resizable(False, False)
        T = Text(root, height=600, width=1000)
        l = Label(root, text="information sur la factorisation")
        l.config(font=("Courier", 14))
        l.pack()
        Fact = (
            'Clé privée trouvée :\n\nn: {}\n\np: {}\n\nq: {}\n\nTemps total de factorisation : {} secondes'.format(n,
                                                                                                                   p_crack,
                                                                                                                   q_crack,
                                                                                                                   temp))
        b2 = Button(root, text="Exit", bg='#3498DB', command=root.destroy)
        b2.place(x=0, y=30, width=1000)
        T.insert(END, Fact)
        T.place(x=30, y=60, width=930, height=300)
        scrollbar2 = ttk.Scrollbar(root, orient=HORIZONTAL)
        scrollbar1 = ttk.Scrollbar(root, orient=VERTICAL)
        scrollbar1.pack(side=RIGHT, fill=Y)
        scrollbar2.pack(side=BOTTOM, fill=X)
        scrollbar2.config(command=T.xview)
        scrollbar1.config(command=T.yview)
        print('calculer d ')
        d = fonctions.findModInverse(e_publique.get(), (p_crack - 1) * (q_crack - 1))
        decrypt = [str(gmpy2.powmod(int(i.strip().strip("'")), d, n)) for i in cypher.get().strip('[]').split(',')]

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
        messagebox.showinfo("La cryptanalyse a échoué.",
                            "Veuillez réessayer avec un autre algorithme de factorisation.")

    # Ajouter deux champs d'entrée pour la clé publique et le cryptogramme


# -----------------------------------------------------------------------------------------vider les champs

def clear_tree():
    trv.delete(*trv.get_children())
    cbx1.delete(0, END)
    en2.delete(0, END)
    enn.delete(0, END)


bt5 = Button(window, text='vider les cases', command=clear_tree, fg='white', bg='#E74C3C')
bt5.place(x=420, y=130)

window.mainloop()
