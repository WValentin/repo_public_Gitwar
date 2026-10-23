nom = input("Entrez votre nom : ")
nb = input ("Entrez un chiffre entre 1-10 : ")
def saluer(nom):
    return "Bonjour " + nom + " !"



while int(nb) > 10 or int(nb) < 1:
    nb = input("Je vous ai dit de selectionner un nombre de 1 à 10 :")
    if int(nb) <=10:
        break

print(saluer(nom))
print("Voici votre nombre : ",nb)

saisi = input("Veuillez saisir le nombre de fois que Python c'est cool s'affiche : ")
for i in range(1,int(saisi)):
    print("Python c'est cool ! ")