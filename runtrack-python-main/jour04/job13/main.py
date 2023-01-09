def ft_remove_double():
    liste = [10,20,30,20,10,50,60,40,80,50,40]
    nvl_liste = []

    for i in liste:
        if i not in nvl_liste:
            nvl_liste.append(i)

    print(nvl_liste)
    
ft_remove_double()