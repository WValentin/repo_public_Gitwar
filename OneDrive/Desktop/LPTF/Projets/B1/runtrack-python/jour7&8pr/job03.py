def afficher_tapis(n):

    print("+" + "-" * (n + 1) + "+")
    
    for i in range(n + 1):
 
        nb_gauche = n - i
        nb_droite = i

        motifs_gauche = "#" * nb_gauche
        motifs_droite = "#" * nb_droite
        espace_vide = " "
        
        ligne_complete = "|" + motifs_gauche + espace_vide + motifs_droite + "|"

        print(ligne_complete)

    print("+" + "-" * (n + 1) + "+")

afficher_tapis(10)
