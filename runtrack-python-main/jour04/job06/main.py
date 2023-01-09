def ft_is_list_reverse():
    liste = [1, 3, 7, "Ben"]
    v1 = liste[0]
    v2 = liste[-1]

    if len(liste) >= 2:
        liste[0] = v2
        liste[-1] = v1
