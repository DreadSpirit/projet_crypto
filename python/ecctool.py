# coding=utf-8
import argparse

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
                    help='genère une paire de clés publique et privée ')
# deuxième argument : id; Requière une option derrière: option requis pour executer la commande;
parser.add_argument('-id', dest='id', required=True,
                    help='id de la personne')

args = parser.parse_args()

# affichage des arguments dans le terminal
print(args)

if args.genKey:
    # action à implémenter : appeler la fonction de géneration des clés qui stocke dans le keystore
    print "géneration de clés"

if args.id:
    # action à implémenter : enregistrer l'id pour cette paire de clé
    print "id : " + args.id
