string = "abcdefghijklmnopqrstuvwxyz" * 10

# Détermine la longueur de la chaîne sous forme de pyramide
length = 1
while length ** 2 <= len(string):
    length += 1

# Affiche la pyramide
for i in range(length):
    print(string[i**2: (i+1)**2])