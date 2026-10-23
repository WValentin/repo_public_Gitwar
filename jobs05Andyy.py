def calcule (num1, operator,num2):
    if operator == '+' :
        return num1 + num2
    elif operator == '-' :
        return num1 - num2
    elif operator == '*' :
        return num1 * num2
    elif operator == '/' :
        return num1 / num2
    else :
        return "Opérateur non reconnu"

num1 = int(input("Entrez un nombre"))
operator =input("Entrez un opérateur (+, -, *, s/)")
num2 = int(input("Entrez un nombre"))

resultat = calcule (num1, operator, num2)
print(resultat)
