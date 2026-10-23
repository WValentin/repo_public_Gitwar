def chiffrer_message(message, decalage):
    abc = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""
    for lettre in message:
        if lettre in abc:
            
            nouvelle_pos = (abc.index(lettre) + decalage) % 26
            resultat = resultat + abc[nouvelle_pos]
            
        else:
            resultat = resultat + lettre
            
    return resultat

print(chiffrer_message("xyz", 3))
