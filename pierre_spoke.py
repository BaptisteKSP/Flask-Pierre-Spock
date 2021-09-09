import random

tab = [] 
for x in range(44): #remplissage du tableau avec des valeurs nulles
    tab.append(0)

tab[1] = 2
tab[2] = 2
tab[3] = 1
tab[4] = 1
tab[10] = 1 # le "1" du nombre "10" correspond au chiffre choisis par le joueur et le "0" correpond au chiffre du bot
tab[12] = 2 # le résultat permet de savoir si le joueur à gagné ou non. "1" = win; "2" = lose
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
    nb = int(f"{nombreJ}{nombreB}") #j'assemble les 2 chiffres pour faire un nombre
    if(tab[nb] == 1): #nb en parametre permet de trouver le nombre 1 ou 2 qui va nous permettre de définir si le joueur à gagné.
        return({0 : "Le joueur a gagné"})
    else:
        return({1 : "Vous avez perdu contre le bot :'("})





    