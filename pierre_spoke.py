import random

tab = []
for x in range(44):
    tab.append(0)

tab[1] = 2
tab[2] = 2
tab[3] = 1
tab[4] = 1
tab[10] = 1
tab[12] = 2
tab[13] = 1
tab[14] = 1
tab[20] = 1
tab[21] = 2
tab[23] = 1
tab[24] = 2
tab[30] = 2
tab[31] = 1
tab[32] = 2
tab[34] = 1
tab[40] = 2
tab[41] = 1
tab[42] = 1
tab[43] = 2

def Begin(nombreJoueur):
    nombreJoueur = int(nombreJoueur)
    if(nombreJoueur < 0 or nombreJoueur > 4 or type(nombreJoueur) != int):
        return({0 : "Le nombre donné est incorrect"})

    #attaque = {0:"Pierre", 1:"Papier", 2:"Ciseaux", 3:"Lezard", 4:"Spock"}
    nombreBot = random.choice([elem for elem in range(5) if elem != nombreJoueur])
    return Result(nombreJoueur, nombreBot)

def Result(nombreJ, nombreB):
    nb = int(f"{nombreJ}{nombreB}")
    if(tab[nb] == 1):
        return({0 : "Le joueur a gagné"})
    else:
        return({1 : "Vous avez perdu contre le bot :'("})





    