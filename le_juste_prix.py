from random import randint

nombre_a_trouver= randint(1,1000)

print("Bienvenue dans l'émission LE JUSTE PRIX !")
print("C'est très simple ! Vous devez troouver le prix d'un article")
print("Ce prix est compris entre 1€ et 1000€ ")
print("Bonne chance  ")
for nb_essais in range(1,11):
    print("Il vous reste", 11-nb_essais,"essai(s)")
    nombre = int(input("Entrez un prix : "))
    if nb_essais !=10:
        if nombre < nombre_a_trouver:
            print("C'est plus")
        elif nombre > nombre_a_trouver:
            print("C'est moins")
        else:
            break
if nombre != nombre_a_trouver:
    print("C'est perdu ! Le juste prix était",nombre_a_trouver,"!!!")
else:
    print("C'est gagné !")
print("Merci d'avoir participé ! A Bientôt !!!")


