
def taille(L):
    a = 0 
    for i in L : 
        a +=1
    return a


def arrondi(lst):
    for i in range(taille(lst)):
        lst[i] = int(lst[i])

def tri(L) : 
    a = 0
    while a < taille(L)-1 : 
        for i in range(a+1,taille(L)):
            if L[a] > L[i] : 
                tmp = L[a]
                L[a] = L[i]
                L[i] = tmp
        a+=1
    return L

        
        
L = [22.4, 4.0, 16.22,9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

print(L)
arrondi(L)
print(L)
tri(L)
print(L)
