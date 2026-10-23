def cesar(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""
    for lettre in message:
        if lettre in alphabet:
            position = alphabet.index(lettre)
            nouvelle_position = (position + decalage) % 26
            resultat = resultat + alphabet[nouvelle_position]
        else:
            resultat = resultat + lettre
    return resultat


print(cesar("chat", 3))
print(cesar("xyz", 3))
print(cesar("abc", -1))
print(cesar("bonjour le monde", 3))