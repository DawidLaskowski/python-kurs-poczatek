# Operatory logiczne and/or/not
"""
kwota_kredytu = int(input("Jaka jest kwota kredytu? "))
oproc_kredytu = float(input("Jakie jest oprocentowanie ? "))
wklad_wlasny = int(input("Jaki jest czas kredytowania (w latach) ?"))
czas_kredytowania = int(input("Jaki jest czas kredytowania (w latach) ?"))
przychód_miesieczny= int(input("Jaki jest miesięczny przychód ? "))
suma_miesc = int(input("Jaka jest suma miesięcznych wydatków ?"))

rata = (kwota_kredytu * oproc_kredytu/100)/12 + kwota_kredytu/(czas_kredytowania*12)
dost_srd = przychód_miesieczny - suma_miesc
war_nie = wklad_wlasny + kwota_kredytu

own_contribution = wklad_wlasny/war_nie
money_over = kwota_kredytu + wklad_wlasny
matching_higher = own_contribution >= 0.2 and money_over >= 1000
matching_lower = own_contribution >= 0.1 and money_over >= 2000
if matching_higher or matching_lower:
    print("Możesz wziąć kredyt")
else:
    print("Nie możesz wziąć kredytu")
"""
# instrukcja in pozwala sprawdzić czy litera występuje
"""
favourite_sport = ["bieganie","koszykówka","jazda na rowerze","pływanie"]
if "koszykówka" in favourite_sport:
    print("Jest")
else:
    print("Nie ma")

person = {
    "first_name": "Dawid",
    "last_name": "Laskowski"
}
if "first_name" in person:
    print(person["last_name"])
"""
"""
# Operatory in oraz is zadania
# zadanie nr 1
shoping_elelments = input("Wprowadź listę zakupów: ")
shoping_list = shoping_elelments.split(",")
if "chleb" in shoping_list or "bułki" in shoping_list:
    print("Planujesz kupić pieczywo")
else:
    print("Nie kupiłes pieczywa")

#Zadanie 2
number = (input("Podaj numer tel: "))
if "0" in number:
    print("Zawiera 0")
else:
    print("Nie zawiera 0")
"""
# Zadanie 3

value =3
if value is True:
    print("To prawda")
if value is False:
    print("To fałsz")
else:
    print("To nie fałsz")
if value is None:
    print("To None")
else:
    print("To inna wartość")
