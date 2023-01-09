liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
liste2 = []
nvl_liste = []

for i in liste:
    i = int(i)
    liste2.append(i)

for i in liste:
    nvl_liste.append(min(liste2))
    liste2.remove(min(liste2))

print(nvl_liste)
