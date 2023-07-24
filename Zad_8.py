# Za pomocą None morzemy wyrazić NIC
# Wartość None możemy przypisać do zmiennej

"""nothing = None
print(f"Nic: {nothing}")
"""
# None ma typ NoneType
# print(f"None jest typu: {type(None)}")

# None może użyć jako wartośdc w słowniku
"""people = [
    {
    "first_name":"Alicja",
    "car": {
        "brand": "Ford",
        "production_year": 2015,
}
},
    {
    "first_name":"Jakub",
    "car": None
    }

]
print(people)"""

"""napis = len("Napis")
print(napis)
# Typ bool

true_variable = True
false_variable = False
print(true_variable == false_variable)
result = bool(7)
print(f"bool(7) -> {result}")
   
result = bool(-3.4)
print(f"bool(-3.4) -> {result}")
result = bool(0)
print(f"bool(0) -> {result}")
result = bool("Napis")
print(f"bool('Napis')->{result}")
result = bool('')
print(f"bool('') -> {result}")
result = bool([4,0])
print(f"bool([4,0]) -> {result}")
result = bool([])
print(f"bool([])->{result}")
result = bool(None)
print(f"bool([None])->{result}")
"""

# Porownania i typ bool zadania

 # Zadanie nr 1  Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania.
"""
computer_price = float(input("Podaj koszt computera ? "))
car_price = float(input("Podaj koszt samochodu ? "))
bike_price = float(input("Podaj koszt roweru ? "))

print(f"Czy komputer jest droższy od samochodu-> {computer_price > car_price}")
print(f"Czy rower jest tańszy od samochodu-> {bike_price < car_price}")
print(f"Czy samochód kosztuje tyle samo co rower-> {bike_price == car_price}")

# Zadanie nr 2
# Poproś użytkownika o wprowadzenie listy zakupów, rozdzielając poszczególne elementy przecinkiem.
# Następnie powiedz (wypisz), czy jest to według Ciebie długa lista, czy też nie.

shopping_list = input("Podaj liste zakupów: ")
shopping_list1 = shopping_list.split(",")
is_shoping = len(shopping_list1)> 4
print(f"Czy lista jest zakupów jest długa ? {is_shoping} ")


# zad 3
war_pocz =int(input("Podaj wartośc początkową: "))
oproc = int(input("Podaj oprocetowanie: "))
l_lat = int(input("Podaj czas trwania w latach: "))
wartosc = war_pocz*(1+oproc/100)**l_lat
wartosc1 = wartosc - war_pocz
wartosc2 = (wartosc1/war_pocz) * 100
print(f"P0 {l_lat} latach wartość twojej lokaty wynosi: {wartosc:.2f} zł ")
print(f"Czy w planowanym okresie wartosc inwestycji wzrośnie o co najmniej 10 % {wartosc2 >= 10 }  ")
"""



































































































































































