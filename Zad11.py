# Mamy 4 rodzaje wspacia - od najlepszych do najgorszych są to:
# - Głowne wsparcie przychód poniżej 5000
# - Wsparcie z funduszu pracownikow -> od 5 do 10 pracowników.
# - Wsparcie dla nowych firm-> krócej niż 3 lata na rynku.
# - Wsparcie na pcieszenie -> dla każego kto nie dostał żadnego innego.

income = 5000
employess_number = 7
years_on_the_market = 3

"""if income < 5000:
    print("Przyznano główne wsparcie")
else:
    if 5 <= employess_number <= 10:
        print("Przynano wsparcie dla pracowników")
    else:
        if years_on_the_market < 3:
            print("Przyznano wsparcie dla firm")
        else:
            print("Przyznano wsparcie na pocieszenie")

 # TO Samo Wykorzystaniem and i negacji
if income < 5000:
    print("Przyznano główne wsparcie")
if income > 5000 and 5 <= employess_number <= 10:
    print("Przyznano wspracie z funduszu pracowników")
if income > 5000 and not 5 <= employess_number <= 10 and years_on_the_market < 3:
    print("Przynano wpsarcie dla nowych firm")
else:
    print("Przyznano wsparcie na pocieszenie")

# Instrukcja elif

if income < 5000:
    print("Przyznano wpsarcie")
elif 5 <= employess_number <= 10:
    print("Przyznano wsparcie z funduszu dla pracowników")
elif years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm")
else:
    print("Przyznano wsparcie pocieszenia )")
"""
income = 4000
expenditures = 2000
age = 35
if age < 18 or income < expenditures:
    print("Nie mozesz wziąc kredytu")
else:
    print("Możesz wziąć kredyt")

