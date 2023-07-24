wybor_gracza1 = input('Gracz1 podaj swój wybór:  ')
wybor_gracza2 = input('Gracz2 podaj swój wybór:  ')

if wybor_gracza1 == 'papier':
    if wybor_gracza2 == 'kamien':
        print('Gracz1 wygrywał')

if wybor_gracza1 == 'kamien':
    if wybor_gracza2 == 'nozyczki':
        print('Gracz1 wygrywał')

if wybor_gracza1 == 'nozyczki':
    if wybor_gracza2 == 'papier':
        print('Gracz1 wygrywał')
