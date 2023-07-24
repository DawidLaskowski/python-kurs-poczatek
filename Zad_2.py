
#Funkcja print i napisy (zadania)

#Zadanie_1
#Zapisz jeszcze raz rozwiązanie zadania ze średnią prędkością biegu, tym razem jako skrypt.
s = 38
t = 3
v = s/t
print("Średnia prędkość wynosi:", v,"km/h")

#Zadanie_2
#Wypisz swoje ulubione potrawy, każdą z nich umieszczając w nowej linii.
print("Moje ulubione potrawy to:","Pizza","Frytki","Miecho", sep="\n" )

print("Cześć! Jestem Python i policzę prędkość Twojego biegu :)")
distance_input = input("Ile kilometrów przebiegłeś/przebiegłaś ? ")
time_input = input("Ile zajeł oci to czasu (godzin)? ")
distance=int(distance_input)
time = int(time_input)

speed = distance / time
print("Biegasz z predkością średnią:", speed,"km/h!")