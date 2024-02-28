grant connect,resource,dba to admin identified by adminpw ;
CONNECT admin/adminpw;

drop table fichiers_rep;
drop table fichiers_aff;
drop table fichiers_crypte;
drop table ransom_exts;
drop table extension ;
drop table ransom ; 
drop table commentaire ;
drop table users ;
drop table tools ;
drop SEQUENCE commentaire_seq;
drop SEQUENCE ransom_seq;
drop SEQUENCE fichiers_crypte_seq;
drop SEQUENCE fichiers_aff_seq;
drop SEQUENCE fichiers_rep_seq;
drop SEQUENCE extension_seq;
drop SEQUENCE tools_seq;



CREATE TABLE users (
    username VARCHAR2(20) PRIMARY KEY,
    Nom VARCHAR2(50),
    Prenom VARCHAR2(50),
    Email VARCHAR2(100),
    Password VARCHAR2(100),
    Type NUMBER(1) DEFAULT 1 CHECK (Type IN (0, 1)),
    Token VARCHAR2(100)
);


CREATE SEQUENCE commentaire_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE commentaire (
    Id_comment NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    objet VARCHAR2(100),
    Commentaire VARCHAR2(500),
    username VARCHAR2(20) REFERENCES users(username)
);

CREATE SEQUENCE ransom_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE ransom (
    Id_ransom NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nom VARCHAR2(100),
    Algorithme VARCHAR2(50),
    Taille_cle NUMBER(10),
    Annee DATE,
    Message VARCHAR2(500),
    Details VARCHAR2(500),
    pub_key NUMBER(1) CHECK (pub_key IN (0, 1))
);

CREATE SEQUENCE fichiers_aff_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE Fichiers_aff (
    Id_fichier_aff NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Emplacement VARCHAR2(200),
    Date_importation DATE,
    Etat NUMBER CHECK (Etat IN (0, 1)),
    username VARCHAR2(20) REFERENCES users(username),
    Id_ransom NUMBER REFERENCES ransom(Id_ransom)
);


CREATE SEQUENCE fichiers_crypte_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE Fichiers_crypte (
    Id_fichier_aff NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    NAME VARCHAR2(200),
    Date_IMPORTATION DATE,
    CLE VARCHAR2(1000),
    id_user VARCHAR2(20) references users(username)
);

CREATE SEQUENCE fichiers_rep_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE Fichiers_rep (
    Id_fichier_rep NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    NAME_FILE VARCHAR2(200),
    Date_reparation DATE,
    CLE VARCHAR2(1000),
    id_user VARCHAR2(20) references users(username)
);

CREATE SEQUENCE extension_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE extension (
    Id_extension NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nom VARCHAR2(50)
);

CREATE TABLE ransom_exts (
    Id_ransom NUMBER REFERENCES ransom(Id_ransom),
    Id_extension NUMBER REFERENCES extension(Id_extension),
    PRIMARY KEY (Id_ransom, Id_extension)
);

CREATE SEQUENCE tools_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE tools (
    Id_tool NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Name VARCHAR2(100),
    Description VARCHAR2(2000),
    Guide VARCHAR2(2000),
    Tool VARCHAR2(2000),
    made_by VARCHAR2(100)
);

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('777 Ransom',
        'Trend Micro Ransomware Decryptor is designed to decrypt files encrypted by 777 Ransom.',
        'https://www.nomoreransom.org/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('AES_NI Ransom',
        'Rakhni Decryptor is designed to decrypt files encrypted by AES_NI Ransom.',
        'https://www.nomoreransom.org/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip',
        'Kaspersky Lab'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Agent.iih Ransom',
        'Rakhni Decryptor is designed to decrypt files encrypted by Agent.iih Ransom.',
        'https://www.nomoreransom.org/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip',
        'Kaspersky Lab'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Akira Ransom',
        'Akira decryptor Decryptor is designed to decrypt files encrypted by Akira Ransom.',
        'https://www.nomoreransom.org/uploads/User%20Manual%20-%20Akira_Decryptor.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_akira64.exe',
        'Kisa'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Alcatraz Ransom',
        'Alcatraz Decryptor is designed to decrypt files encrypted by Alcatraz Ransom.',
        'https://www.nomoreransom.org/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_alcatrazlocker.exe',
        'Avast'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Alpha Ransom',
        'Alphadecrypter Decryptor is designed to decrypt files encrypted by Alpha Ransom.',
        'https://www.bleepingcomputer.com/download/alphadecrypter/dl/329/',
        'https://www.bleepingcomputer.com/download/alphadecrypter/dl/329/',
        'Bleeping Computer'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Amnesia Ransom',
        'Amnesia Decryptor is designed to decrypt files encrypted by Amnesia Ransom.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_amnesia.pdf',
        'https://decrypter.emsisoft.com/download/amnesia',
        'Emsisoft'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Annabelle Ransom',
        'BDAnnabelleDecryptTool Decryptor is designed to decrypt files encrypted by Annabelle Ransom.',
        'https://www.nomoreransom.org/uploads/Annabelle%20RANSOMWARE%20DECRYPTION%20TOOL.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDAnnabelleDecryptTool.exe',
        'Bitdefender'
       );

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Aura Ransom',
        'Rakhni Decryptor is designed to decrypt files encrypted by Aura Ransom.',
        'https://www.nomoreransom.org/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip',
        'Kaspersky Lab'
       );
