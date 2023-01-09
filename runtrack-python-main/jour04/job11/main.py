def ft_list_increment():
    L = []
    L.extend([7, 11, 42, 39, 2])
    nb_valeurs = len(L) - 1
    i = 0

    while i <= nb_valeurs:
        L[i] = L[i] + 1
        i = i + 1

    print(L)

