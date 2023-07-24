# Zadania instrukcja if else

"""computer_price = float(input("Podaj koszt computera ? "))
car_price = float(input("Podaj koszt samochodu ? "))
bike_price = float(input("Podaj koszt roweru ? "))

if computer_price > car_price:
    print("Komputer jest droższy od samochodu")
else:
    print("Komputer jest tańszy od samochodu")
if bike_price < car_price:
    print("Rower jest tańszy od samochodu")
else:
    print("Samochód jest tańszy od roweru")
if car_price == bike_price:
    print("Samochód kosztuje tyle co rower")
else:
    print("Samochód nie kosztuje tyle co rower")
# zadanie 2
shopping_list = input("Podaj liste zakupów: ")
shopping_list1 = shopping_list.split(",")
if len(shopping_list1) > 4:
    print("Lista jest długa")
else:
    print("Lista jest krótka")

#zadanie nr_3
print("Ile pieniędzy wydajesz na? ")
jedzenie= float(input("jedzenie? "))
rozrywka=float(input("rozrywkę? "))
oplaty=float(input("opłaty? "))
inne=float(input("inne? "))
wszystkie_wydatki = jedzenie + rozrywka + oplaty + inne

wszystkie = {
    "jedzenie": jedzenie * 100 / wszystkie_wydatki,
    "rozrywka": rozrywka * 100 / wszystkie_wydatki,
    "oplaty": oplaty * 100 / wszystkie_wydatki,
    "inne": inne * 100 / wszystkie_wydatki,
}
wybor1="jedzenie"
if wszystkie['rozrywka'] > wszystkie[wybor1]:
    wybor1 ="rozrywka"

if wszystkie['oplaty'] > wszystkie[wybor1]:
    wybor1 ="oplaty"

if wszystkie['inne'] > wszystkie[wybor1]:
    wybor1 ="inne"


print(f" Najwiecej wydajesz na {wybor1} - {wszystkie[wybor1]:.0f}% wszystkich wydatków")

#zadanie 4

math_grade = int(input("Jaka jest twoja ocena koncowa z matematyki ? "))
physics_grade = int(input("Jaka jest twoja ocena koncowa z fizyki ? "))
polish_grade = int(input("Jaka jest twoja ocena koncowa z polskiego ? "))
english_grade = int(input("Jaka jest twoja ocena koncowa z angielskiego ? "))
history_grade = int(input("Jaka jest twoja ocena koncowa z histori ? "))

number_of_failures = 0

if math_grade < 2:
    number_of_failures = number_of_failures + 1
if physics_grade < 2:
    number_of_failures = number_of_failures + 1
if polish_grade < 2:
    number_of_failures = number_of_failures + 1
if english_grade < 2:
    number_of_failures = number_of_failures + 1
if history_grade < 2:
    number_of_failures = number_of_failures + 1

if number_of_failures == 0:
    print("Gratulacje ! Zdałaś/zdałaś do następnej klasy :)")
else:
    if number_of_failures == 1:
        average = (math_grade + physics_grade + polish_grade + english_grade + history_grade) / 5
        if average > 3.5:
          print("Gratulacje ! Zdałaś do nasępnej klasy :)")
        else:
          print("Niestety...")
    else:
        print("Niestety")

# zadanie 4
name = input("Jak masz na imie? ")
if name[-1] =="a":
    print("Jestes kobietą")
else:
    print("Jestes mężczyzną")
"""
