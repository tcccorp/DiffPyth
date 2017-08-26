# -*- coding: utf-8 -*-
# diff entre 2 fichiers .  On parse le premier ligne par ligne . On recherche chaque ligne dans le deuxieme
# si c'est trouvé, on supprime la ligne dans le tableau du 2eme
# si ce n'est pas trouvé, on le met dans un fichier .
# a la fin, on aura un fichier avec ce qui est en plus dans le 1er et un uatre avec ce qui est en plus dans le 2eme




from optparse import OptionParser

def main():
    enPlus=[]
    parser = OptionParser(usage="usage: %prog fichier1 fichier2",version="%prog 1.0")
    (options, args) = parser.parse_args()

    if len(args) != 2:
        parser.error("Vous devez rentrer les 2 fichiers a comparer")

#ouverture du premier fichier
    fichierA = open(args[0],"r").read().split("\n")
#ouverture du deuxieme
    fichierB = open(args[1],"r").read().split("\n")
    for lineFichierA in fichierA:
        if lineFichierA in fichierB:
            fichierB.remove(lineFichierA)
        else:
            enPlus.append(lineFichierA)
    print ("Il y a " + str(len(enPlus)) +" éléments en plus dans le fichier A et " + str(len(fichierB))+ " dans le fichier B")
    open ("enplus.txt","w").write("\n".join(enPlus))
    open ("reste.txt","w").write("\n".join(fichierB))
		
if __name__ == '__main__':
    main()
