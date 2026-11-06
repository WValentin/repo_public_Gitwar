# Un gardien de phare va aux toilettes cinq fois par jour. Or les WC
# sont au rez-de-chaussée…
# Écrire une fonction qui reçoit en paramètres, le nombre de marches
# du phare et la hauteur de chaque marche (en cm), cette fonction
# doit calculer combien de mètre le gardien effectué par semaine
# pour aller aux toilettes. 
# La sortie du code doit être :
# Pour x marches de y cm, le gardien parcourt z.zz m par semaine.
# On n'oubliera pas :
# 
# ➔ Qu’une semaine comporte 7 jours ;
# ➔ Qu’une fois en bas, le gardien doit remonter ;
# ➔ Que le résultat est à exprimer en m.

# créer une varisable semaine
# créer une variable jours
# créer une varibale nombre marche = x
# créer une variable hauteur de marche cm = y
# resultat en m = z.zz m (float)

# créer une fonction pause_pipi(x, y)

def pause_pipi(x, y):
    jours = 7
    pipi = 5
    nombre_pipi = jours * pipi
    marches = int(x)
    hauteur = float(y)
    total_cm = float(x * y)
    total_m = total_cm / 100
    result = (nombre_pipi * total_m)
    print (result "m")

pause_pipi(1, 30.6)
    #result = nombre de m que le gardien parcours par semaine



    


