# coding=utf-8
import argparse
import ed25519 as ed
import gestionKeystore as gk

parser = argparse.ArgumentParser(description='Génération de clés')

parser.add_argument('-genKey', action='store_true',
                    help='génére une paire de clés publique et privée ')

parser.add_argument('-id', dest='id', required=True,
                    help='id de la personne')

parser.add_argument('-export', dest='typeKey',
                    help='-export [pub|sec], exporte la clé publique/privé')

parser.add_argument('-message', dest='message',
                    help='-message message, signe un message entré en arg grâce à une sk et pk')

parser.add_argument('-sign',  dest='sign',
                    help='-sign signature, vérifie si la signature entrée en arg est valide')


parser.add_argument('-gensign', action='store_true',
                    help='génére une signature')

args = parser.parse_args()

# Génération des clés
if args.genKey and args.id:
    # action à implémenter : appeler la fonction de géneration des clés qui stocke dans le keystore
    print "génération des clés pour " + args.id
    gk.genKeys(args.id)

# Affiche de clés
if args.typeKey and args.id:
    if args.typeKey == 'pub' or args.typeKey == 'sec':
        key = gk.getkey(args.id, args.typeKey)
        if key:
            print key
        else:
            print "Pas d'entrée trouvée pour " + args.id
    else:
        print args.typeKey + " est une mauvaise option pour l'argument -export"

# Génére la signature
if args.message and args.id and args.gensign:
    sk = gk.getkey(args.id, 'sec')
    pk = gk.genPkBrut(args.id)
    sign = ed.signature(args.message,sk, pk)

    if sign:
        print sign.encode('hex')


# Vérifie si la signature est valide
if args.sign and args.message and args.id:
    sk = gk.getkey(args.id, 'sec')
    pk = gk.genPkBrut(args.id)
    sign = str(args.sign).rstrip().decode('hex')
    try:
        ed.checkvalid(sign, args.message, pk)
        print "La signature est valide"
    except:
        print "La signature n'a pu être validée"

