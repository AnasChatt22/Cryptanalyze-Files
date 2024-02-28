
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes




def generatedKeys(plaintext_file, encrypted_file):
    # Lire le contenu des fichiers
    with open(plaintext_file, 'rb') as f:
        plaintext = f.read()
    with open(encrypted_file, 'rb') as f:
        ciphertext = f.read()

    keys = []
    block_size = AES.block_size
    num_blocks = min(len(plaintext), len(ciphertext)) // block_size

    # Générer les clés à partir du XOR de chaque bloc de texte en clair et de texte chiffré
    for i in range(num_blocks):
        key = bytes([p ^ c for p, c in zip(plaintext[i * block_size:(i + 1) * block_size],
                                           ciphertext[i * block_size:(i + 1) * block_size])])
        keys.append(key)

    # Générer les clés à partir de toutes les combinaisons possibles
    # possible_combinations = itertools.product(range(256), repeat=block_size)
    # for combination in possible_combinations:
    #     key = bytes(combination)
    #     keys.append(key)
    return keys


def find_private_key(plaintext_file, encrypted_file):
    # Générer les clés
    keys = generatedKeys(plaintext_file, encrypted_file)

    # Lire le contenu des fichiers
    with open(plaintext_file, 'rb') as f:
        plaintext = f.read()
    with open(encrypted_file, 'rb') as f:
        ciphertext = f.read()

    # Itérer sur chaque clé et vérifier si elle correspond au chiffrement du texte en clair
    for key in keys:
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted_plaintext = cipher.encrypt(pad(plaintext, AES.block_size))

        if encrypted_plaintext == ciphertext:
            return key

    # Si aucune clé ne correspond, retourner None
    return None



##################################

def recherche_motifs(path):
    with open(path, 'rb') as file:
        contenu = file.read()
    motifs = {}
    longueur_texte = len(contenu)

    for i in range(longueur_texte):
        for j in range(3, longueur_texte - i + 1):
            motif = contenu[i:i + j]
            if motif in motifs:
                motifs[motif] += 1
            else:
                motifs[motif] = 1

    return motifs






from collections import Counter


def analyse_frequence_octets(path):
    with open(path, 'rb') as file:
        contenu = file.read()
    # Compter la fréquence de chaque octet dans le texte chiffré
    compteur_octets = Counter(contenu)

    # Calculer la fréquence relative de chaque octet
    taille_texte = len(contenu)
    frequence_octets = {octet: (occurrence / taille_texte) * 100 for octet, occurrence in compteur_octets.items()}

    return frequence_octets


# Profils de fréquence des octets pour AES et RSA

from collections import Counter


def generer_profil_frequence(path):
    with open(path, 'rb') as file:
        contenu = file.read()
    # Compter la fréquence de chaque octet dans le texte clair
    compteur_octets = Counter(contenu)

    # Calculer la fréquence relative de chaque octet
    taille_texte = len(contenu)
    profil = {octet: (occurrence / taille_texte) for octet, occurrence in compteur_octets.items()}

    return profil





def generer_profil_frequence_rsa(path):
    with open(path, 'rb') as file:
        contenu = file.read()

    # Chiffrement avec RSA
    rsa_key = RSA.generate(2048)  # Génération d'une clé RSA de 2048 bits
    rsa_cipher = PKCS1_OAEP.new(rsa_key)

    # Diviser le texte en morceaux plus petits pour le chiffrer avec RSA
    taille_max_bloc = rsa_key.size_in_bytes() - 2 * 64  # Taille maximale d'un bloc pour RSA OAEP
    rsa_encrypted_data = b''
    for i in range(0, len(contenu), taille_max_bloc):
        bloc = contenu[i:i + taille_max_bloc]
        rsa_encrypted_data += rsa_cipher.encrypt(bloc)
    print(rsa_encrypted_data)
    # Calculer la fréquence relative de chaque octet pour RSA
    compteur_octets_rsa = Counter(rsa_encrypted_data)
    # Calculer la fréquence relative de chaque octet RSA
    taille_texte = len(rsa_encrypted_data)
    profil_rsa = {octet: (occurrence / taille_texte) for octet, occurrence in compteur_octets_rsa.items()}
    return profil_rsa


def generer_profil_frequence_aes(path):
    with open(path, 'rb') as file:
        contenu = file.read()

    # Chiffrement avec AES
    aes_key = get_random_bytes(16)  # Génération d'une clé AES de 128 bits
    aes_cipher = AES.new(aes_key, AES.MODE_ECB)
    # Assurez-vous que le texte est correctement paddé pour AES
    contenu_padded = pad(contenu, AES.block_size)
    aes_encrypted_data = aes_cipher.encrypt(contenu_padded)
    print(aes_encrypted_data)
    # Calculer la fréquence relative de chaque octet pour AES
    compteur_octets_aes = Counter(aes_encrypted_data)
    # Calculer la fréquence relative de chaque octet AES
    taille_texte = len(aes_encrypted_data)
    profil_aes = {octet: (occurrence / taille_texte) for octet, occurrence in compteur_octets_aes.items()}
    return profil_aes


def comparer_profils(path1, path2):
    # Vérifiez si les chemins de fichier ne sont pas None
    if path1 is None or path2 is None:
        raise ValueError("Les chemins de fichier ne doivent pas être None")

    # Générer le profil de fréquence pour le premier fichier
    resultats = generer_profil_frequence(path1)

    # Récupérer les profils de fréquence des octets pour AES et RSA
    profil_aes = generer_profil_frequence_aes(path2)
    profil_rsa = generer_profil_frequence_rsa(path2)

    # Calculer les différences entre les profils de fréquence des octets des données chiffrées et les profils de référence
    differences_aes = sum(abs(resultats[i] - profil_aes.get(i, 0)) for i in resultats)
    differences_rsa = sum(abs(resultats[i] - profil_rsa.get(i, 0)) for i in resultats)

    # Comparer les différences pour déterminer l'algorithme utilisé
    if differences_aes > differences_rsa:
        return "AES"
    else:
        return "RSA"