commit ;

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Aurora Ransom', 'AuroraDecryptor est conçu pour déchiffrer les fichiers chiffrés par Aurora.',
        'https://www.bleepingcomputer.com/news/security/how-to-decrypt-the-aurora-ransomware-with-auroradecrypter/',
        'https://www.bleepingcomputer.com/download/auroradecrypter/dl/379/', 'Bleeping Computer ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('AutoIt Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par AutoIt.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('AutoLocky Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par AutoLocky.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Avaddon Ransom', 'BDAvaddonDecryptor est conçu pour déchiffrer les fichiers chiffrés par Avaddon.',
        'https://www.nomoreransom.org/uploads/Avaddon_documentation_new.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDAvaddonDecryptor.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Avest Ransom', 'Avest est conçu pour déchiffrer les fichiers chiffrés par Avest.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_avest.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/avest', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('BTCWare Ransom', 'BTCWare est conçu pour déchiffrer les fichiers chiffrés par BTCWare.',
        '/uploads/Avast_how-to-guide.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_btcware.exe',
        'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Babuk Ransom', 'Babuk ransomware est conçu pour déchiffrer les fichiers chiffrés par Babuk.',
        'https://www.nomoreransom.org/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_babuk.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('BadBlock Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par BadBlock.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('BarRax Ransom', 'BarRax est conçu pour déchiffrer les fichiers chiffrés par BarRax.', '/uploads/barrax.pdf',
        'https://blog.checkpoint.com/wp-content/uploads/2017/03/BarRaxDecryptor.zip', 'Check Point ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Bart Ransom', 'Bart est conçu pour
déchiffrer les fichiers chiffrés par Bart.', '/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_bart.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Bianlian Ransom', 'Bianlian est conçu pour déchiffrer les fichiers chiffrés par Bianlian.',
        '/uploads/Bianlian_Decryptor.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_bianlian.exe',
        'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('BigBobRoss Ransom', 'Bigbobross fix est conçu pour déchiffrer les fichiers chiffrés par BigBobRoss.',
        'https://www.nomoreransom.org/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_bigbobross.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Bitcryptor Ransom', 'Coinvault est
conçu pour déchiffrer les fichiers chiffrés par Bitcryptor.', '/uploads/CoinVault-decrypt-howto.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/CoinVaultDecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CERBER V1 Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par CERBER V1.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Chaos Ransom', 'Chaos est conçu pour déchiffrer les fichiers chiffrés par Chaos.',
        '/uploads/UserManualChaosDecryptor.pdf',
        'https://github.com/Truesec/TSDecryptors/releases/download/v1.0.0.0/Truesec.Decryptors-1.0.0.0.zip',
        'Truesec ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CheckMail7 Ransom', 'Checkmail7 est conçu pour déchiffrer les fichiers chiffrés par CheckMail7.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_checkmail7.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/checkmail7', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Chernolocker Ransom', 'Chernolocker est conçu pour déchiffrer les fichiers chiffrés par Chernolocker.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_chernolocker.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/chernolocker', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Chimera Ransom', 'Rakhni est conçu
pour déchiffrer les fichiers chiffrés par Chimera.', '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Coinvault Ransom', 'Coinvault est conçu pour déchiffrer les fichiers chiffrés par Coinvault.',
        '/uploads/CoinVault-decrypt-howto.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/CoinVaultDecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Cry128 Ransom', 'Cry128 est conçu pour déchiffrer les fichiers chiffrés par Cry128.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_cry128.pdf',
        'https://decrypter.emsisoft.com/download/cry128', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Cry9 Ransom', 'Cry9 est conçu pour
déchiffrer les fichiers chiffrés par Cry9.', 'https://decrypter.emsisoft.com/howtos/emsisoft_howto_cry9.pdf',
        'https://decrypter.emsisoft.com/download/cry9', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryCryptor Ransom', 'CryDecryptor est conçu pour déchiffrer les fichiers chiffrés par CryCryptor.',
        '/uploads/CryDecryptor Tool by ESET.pdf',
        'https://github.com/eset/cry-decryptor/releases/download/v1.0/CryDecryptor.apk', 'ESET ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CrySIS Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par CrySIS.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Cryakl Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Cryakl.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Crybola Ransom', 'Rannoh est conçu
pour déchiffrer les fichiers chiffrés par Crybola.', '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Crypt32 Ransom', 'Crypt32 est conçu pour déchiffrer les fichiers chiffrés par Crypt32.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_crypt32.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/crypt32', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Crypt888 Ransom', 'Crypt888 est conçu pour déchiffrer les fichiers chiffrés par Crypt888.',
        '/uploads/Avast_how-to-guide.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_crypt888.exe',
        'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptON Ransom', 'Crypton est conçu pour déchiffrer les fichiers chiffrés par CryptON.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_crypton.pdf',
        'https://decrypter.emsisoft.com/download/crypton', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptXXX V1 Ransom', 'Rannoh est conçu pour déchiffrer les fichiers chiffrés par CryptXXX V1.',
        '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptXXX V2 Ransom', 'Rannoh est conçu pour déchiffrer les fichiers chiffrés par CryptXXX V2.',
        '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptXXX V3 Ransom', 'Rannoh est conçu pour déchiffrer les fichiers chiffrés par CryptXXX V3.',
        '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptXXX V4 Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par CryptXXX V4.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptXXX V5 Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par CryptXXX V5.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('CryptoMix Ransom', 'CryptoMix est conçu pour déchiffrer les fichiers chiffrés par CryptoMix.', '#',
        'https://nomoreransom.cert.pl/static/cryptomix_decryptor.exe', 'CERT-PL ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Cryptokluchen Ransom', 'Rakhni est
conçu pour déchiffrer les fichiers chiffrés par Cryptokluchen.', '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Cyborg Ransom', 'Cyborg est conçu pour déchiffrer les fichiers chiffrés par Cyborg.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_cyborg.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/cyborg', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('DXXD Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par DXXD.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Daivol ransomware Ransom', 'Daivol
ransomware est conçu pour déchiffrer les fichiers chiffrés par Daivol ransomware.',
        'https://www.emsisoft.com/ransomware-decryption-tools/howtos/emsisoft_howto_diavol.pdf   ',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/diavol', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Damage Ransom', 'Damage est conçu pour déchiffrer les fichiers chiffrés par Damage.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_damage.pdf',
        'https://decrypter.emsisoft.com/download/damage', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Darkside Ransom', 'Darkside est conçu pour déchiffrer les fichiers chiffrés par Darkside.',
        '/uploads/DarkSide RANSOMWARE DECRYPTION TOOL.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDDarkSideDecryptor.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Democry Ransom', 'Rakhni est conçu
pour déchiffrer les fichiers chiffrés par Democry.', '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Derialock Ransom', 'StupidDecryptor est conçu pour déchiffrer les fichiers chiffrés par Derialock.',
        'https://www.bleepingcomputer.com/ransomware/decryptor/how-to-decrypt-the-stupid-ransomware-family-with-stupiddecrypter/',
        'https://www.bleepingcomputer.com/download/stupiddecryptor/dl/351/', 'Bleeping Computer ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Dharma Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Dharma.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('DragonCyber Ransom', 'Jigsaw est conçu pour déchiffrer les fichiers chiffrés par DragonCyber.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_jigsaw.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/jigsaw', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('ElvisPresley  Ransom', 'Jigsaw est
conçu pour déchiffrer les fichiers chiffrés par ElvisPresley .',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_jigsaw.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/jigsaw', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('EncrypTile Ransom', 'EncrypTile est conçu pour déchiffrer les fichiers chiffrés par EncrypTile.',
        '/uploads/EncrypTile.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_encryptile.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Everbe 1.0 Ransom', 'InsaneCryptDecrypter est conçu pour déchiffrer les fichiers chiffrés par Everbe 1.0.',
        'https://www.bleepingcomputer.com/ransomware/decryptor/how-to-decrypt-the-insanecrypt-or-everbe-1-family-of-ransomware/',
        'https://www.bleepingcomputer.com/download/insanecrypt-desucrypt-decrypter/dl/369/', 'Bleeping Computer ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('FONIX Ransom', 'FONIX est conçu pour déchiffrer les fichiers chiffrés par FONIX.',
        '/uploads/FONIX RANSOMWARE DECRYPTION TOOL.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDFONIXDecryptor.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('FenixLocker Ransom', 'FenixLocker est conçu pour déchiffrer les fichiers chiffrés par FenixLocker.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_fenixlocker.pdf',
        'https://decrypter.emsisoft.com/download/fenixlocker', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('FilesLocker v1 and v2 Ransom',
        'FilesLockerDecrypter est conçu pour déchiffrer les fichiers chiffrés par FilesLocker v1 and v2.',
        'https://www.bleepingcomputer.com/ransomware/decryptor/how-to-decrypt-the-fileslocker-ransomware-with-fileslockerdecrypter/',
        'https://www.bleepingcomputer.com/download/fileslockerdecrypter/dl/378/', 'Bleeping Computer ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('FortuneCrypt Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par FortuneCrypt.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Fury Ransom', 'Rannoh est conçu pour déchiffrer les fichiers chiffrés par Fury.',
        '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('GalactiCryper Ransom', 'GalactiCryper est conçu pour déchiffrer les fichiers chiffrés par GalactiCryper.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_galacticrypter.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/galacticrypter', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('GandCrab (V1, V4 and V5 up to V5.2 versions) Ransom', 'BDGandCrabDecryptTool est conçu pour déchiffrer les fichiers chiffrés par GandCrab
(V1, V4 and V5 up to V5.2 versions).', '/uploads/GANDCRAB RANSOMWARE DECRYPTION TOOL (002).pdf',
        'https://download.bitdefender.com/am/malware_removal/BDGandCrabDecryptTool.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('GetCrypt Ransom', ' est conçu pour
déchiffrer les fichiers chiffrés par GetCrypt.', 'https://decrypter.emsisoft.com/howtos/emsisoft_howto_getcrypt.pdf',
        'https://www.emsisoft.com/decrypter/download/getcrypt', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Globe Ransom', 'Globe est conçu pour déchiffrer les fichiers chiffrés par Globe.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_globe.pdf',
        'https://decrypter.emsisoft.com/download/globe', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Globe/Purge Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par Globe/Purge.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Globe2 Ransom', 'Globe2 est conçu pour déchiffrer les fichiers chiffrés par Globe2.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_globe2.pdf',
        'https://decrypter.emsisoft.com/download/globe2', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Globe3 Ransom', 'Globe3 est conçu pour déchiffrer les fichiers chiffrés par Globe3.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_globe3.pdf',
        'https://decrypter.emsisoft.com/download/globe3', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('GlobeImposter Ransom', 'GlobeImposter est conçu pour déchiffrer les fichiers chiffrés par GlobeImposter.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_globeimposter.pdf',
        'https://decrypter.emsisoft.com/download/globeimposter', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('GoGoogle Ransom', 'GoGoogle est conçu pour déchiffrer les fichiers chiffrés par GoGoogle.',
        '/uploads/StepsForDecryptionGoGoogle.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDGoGoogleDecryptor.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Gomasom Ransom', 'Gomasom est conçu pour déchiffrer les fichiers chiffrés par Gomasom.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_gomasom.pdf',
        'https://decrypter.emsisoft.com/download/gomasom', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('HKCrypt Ransom', 'HKCrypt est conçu pour déchiffrer les fichiers chiffrés par HKCrypt.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_hkcrypt.pdf',
        'https://decrypter.emsisoft.com/download/hkcrypt', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Hakbit Ransom', 'Hakbit est conçu pour déchiffrer les fichiers chiffrés par Hakbit.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_hakbit.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/hakbit', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('HermeticRansom Ransom', 'HermeticRansom est conçu pour déchiffrer les fichiers chiffrés par HermeticRansom.',
        'https://www.nomoreransom.org/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_hermeticransom.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('HiddenTear Ransom', 'HiddenTear est conçu pour déchiffrer les fichiers chiffrés par HiddenTear.',
        '/uploads/Avast_how-to-guide.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_hiddentear.exe',
        'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('HildaCrypt Ransom', 'hildacrypt est conçu pour déchiffrer les fichiers chiffrés par HildaCrypt.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_hildacrypt.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/hildacrypt', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Hive (v1 to v4) Ransom', 'Hive (v1
to v4) est conçu pour déchiffrer les fichiers chiffrés par Hive (v1 to v4).',
        '/uploads/Hive_Ransomware_Integrated_Decryption_Tool_User_Manual(ENG).pdf',
        'https://seed.kisa.or.kr/kisa/Board/133/detailView.do', 'Kisa ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Iams00rry Ransom', 'Iams00rry est conçu pour déchiffrer les fichiers chiffrés par Iams00rry.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_ims00rry.pdf',
        'https://www.emsisoft.com/decrypter/ims00rry', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('InsaneCrypt  Ransom', 'InsaneCryptDecrypter est conçu pour déchiffrer les fichiers chiffrés par InsaneCrypt .',
        'https://www.bleepingcomputer.com/ransomware/decryptor/how-to-decrypt-the-insanecrypt-or-everbe-1-family-of-ransomware/',
        'https://www.bleepingcomputer.com/download/insanecrypt-desucrypt-decrypter/dl/369/', 'Bleeping Computer ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Iwanttits Ransom', 'Ransomwared est conçu pour déchiffrer les fichiers chiffrés par Iwanttits.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_ransomwared.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/ransomwared', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('JSWorm 2.0 Ransom', 'JS WORM 2.0 est conçu pour déchiffrer les fichiers chiffrés par JSWorm 2.0.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_jsworm2.pdf',
        'https://www.emsisoft.com/decrypter/download/jsworm-20', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('JSWorm 4.0 Ransom', 'JSWorm 4.0 est conçu pour déchiffrer les fichiers chiffrés par JSWorm 4.0.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_jsworm4.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/jsworm-40', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Jaff Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Jaff.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('JavaLocker Ransom', 'JavaLocker est conçu pour déchiffrer les fichiers chiffrés par JavaLocker.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_javalocker.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/javalocker', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Jigsaw Ransom', 'Jigsaw est conçu pour déchiffrer les fichiers chiffrés par Jigsaw.',
        '/uploads/JigsawDecryption_how-to-guide.pdf',
        'https://blog.checkpoint.com/wp-content/uploads/2016/07/JPS_release.zip', 'Check Point ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Judge Ransom', 'Judge est conçu pour déchiffrer les fichiers chiffrés par Judge.',
        'https://mdsassets.blob.core.windows.net/downloads/JudgeHowToGuide.pdf',
        'https://mdsassets.blob.core.windows.net/downloads/Judge-Decryptor.exe', 'Tesorion ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Kokokrypt Ransom', 'KokoKrypt est conçu pour déchiffrer les fichiers chiffrés par Kokokrypt.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_kokokrypt.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/kokokrypt', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('LECHIFFRE Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par LECHIFFRE.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('LambdaLocker Ransom', 'LambdaLocker est conçu pour déchiffrer les fichiers chiffrés par LambdaLocker.',
        '/uploads/Avast_how-to-guide.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_lambdalocker.exe',
        'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Lamer Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Lamer.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Linux.Encoder.1 Ransom',
        'Linux.Encoder.1 est conçu pour déchiffrer les fichiers chiffrés par Linux.Encoder.1.',
        '/uploads/Linux-encoder-1.pdf',
        'https://labs.bitdefender.com/wp-content/plugins/download-monitor/download.php?id=Decrypter_0-1.3.zip',
        'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Linux.Encoder.3 Ransom',
        'Linux.Encoder.3 est conçu pour déchiffrer les fichiers chiffrés par Linux.Encoder.3.',
        '/uploads/Linux-encoder-3.pdf',
        'https://labs.bitdefender.com/wp-content/plugins/download-monitor/download.php?id=encoder_3_decrypter.zip',
        'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('LockFile Ransom', 'LockFile ransomware est conçu pour déchiffrer les fichiers chiffrés par LockFile.',
        'https://decoded.avast.io/threatintel/decryptor-for-atomsilo-and-lockfile-ransomware',
        'https://files.avast.com/files/decryptor/avast_decryptor_atomsilo.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('LockerGoga Ransom', 'LockerGoga est conçu pour déchiffrer les fichiers chiffrés par LockerGoga.',
        '/uploads/LockerGoga-Decrypt-Doc.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDLockerGogaDecryptTool.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Loocipher Ransom', 'Loocipher Emsisoft est conçu pour déchiffrer les fichiers chiffrés par Loocipher.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_loocipher.pdf',
        'https://www.emsisoft.com/decrypter/loocipher', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Lorenz Ransom', 'Lorenz est conçu pour déchiffrer les fichiers chiffrés par Lorenz.',
        'https://mdsassets.blob.core.windows.net/downloads/LorenzHowTo.pdf',
        'https://mdsassets.blob.core.windows.net/downloads/Lorenz-Decryptor.exe', 'Tesorion ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Lortok Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Lortok.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('MacRansom Ransom', 'MacRansom est conçu pour déchiffrer les fichiers chiffrés par MacRansom.',
        '/uploads/MacRansom.pdf',
        'https://esupport.trendmicro.com/media/13801530/Trend%20Micro%20Ransomware%20Decryptor_V1.0.1.zip',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('MafiaWare666 Ransom', 'MafiaWare666 est conçu pour déchiffrer les fichiers chiffrés par MafiaWare666.',
        '/uploads/UserManualAvastMafiaWare666Decryptor.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_mafiaware666.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Magniber Ransom', 'Magniber est conçu pour déchiffrer les fichiers chiffrés par Magniber.',
        '/uploads/Magniber_decryption_tool_user_manual.pdf', 'https://seed.kisa.or.kr/kisa/Board/56/detailView.do',
        'Kisa ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Mapo Ransom', 'Mapo est conçu pour
déchiffrer les fichiers chiffrés par Mapo.',
        'https://www.cert.pl/en/news/single/free-decryption-tool-for-mapo-ransomware/',
        'https://nomoreransom.cert.pl/static/mapo_decryptor.exe', 'CERT-PL ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Marlboro Ransom', 'Marlboro est conçu pour déchiffrer les fichiers chiffrés par Marlboro.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_marlboro.pdf',
        'https://decrypter.emsisoft.com/download/marlboro', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Marsjoke aka Polyglot Ransom',
        'Rannoh est conçu pour déchiffrer les fichiers chiffrés par Marsjoke aka Polyglot.',
        '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Maze / Sekhmet / Egregor Ransom',
        'Maze / Sekhmet / Egregor est conçu pour déchiffrer les fichiers chiffrés par Maze / Sekhmet / Egregor.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('MegaCortex Ransom', 'MegaCortex est conçu pour déchiffrer les fichiers chiffrés par MegaCortex.',
        '/uploads/UserManualMegaCortexDecryptor.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDMegaCortexDecryptTool.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('MegaLocker Ransom', 'MegaLocker est conçu pour déchiffrer les fichiers chiffrés par MegaLocker.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_megalocker.pdf',
        'https://www.emsisoft.com/decrypter/download/megalocker', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Merry X-Mas Ransom', 'Merry X-Mas est conçu pour déchiffrer les fichiers chiffrés par Merry X-Mas.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_mrcr.pdf', 'https://decrypter.emsisoft.com/download/mrcr',
        'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('MirCop Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par MirCop.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Mira Ransom', 'Mira est conçu pour
déchiffrer les fichiers chiffrés par Mira.', 'https://www.f-secure.com/en/web/labs_global/mira-decryptor',
        'https://download.f-secure.com/support/tools/Mira-decryptor/Mira%20Ransomware%20Decryptor.zip', 'F-Secure ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Mole Ransom', 'Mole est conçu pour
déchiffrer les fichiers chiffrés par Mole.', '#', 'https://nomoreransom.cert.pl/static/mole_decryptor.exe', 'CERT-PL ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Muhstik Ransom', 'muhstik  est conçu pour déchiffrer les fichiers chiffrés par Muhstik.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_muhstik.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/muhstik', 'Emsisoft ');

INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Nemty Ransom', 'Nemty est conçu pour déchiffrer les fichiers chiffrés par Nemty.',
        'https://mdsassets.blob.core.windows.net/downloads/NemtyHowToGuide.pdf',
        'https://mdsassets.blob.core.windows.net/downloads/NemtyDecryptor.exe', 'Tesorion ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Nemucod Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par Nemucod.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('NemucodAES Ransom', 'NemucodAES est conçu pour déchiffrer les fichiers chiffrés par NemucodAES.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_nemucodaes.pdf',
        'https://decrypter.emsisoft.com/download/nemucodaes', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Nmoreira Ransom', 'Nmoreira est conçu pour déchiffrer les fichiers chiffrés par Nmoreira.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_nmoreira.pdf',
        'https://decrypter.emsisoft.com/download/nmoreira', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('NoWay Ransom', 'NoWay est conçu pour déchiffrer les fichiers chiffrés par NoWay.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_noway.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/noway', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Noobcrypt Ransom', 'Noobcrypt est conçu pour déchiffrer les fichiers chiffrés par Noobcrypt.',
        '/uploads/Avast_how-to-guide.pdf', 'https://files.avast.com/files/decryptor/avast_decryptor_noobcrypt.exe',
        'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Onyx2 Ransom', 'Onyx2 est conçu pour déchiffrer les fichiers chiffrés par Onyx2.',
        '/uploads/UserManualOnyx2Decryptor.pdf',
        'https://github.com/Truesec/TSDecryptors/releases/download/v1.0.0.0/Truesec.Decryptors-1.0.0.0.zip',
        'Truesec ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Ouroboros Ransom', 'Ouroboros est conçu pour déchiffrer les fichiers chiffrés par Ouroboros.',
        'https://labs.bitdefender.com/2019/10/ouroboros-ransomware-decryption-tool/',
        'https://download.bitdefender.com/am/malware_removal/BDOuroborosDecryptTool.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Ozozalocker Ransom', 'Ozozalocker est conçu pour déchiffrer les fichiers chiffrés par Ozozalocker.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_ozozalocker.pdf',
        'https://decrypter.emsisoft.com/download/ozozalocker', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Paradise Ransom', 'Paradise est conçu pour déchiffrer les fichiers chiffrés par Paradise.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_paradise.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/paradise', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Pewcrypt Ransom', 'Pewcrypt est conçu pour déchiffrer les fichiers chiffrés par Pewcrypt.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_pewcrypt.pdf',
        'https://decrypter.emsisoft.com/download/pewcrypt', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Philadelphia Ransom', 'Philadelphia est conçu pour déchiffrer les fichiers chiffrés par Philadelphia.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_philadelphia.pdf',
        'https://decrypter.emsisoft.com/download/philadelphia', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Planetary Ransom', 'Planetary est conçu pour déchiffrer les fichiers chiffrés par Planetary.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_planetary.pdf',
        'https://decrypter.emsisoft.com/download/planetary', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Pletor Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Pletor.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Plutocrypt Ransom', 'Plutocrypt est conçu pour déchiffrer les fichiers chiffrés par Plutocrypt.',
        '/uploads/User Manual - PlutoCrypt_Decryptor.pdf',
        'https://github.com/prodaft/malware-ioc/raw/master/PlutoCrypt/plutocrypt_decryptor.exe', 'Prodaft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Popcorn Ransom', 'Popcorn est conçu pour déchiffrer les fichiers chiffrés par Popcorn.',
        'https://www.elevenpaths.com/innovation-labs/technologies/recover-popcorn',
        'https://www.elevenpaths.com/innovation-labs/technologies/recover-popcorn#eulaModal', 'Elevenpaths ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Professeur Ransom', 'Jigsaw est conçu pour déchiffrer les fichiers chiffrés par Professeur.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_jigsaw.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/jigsaw', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Prometheus Ransom', 'Prometheus est conçu pour déchiffrer les fichiers chiffrés par Prometheus.',
        '/uploads/Prometheus - How to Guide.pdf',
        'https://github.com/cycraft-corp/Prometheus-Decryptor/releases/download/1.2/prometheus_decryptor.zip',
        'Cycraft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Puma Ransom', 'Puma est conçu pour
déchiffrer les fichiers chiffrés par Puma.', 'https://decrypter.emsisoft.com/howtos/emsisoft_howto_stoppuma.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/stop-puma', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Pylocky Ransom', 'pylocky_decryptor est conçu pour déchiffrer les fichiers chiffrés par Pylocky.',
        'https://blog.talosintelligence.com/2019/01/pylocky-unlocked-cisco-talos-releases.html',
        'https://github.com/Cisco-Talos/pylocky_decryptor', 'CISCO ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('RAGNAROK Ransom', 'RAGNAROK est conçu pour déchiffrer les fichiers chiffrés par RAGNAROK.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_ragnarok.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/ragnarok', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('REvil/Sodinokibi Ransom',
        'REvil/Sodinokibi est conçu pour déchiffrer les fichiers chiffrés par REvil/Sodinokibi.',
        '/uploads/REvil_documentation.pdf', 'http://download.bitdefender.com/am/malware_removal/BDREvilDecryptor.exe',
        'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Ragnar Ransom', 'Ragnar Decryptor est conçu pour déchiffrer les fichiers chiffrés par Ragnar.',
        '/uploads/User Manual - Ragnar_Decryptor.pdf',
        'https://seed.kisa.or.kr/async/MultiFile/download.do?FS_KEYNO=FS_0000000415&amp;MNK=MN_0000001279', 'Kisa ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Rakhni Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Rakhni.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('RanHassan Ransom', 'RanHassan est conçu pour déchiffrer les fichiers chiffrés par RanHassan.',
        '/uploads/UserManualRanHassanDecryptor.pdf',
        'https://download.bitdefender.com/am/malware_removal/BDRanHassanDecryptTool.exe', 'Bitdefender ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Rannoh Ransom', 'Rannoh est conçu pour déchiffrer les fichiers chiffrés par Rannoh.',
        '/uploads/RannohDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Ransomwared Ransom', 'Ransomwared est conçu pour déchiffrer les fichiers chiffrés par Ransomwared.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_ransomwared.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/ransomwared', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('RedRum Ransom', 'RedRum est conçu pour déchiffrer les fichiers chiffrés par RedRum.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_redrum.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/redrum', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Rotor Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Rotor.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('SNSLocker Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par SNSLocker.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Shade Ransom', 'Shade est conçu pour déchiffrer les fichiers chiffrés par Shade.',
        'https://support.kaspersky.com/13059?_ga=2.27044596.858346383.1588243768-313061628.1558015910#block1',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/ShadeDecryptor.zip?_ga=2.161492788.960080222.1588573244-1427278170.1570299536',
        'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('SimpleLocker  Ransom', 'Simplelocker est conçu pour déchiffrer les fichiers chiffrés par SimpleLocker .',
        '/uploads/SImplelocker_decryptiontool_user_manual.pdf', 'https://seed.kisa.or.kr/kisa/Board/57/detailView.do',
        'Kisa ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Simplocker Ransom', 'Simplelocker est conçu pour déchiffrer les fichiers chiffrés par Simplocker.',
        '/uploads/ESET_Simplocker_Decryption tool.pdf',
        'https://download.eset.com/com/eset/tools/decryptors/simplocker/latest/eset-simplocker-decryptor.apk', 'ESET ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Solidbit Ransom', 'Solidbit est conçu pour déchiffrer les fichiers chiffrés par Solidbit.',
        '/uploads/UserManualSolidbitDecryptor.pdf',
        'https://github.com/Truesec/TSDecryptors/releases/download/v1.0.0.0/Truesec.Decryptors-1.0.0.0.zip',
        'Truesec ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('SpartCrypt Ransom', 'SpartCrypt est conçu pour déchiffrer les fichiers chiffrés par SpartCrypt.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_spartcrypt.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/spartcrypt', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Stampado Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par Stampado.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('SynAck Ransom', 'SynAck est conçu pour déchiffrer les fichiers chiffrés par SynAck.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_synack.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/synack', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Syrk Ransom', 'Syrk est conçu pour
déchiffrer les fichiers chiffrés par Syrk.', 'https://decrypter.emsisoft.com/howtos/emsisoft_howto_syrk.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/syrk', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('TargetCompany Ransom', 'TargetCompany est conçu pour déchiffrer les fichiers chiffrés par TargetCompany.',
        'https://www.nomoreransom.org/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_targetcompany64.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Tarrak ransomware Ransom', 'Tarrak
ransomware 32-bit est conçu pour déchiffrer les fichiers chiffrés par Tarrak ransomware.',
        'https://www.nomoreransom.org/uploads/Avast_how-to-guide.pdf',
        'https://files.avast.com/files/decryptor/avast_decryptor_tarrak.exe', 'Avast ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Teamxrat/Xpan Ransom',
        'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par Teamxrat/Xpan.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('TeslaCrypt V1 Ransom',
        'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par TeslaCrypt V1.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('TeslaCrypt V2 Ransom',
        'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par TeslaCrypt V2.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('TeslaCrypt V3 Ransom', 'Rakhni est
conçu pour déchiffrer les fichiers chiffrés par TeslaCrypt V3.', '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('TeslaCrypt V4 Ransom', 'Rakhni est
conçu pour déchiffrer les fichiers chiffrés par TeslaCrypt V4.', '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Thanatos Ransom', 'Thanatos est conçu pour déchiffrer les fichiers chiffrés par Thanatos.',
        'https://talosintelligence.com/thanatos_decryptor', 'https://github.com/Cisco-Talos/ThanatosDecryptor',
        'CISCO ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('ThunderX Ransom', 'ThunderX est conçu pour déchiffrer les fichiers chiffrés par ThunderX.',
        '/uploads/ThunderXHowToGuide.pdf', 'https://mdsassets.blob.core.windows.net/downloads/ThunderX-Decryptor.exe',
        'Tesorion ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Trustezeb Ransom', 'Trustezeb.A est conçu pour déchiffrer les fichiers chiffrés par Trustezeb.',
        '/uploads/kb7083_TrustezebA.PDF',
        'https://download.eset.com/com/eset/tools/decryptors/trustezeb_a/latest/esettrustezebadecoder.exe', 'ESET ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('TurkStatic Ransom', 'TurkStatic est conçu pour déchiffrer les fichiers chiffrés par TurkStatic.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_turkstatik.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/turkstatik', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('VCRYPTOR Ransom', 'VCRYPTOR est conçu pour déchiffrer les fichiers chiffrés par VCRYPTOR.',
        '/uploads/VCrypt_how-to_guide.pdf', 'https://www.elevenpaths.com/downloads/vcrypt_decryptor.zip',
        'Elevenpaths ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('WannaCryFake Ransom', 'WannaCryFake est conçu pour déchiffrer les fichiers chiffrés par WannaCryFake.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_syrk.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/wannacryfake', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Wildfire Ransom', 'Wildfire est conçu pour déchiffrer les fichiers chiffrés par Wildfire.',
        '/uploads/WildFire_Decryptor_how_to.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/RU/WildfireDecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('XData Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par XData.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('XORBAT Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par XORBAT.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('XORIST Ransom', 'Trend Micro Ransomware est conçu pour déchiffrer les fichiers chiffrés par XORIST.',
        '/uploads/TrendMicro_how-to_guide.pdf',
        'https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d',
        'Trend Micro ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Yatron Ransom', 'Rakhni est conçu pour déchiffrer les fichiers chiffrés par Yatron.',
        '/uploads/RakhniDecryptor_how-to_guide.pdf',
        'https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip', 'Kaspersky Lab ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('ZQ Ransom', 'ZQ est conçu pour déchiffrer les fichiers chiffrés par ZQ.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_zq.pdf', 'https://www.emsisoft.com/decrypter/download/zq',
        'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('ZeroFucks Ransom', 'ZeroFucks est conçu pour déchiffrer les fichiers chiffrés par ZeroFucks.',
        'https://www.emsisoft.com/decrypter/howtos/emsisoft_howto_zerofucks.pdf',
        'https://www.emsisoft.com/decrypter/zerofucks', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Ziggy Ransom', 'Ziggy est conçu pour déchiffrer les fichiers chiffrés par Ziggy.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_ziggy.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/ziggy', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('Zorab Ransom', 'Zorab est conçu pour déchiffrer les fichiers chiffrés par Zorab.',
        'https://decrypter.emsisoft.com/howtos/emsisoft_howto_zorab.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/zorab', 'Emsisoft ');


INSERT INTO tools (Name, Description, Guide, Tool, made_by)
VALUES ('djvu Ransom', 'djvu est conçu pour
déchiffrer les fichiers chiffrés par djvu.', 'https://decrypter.emsisoft.com/howtos/emsisoft_howto_stopdjvu.pdf',
        'https://www.emsisoft.com/ransomware-decryption-tools/download/stop-djvu', 'Emsisoft ');
commit;



