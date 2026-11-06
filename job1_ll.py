  int(input("Veuillez entrer la longueur : "))
  int(input("Veuillez entrer la hauteur : "))

def draw_rectangle(x,y,6):
    i = 0
    print("|", "-"*x, "|")
    for i in range(y):
        print("|" + " "*(x+2) + "|") # +2 sinon c'est decale, meme avec +1
    print("|", "-"*x, "|")

print("Le rectangle de longueur = ", width, "et de hauteur = ", height, " :")
