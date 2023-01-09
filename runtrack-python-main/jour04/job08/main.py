def ft_add_peer():
    liste = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    nb_valeurs = len(liste) - 1
    i = 0
    somme = 0

    while i <= nb_valeurs:
        if liste[i] % 2 == 0:
            somme = somme + liste[i]
        
        i = i + 1
    
    print(somme)
