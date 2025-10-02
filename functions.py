"""
Author: DURAND Guillian
Date: 02/10/2025
email: guillian.durand@cpe.fr
"""
from random import choice

def pick_word():
    fichier =  open("mots.txt")
    mots = fichier.readlines()
    return choice(mots).strip("\n")



def f_pendu(mot):
    lettres_set = set()
    affichage = [mot[0]] + [" _" for i in range(len(mot) - 1)]
    j = 0
    while "".join(affichage) != mot and j < 8:
        print("".join(affichage))
        guess = input("Devinez une lettre\n")
        while guess in lettres_set:
            guess = input(f"Vous avez deja deviné {guess} essayez une autre lettre.\n")
        lettres_set.add(guess)
        for i in range(len(mot)):
            if guess == mot[i]:
                affichage[i] = guess
        #print("".join(affichage))
        if guess not in mot:
            j =+ 1
            print(f"Vie restant: {8-j}")
    return 8 - j

def pendu():
    rejouer = "y"
    while rejouer == "y" or rejouer == "yes":
        score = f_pendu(pick_word())
        rejouer = input("Voulez vous rejouer une parite ? y/n\n")
        print(f"Votre plus haut score est {score} vie(s) restante(s)")

pendu()


#yun big boss uwu itadakimasu