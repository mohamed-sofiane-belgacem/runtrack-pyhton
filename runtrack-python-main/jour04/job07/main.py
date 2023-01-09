def ft_is_nb_multiple():
    L = [8, 24, 48, 2, 16]
    nb_valeur_liste = len(L) - 1
    i = 0
    nb_de_multiple = 0

    while i <= nb_valeur_liste:
        if L[i] % 3 == 0:
            nb_de_multiple = nb_de_multiple + 1

        i = i + 1
    print("Il y'a " + str(nb_de_multiple) + " multiple(s) de 3 dans la liste")

            