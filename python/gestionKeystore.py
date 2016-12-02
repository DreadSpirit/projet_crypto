# coding=utf-8

# Retourne la cle privé ou publique pour une entrée
def getkey(id, type):
    keystore = open("keystore", "r")
    for ligne in keystore:
        if type in ligne:
            ligne_suiv = keystore.next()
            key = ligne_suiv.split(":")
            if key[0] == id:
                return key[2]
