produit = "lait"
prix = 1 
quantité = 20 
achat = int(input("Combien de lait souhaitez-vous acheter ?"))


print("produit:", produit)
print("prix à l'unité:", prix)
print("quantité en stock :", quantité)
quantité = quantité + 5 
quantité = quantité - achat
prix = prix + prix * 0.1

print("prix à l'unité après inflation:", prix)
print("quantité restante :", quantité) 