def my_sort(L: list):
    coups = 0
    done = False
    while not done :
        done = True

        for i in range(len(L)):

            if i != len(L)-1 and L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                coups += 1
                done = False

    
    print("Nombre de coups : ", coups)
    return L

mylist = [12, 9, 67, 45, 23, 6)
print(my_sort(mylist))
