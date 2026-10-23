import random

while True:

    computer_choice = random.randint(0, 100)
    print("J'ai choisi un nombre entre 0 et 100")

    tries = 0


    while True:
        if tries == 7:
            print(f"Perdu ! Le nombre secret est {computer_choice}")
            break

        user_choice = int(input("Votre proposition : "))
        if user_choice not in range(101):
            print("Veuillez saisir un nombre entre 0 et 100.")
            continue

        tries += 1

        if user_choice < computer_choice:
            print("C'est plus !")

        elif user_choice > computer_choice:
            print("C'est moins !")

        else:
            print(f"Bravo ! Vous avez trouvé en {tries} essais.")
            break

        
    ask_user = input("Voulez-vous rejouer ? (o/n) : ")
    if ask_user == "n":
        print("Merci d'avoir joué, à bientôt !")
        break

