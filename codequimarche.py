def chiottes(nbr_marches, h_marches) :
    distance = ((nbr_marches * h_marches * 70)/100) + ((nbr_marches * h_marches * 70)% 100)
    print(f"Pour {nbr_marches} marches de {h_marches} cm, le gardien parcourt {distance:.2f} m par semaine.")

chiottes(40, 10)