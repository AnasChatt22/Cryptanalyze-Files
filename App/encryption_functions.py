import math
import os
import random

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from sympy import isprime


# *********************AES*****************************
def encrypt_file_aes(file_path, key_size=256):
    # Générer une clé secrète à partir d'un mot de passe (vous pouvez utiliser une méthode plus sécurisée pour stocker le mot de passe)
    password = b'mon_mot_de_passe_secret'
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_size // 8,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)

    # Initialiser le vecteur d'initialisation (IV)
    iv = os.urandom(16)

    # Lire le contenu du fichier
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Utiliser AES pour crypter le fichier
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_content = encryptor.update(file_content) + encryptor.finalize()

    # Retourner le fichier crypté, la clé privée et la taille de la clé
    return encrypted_content, key


# ************************RSA**************************
def generate_key(key_size):
    """
    Génère une paire de clés RSA de la taille spécifiée
    """
    while True:

        p = random.randint(2 ** (key_size - 1), 2 ** key_size - 1)
        if isprime(p):
            break

    while True:

        q = random.randint(2 ** (key_size - 1), 2 ** key_size - 1)
        if isprime(q):
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:

        e = random.randint(2 ** (key_size - 1), 2 ** key_size - 1)
        if math.gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def mod_inverse(a, m):
    """
    Calcule l'inverse modulaire d'un nombre
    """
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if x < 0:
        x += m0

    return x


def encrypt_fileRSA(file_path, key_size):
    key, private_key = generate_key(key_size)
    """
    Crypte un fichier avec une clé RSA
    """
    with open(file_path, 'rb') as f:
        data = f.read()

    # On convertit les données en entier
    data = int.from_bytes(data, byteorder='big')

    # On calcule le message chiffré
    encrypted_data = pow(data, key[0], key[1])

    # On convertit le message chiffré en bytes
    encrypted_data = encrypted_data.to_bytes((encrypted_data.bit_length() + 7) // 8, byteorder='big')

    # On écrit les données chiffrées dans un nouveau fichier
    with open(file_path + '.encrypted', 'wb') as f:
        f.write(encrypted_data)

    return encrypted_data, private_key
