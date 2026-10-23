hauteur = int(input("Entrez la hauteur du triangle : "))

for i in range(1, hauteur + 1):

    espaces_externes = " " * (hauteur - i)

    if i == hauteur:
        interieur = "_" * (2 * (i - 1))

    else:
        interieur = " " * (2 * (i - 1))

    print(f"{espaces_externes}/{interieur}\\")
