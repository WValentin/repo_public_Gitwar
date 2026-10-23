import random
nombre_secret=random.randint(0,100)
essais=0
print("J'ai choisi un nombre entre 0 et 100. Devinez-le !")
while True:
    proposition=int(input("Votre proposition : "))
    essais=essais+1
    if proposition<nombre_secret:
        print("C'est plus !")
    elif proposition>nombre_secret:
        print("C'est moins !")
    else:
        print("Bravo ! Vous avez trouvé en",essais,"essais.")
        break