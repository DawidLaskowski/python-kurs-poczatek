# Lista smkaów
favourite_flavours = [
    "malinowy",       #0 / -5
    "truskawkowy",    #1 / -4
    "czekoladowy",    #2 / -3
    "pistacjowy",     #3 / -2
    "kokosowy",       #4 / -1
]

"""
print("Ulubiony smak lodów:", favourite_flavours[0])
print("Drugi smak lodów:", favourite_flavours[1])
print("Trzeci smak lodów:", favourite_flavours[2])
print("Czwarty smak lodów:", favourite_flavours[3])
print("Piaty smak lodów:", favourite_flavours[4])

# Długośc listy
print(f"Na liscie jest {len(favourite_flavours)} smaków lodów")
#Ostatni element listy
print("Ostatni element:", favourite_flavours[len(favourite_flavours) - 1])
#Ostatni element listy - wygodniej
print("Ostatni element:", favourite_flavours[-1])

#Smaki na liście
print("Dwa najbardziej ullubione smaki:", favourite_flavours[:2])
print("Dwa najbardziej ullubione smaki:", favourite_flavours[2:])

# Dodanie smaku
print(favourite_flavours)
favourite_flavours.append("Kawowy")
print(favourite_flavours)
# Dodanie w dowolnym miejscu
favourite_flavours.insert(0,"jagodowy")
print(favourite_flavours)

# Usunięcie elementu po indeksie
del favourite_flavours[4]
print(favourite_flavours)

# wyciądniecie z listy
second_flavour = favourite_flavours.pop(1)
print(second_flavour)
#Usunięcie elementu p owartości
favourite_flavours.remove("czekoladowy")
print(favourite_flavours)
favourite_flavours[-1]="malinowy"
print(favourite_flavours)"""



# Zadania Typ list1
"""
Zadanie nr 1
Stwórz zmienną favourite_sports, która będzie listą zawierającą nazwy dyscyplin sportu, które lubisz.
Następnie wypisz informacje, jaki sport jest pierwszy na Twojej liście, a jaki ostatni.
Podmień jeden ze sportów na inny i wypisz całą listę.


favourite_sports = ["piłka_nozna","siatkówka","tenis","koszykówka","piłka_ręczna"]
print(favourite_sports)
print("Pierwszy sport na mojej liście to:",favourite_sports[0])
print("Ostatni sport na mojej liście to:",favourite_sports[-1])
#del favourite_sports[1]
#favourite_sports.insert(1,"Rugby")
favourite_sports[1]="Rugby"
print(favourite_sports)
"""
"""
Zadanie nr 2

Zapytaj użytkownika o 3 ulubione potrawy i zapisz je w postaci listy.

print("Podaj 3 ulubione potawy ?")
potrawa1=input()
potarwa2=input()
potrawa3=input()
potawy=[potrawa1,potarwa2,potrawa3]
print("Towje potawy to: ",potawy)

print("Podaj 3 ulubione potawy ?")
favourite_dish=[]
potrawa=input()
favourite_dish.append(potrawa)
potrawa=input()
favourite_dish.append(potrawa)
potrawa=input()
favourite_dish.append(potrawa)
print("Towje potawy to: ",favourite_dish)

favourite_dish=[]
dish = input("Podaj dania oddzielając przecinkiem ? ")
favourite_dish=dish.split(",")
print(favourite_dish)
"""
"""
#Zapytaj użytkownika o numer telefonu i wypisz go w postaci zanonimizowanej.
#Wypisz pierwszych 6 cyfr, a kolejne zastąp myślnikiem.

phone_number = input("Jaki jest twoj numer telefonu ?")
phone_number = phone_number.replace("-"," ")
public = phone_number[:6]
number_of_private = len(phone_number) - 6
n_prvate ="-" * number_of_private
anonimowy = f"{public}{n_prvate}"
print("Znanizowany numer:", anonimowy)
"""
"""
numer = input("Podaj nr_telefonu ? ")
public = numer[:6]
number_of_private = len(numer) - 6
n_public = "-" * number_of_private
ann = f"{public}{n_public}"
print(ann)
"""




