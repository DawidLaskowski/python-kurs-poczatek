
# Zmienne (zadania)
print('Hello world')
# zadanie 2
#Zakładając, że na lokatę wpłacono 1000 zł, a oprocentowanie wynosi 4% w skali roku, oblicz jaka będzie wartość lokaty po 5 latach.
wartosc_pocz = 1000
liczba_lat = 5
procent = 4
wartosc = wartosc_pocz * (1+procent/100)**liczba_lat
print(wartosc)

# zadanie 1
# W ciągu 3 godzin biegu biegacz pokonał 38 kilometrów. Wyznacz średnią prędkość korzystając ze zmiennych.
s = 38
t = 3
v = s/t
print(v)

#zadanie 3
#Oblicz jaką drogę pokonasz idąc do sklepu po czerwonych liniach i wypisz tyle myślników (-) jaki będzie wynik.
# c^2=a^2+b^2
a = 12
b = 9
c=(a**2+b**2) ** 0.5
print(c)
total_distance = 2 * c
print(total_distance)
kreski = ("-") * int(total_distance)
print(kreski)
