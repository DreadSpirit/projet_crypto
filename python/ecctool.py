# coding=utf-8
import argparse
from os import urandom

import ed25519

# Déscription du scrit :
# On utilise un parser pour manipuler les arguments qu'on obtient via un terminal.
# C'est le point d'entrée de notre programme.
# La doc (plutot bien faite) se trouve ici : https://docs.python.org/3/library/argparse.html
# Pour utiliser le script, placez-vous dans le répertoire courant et taper :
#   python ecctool.py -h  pour voir les commandes disponibles
#   python -genkey -id alice pour tester

# on met dans la variable parser, la librairie argparse
parser = argparse.ArgumentParser(description='Géneration de clés ... A compléter')

# premier argument : genKey; Ne requière pas d'option; args.genKey = true si invoqué
parser.add_argument('-genKey', action='store_true',
                    help='génere une paire de clés publique et privée ')
# deuxième argument : id; Requière une option derrière: option requis pour executer la commande;
parser.add_argument('-id', dest='id', required=True,
                    help='id de la personne')

parser.add_argument('-export', dest='export',
                    help='-export [pub|sec], exporte la clé publique/privé')

args = parser.parse_args()

if args.genKey and args.id:
    # action à implémenter : appeler la fonction de géneration des clés qui stocke dans le keystore
    print "géneration des clés pour " + args.id

    keystore = open("keystore", "a")
    # géneration de la clé publique et de la clé privée

    sk = urandom(256 / 8).encode('hex')
    pk = ed25519.publickey(sk).encode('hex')

    # impression de la clé publique
    keystore.write("[pub]\n" + args.id + ":DSA-Ed25519-SHA-512:" + pk + "\n")

    # imporession de la clé privée
    keystore.write("[sec]\n" + args.id + ":DSA-Ed25519-SHA-512:" + sk + "\n")

if args.export and args.id:
    if args.export == 'pub' or args.export == 'sec':
        keystore = open("keystore", "r")
        # on cherche dans les clés publiques ou privés avec le bon id
        for ligne in keystore:
            if args.export in ligne:
                ligne_suiv = keystore.next()
                key = ligne_suiv.split(":")
                print key[2]
    else:
        print args.export + " est une mauvaise option pour l'argument -export"
