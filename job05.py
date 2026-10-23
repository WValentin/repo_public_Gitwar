L = [1,2,3,4,5]

print(L)

print(L[1])

def liste_L():
    L[3] = L[2] + L[4]
    return L

print(liste_L())

print(L[-1])