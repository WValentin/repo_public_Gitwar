def saluer(nom):
    print(f"Bonjour {nom} !")
n=0
nom = input("votre nom ? ")

while n== 0:
    nbr = int(input("nombre entre 1-10 ? "))
    if nbr >= 1 and nbr <= 10:
        saluer(nom)
        for i in range(nbr):
            print(f"Répétition {i+1}: Python c'est cool !")
        n+=1    
    else:
        print("erreur, nombre hors de la plage, réessayer") 
