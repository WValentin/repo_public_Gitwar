def tapis(taille):
    a="+"
    b="-"
    c="|"
    d="#"
    e=" "
    n=0
    print(a+b*taille+a)
    for i in range(taille):
        print(c+d*(taille-1)+e+d*n+c)
        n=n+1
        taille=taille-1
    print(a+b*n+a)


tapis(10)