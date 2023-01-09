def ft_list_sort(liste):
    nvl_liste = []
    i = 0
    while liste != []:
        nvl_liste.append(min(liste))
        liste.remove(min(liste))
    print(nvl_liste)
        
maliste = [1,3,7,23,64,2,32,76,45]
ft_list_sort(maliste)
