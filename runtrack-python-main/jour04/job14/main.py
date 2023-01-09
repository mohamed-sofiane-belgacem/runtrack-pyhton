def my_long_word(n, text):
    text_en_tableau = text.split()
    nv_text = ""
    nb_lettres = 0

    for mot in text_en_tableau:

        for i in mot:
            nb_lettres = nb_lettres + 1

        if nb_lettres > n:
            nv_text = nv_text + mot + " "

        nb_lettres = 0

    print(nv_text)

my_long_word(3, "je suis un test voila voila cree par ben youssam")