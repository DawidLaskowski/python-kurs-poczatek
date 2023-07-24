# do póki licznik nie przekroczy 30

"""counter = 0
while counter <= 30:
    print(counter)
    counter +=1
while True:
    print("Nigdy nie skończę !!!")


expected_potatoes = int(input("Ile ziemniaków chcesz na obiad ?"))
potatoes = []
while len(potatoes) < expected_potatoes:
    print("Obieram ziemiaka")
    print("I wrzucam do garnka :)")
    potatoes.append("Ziemiak")
print(potatoes)


option = "T"
while option == "T":
    income = int(input("Podaj przychód: "))
    employess_number = int(input("Podaj liczbę pracowników: "))
    years_on_the_market = int(input("Ile lat działacie na rynku: "))
    if income <2000:
        print("Przyznano ci wsparcie główne")
    elif 5 <= employess_number <= 10:
        print("Przyznano wsparci z funduszu pracowników")
    elif years_on_the_market < 3:
        print("Przyznano wpsarcie dla nowych firm")
    else:
        print("Przyznano wpsracie na pocieszenie;)")
    option = input("Jeżeli chcesz sprawdzić dla innych danych wpisz 'T':")


favourites_sports = ["bieganie","pływanie","jazda na rowerze","triathlon"]
sport_index = 0
while sport_index < len(favourites_sports):
    if sport_index %2 == 0:
        print(favourites_sports[sport_index])
    sport_index += 1

#Sumowanie liczb = [1, 3, 510, 123, 24]
numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
number_index = 0
while number_index < len(numbers):
    numbers_sum=numbers_sum+numbers[number_index]
    number_index += 1
print(f"Suma: {numbers_sum}")

post_code = input("Jaki jest twój kod pocztowy? ")
letter_index =0
while letter_index < len(post_code):
    print(f"{post_code[letter_index]}")
    letter_index +=1


#pętla while
#zadanie 1
liczba = int(input("Podaj liczbe:  "))
l_prob = 1
while l_prob < 10:
    if liczba % 2==0:
        print("Przysta")
    else:
        liczba = int(input("Podaj liczbe:  "))
    l_prob+1
print("Za dużo prób niestety")

#Zadanie 2
favourite_dish = input("Podaj ulubione dania: ")
favourite_dish = favourite_dish.split(",")
dish_index =0
while dish_index < len(favourite_dish):
    print(f"{dish_index}:{favourite_dish[dish_index]}")
    dish_index +=1


#zadania 3

number = input("Podaj numer telfonu: ")
number = number.replace("-","")
formatted_number = ""
letter_index = 0
while letter_index < len(number):
    if letter_index %3 == 0 and letter_index !=0:
        formatted_number += "-"
    formatted_number += number[letter_index]
    letter_index += 1
print(f"Twój numer telefonu to: {formatted_number}")
"""