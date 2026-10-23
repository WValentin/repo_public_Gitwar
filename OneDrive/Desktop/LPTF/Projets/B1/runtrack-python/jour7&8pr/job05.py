def distance_phare(marches, hauteur):

    z = (marches * hauteur * 70) / 100
    print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {z:.2f} m par semaine.")

distance_phare(100, 20)
