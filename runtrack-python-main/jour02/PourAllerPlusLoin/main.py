def ft_is_triangle(a, b, c):
    if a == b and b == c and c == a:
        print("Il est possible de construire un triangle")
        print("Ce triangle sera équilatéral")

    elif a + b > c and a + c > b and b + c > a:
        print("Il est possible de construire un triangle")

        if (a == b or b == c or c == a) and ( a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b):
            print("Ce triangle sera rectangle isocele")

        elif a == b or b == c or c == a :
            print("Ce triangle sera isocèles")

        elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
            print("Ce triangle sera rectangle")

        else:
            print("Ce triangle sera quelconque")
