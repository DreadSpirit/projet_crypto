# coding=utf-8
import argparse
from os import urandom

import ed25519
import gestionKeystore as gk

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

parser.add_argument('-export', dest='typeKey',
                    help='-export [pub|sec], exporte la clé publique/privé')

args = parser.parse_args()

# Géneration des clés
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

# Affiche de clés
if args.typeKey and args.id:
    if args.typeKey == 'pub' or args.typeKey == 'sec':
        key = gk.getkey(args.id, args.typeKey)
        if key:
            print key
        else:
            print "Pas d'entrée trouvé pour " + args.id
    else:
        print args.typeKey + " est une mauvaise option pour l'argument -export"
