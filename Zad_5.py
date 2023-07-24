

"""python_age = 30
info = f"Python ma juz prawie:"+ str(python_age) + " lat!"
info = f"Python ma juz prawie {python_age} lat!"
calculation = f"Wynik działania 3 x 6 to {3 * 6}"
print(calculation)
print(info)
name = "Dawid"
hello = f"Nazywam się {name}"
print(hello)

# Średnia prędkość biegu

distance = 35
time = 3
speed = distance / time
print(f"Biegasz z prędkością średnią: {speed:.2f} km/h! ")

your_street = input("Na jakiej ulicy mieszkasz ? ")
print(f"Nazwa tej ulicy ma aż {len(your_street)} liter!")

short = "Krótki napis"
length = "Bardzo bardzo bardzo bardzo długi napis "
print(short, "ma długośc", len(short))
print(length, "ma długośc", len(length))
"""
#Typ str czyli napisy zadania

#Zadanie nr 1
#Dostosuj program liczący wartość lokaty, tak aby wyświetlał ją z dokładnością do groszy (dwóch cyfr po przecinku).

"""war_pocz =int(input("Podaj wartośc początkową: "))
oproc = int(input("Podaj oprocetowanie: "))
l_lat = int(input("Podaj czas trwania w latach: "))
wartosc = war_pocz*(1+oproc/100)**l_lat
print(f"P0 {l_lat} latach wartość twojej lokaty wynosi: {wartosc:.2f} zł ")"""

#Zadanie 2 Zapytaj użytkownika o imię i wypisz ile liter zawiera.
"""
print("Podaj imie:")
imie=input()
print(f"Twoje imie zawiera {len(imie)}")
"""
"""
#Zadanie 3 Zapytaj użytkownika gdzie mieszka i wypisz odpowiedź, np. "Jak miło, że mieszkasz w Gdańsku".
print("Gdzie mieszkasz ? ")
place =input()
print(f"Jak miło że mieszkasz w {place.title()}")
"""
# Zadanie 4
# Wyobraź sobie, że przetwarzasz dane dotyczące samochodów.
# Numery tablic rejestracyjnych zostały jednak zapisane w niespójny sposób:
#ford = "ab100100"
#audi = "EEE 123123"
#citroen = "Zk-300300"
#honda = "AB210210"

ford = "ab100100"
audi = "EEE 123123"
citroen = "Zk-300300"
honda = "Ab210210"

print(f"Ford: {ford.upper()}")
audi_dash=audi.upper().replace(" ", "")
print(f"Audi: {audi_dash}")
citroen_dash=citroen.replace("-","")
print(f"Citroen: {citroen_dash.upper()}")
print(f"Honda: {honda.upper()}")




