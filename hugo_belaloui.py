def saluer(nom):
    print(f"Bonjour {nom} !")

num = int(input("entrez un nombre entre un et dix : "))
while num < 1 or num > 10:
    num = int(input("entrez un chiffre entre un et dix : "))
nom = input("entrez votre nom : ")

saluer(nom)
for i in range(num+1):
    print("Répétition X : Python c'est cool !")