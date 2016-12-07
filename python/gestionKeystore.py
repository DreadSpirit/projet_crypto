# coding=utf-8

from os import urandom

import ed25519


# Retourne la cle privé ou publique pour une entrée
def getkey(id, type):
    keystore = open("keystore", "r")
    for ligne in keystore:
        if type in ligne:
            ligne_suiv = keystore.next()
            key = ligne_suiv.split(":")
            if key[0] == id:
                return key[2]


def genKeys(id):
    keystore = open("keystore", "a")
    # génération de la clé publique et de la clé privée

    sk = urandom(256 / 8).encode('hex')
    pk = ed25519.publickey(sk).encode('hex')

    # impression de la clé publique
    keystore.write("[pub]\n" + id + ":DSA-Ed25519-SHA-512:" + pk + "\n")

    # imporession de la clé privée
    keystore.write("[sec]\n" + id + ":DSA-Ed25519-SHA-512:" + sk + "\n")

def genPkBrut(id):
    sk = getkey(id,'sec')
    pk = ed25519.publickey(sk)
    return pk
