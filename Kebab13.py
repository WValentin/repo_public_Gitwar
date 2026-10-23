def tapis(n):
    for x in range(n + 3):
        if x == 0 or x == n + 2:
            print("+", (n + 1) * "-", "+", sep = "")
        else:
            print("|", (n + 1 - x) * "#", " ", (x - 1 ) * "#", "|", sep = "")