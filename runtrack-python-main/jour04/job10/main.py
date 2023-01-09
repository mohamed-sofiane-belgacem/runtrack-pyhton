def ft_is_multiply():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    nb_valeurs = len(L) - 1
    i = 0
    res = 1

    while i <= nb_valeurs:
        if L[i] >= 25 and L[i] <= 90:
            res = res * L[i]
        i = i + 1
        
    print(res)
        
