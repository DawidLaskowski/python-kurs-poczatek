#Pentle for

"""collection = ["ciastko","książki","piłka"]

for element in collection:
    print(element)"""
# Wypisanie listy ulubionych sportów

"""favourite_sport=["bieganie","pływanie","jazda na rowerze","trithlon"]
for sport in favourite_sport:
    print(sport)

# Kod pocztowy
post_code = input("Podaj kod pocztowy: ")
for code in post_code:
    print(code)

expenditures = {
    "prąd": [250],
    "woda": [30.45],
    "zakupy": [120.15,170.53,20.15]
}
for expenditures_element in expenditures:
    print(expenditures_element)
# klucze i wartośći
for expenditures_element in expenditures:
    print(f"{expenditures_element}->{expenditures[expenditures_element]}")

expenditures = {
    "prąd": [250],
    "woda": [30.45],
    "zakupy": [120.15,170.53,20.15]
}
for expenditures_name, expenditures in expenditures.items():
    print(f"{expenditures_name}->{expenditures}")

# krótkę można "rozpakować"
item = ("prąd", 340 )
value = item
print(value)

# Wypisujemy kod pocztowy - znak wraz z informacją o kolejności
post_code = input("Jaki jest twój kod pocztowy ?")
for index,letter in enumerate(post_code):
    print(f"[{index}]) -> {letter}")

# Wypisanie co drugiego sportu
favourite_sport = ["bieganie","pływanie","jazda na rowerze","thriatlon"]
for index, sport in enumerate(favourite_sport):
    if index % 2 == 0:
        print(sport)

# zadanie 1
grades = []
grade_input = input("Podaj kolejną ocene albo zakończ wpisując 'X")
while grade_input != 'X':
    grade=int(grade_input)
    grades.append(grade)
    grade_input = input("Podaj kolejną ocene albo zakończ wpisując 'X")

grades_sum = 0
for garde in grades:
    grades_sum +=grade

average = grades_sum / len(grades)
print(f"Twoja średnia wynosi {average:.2f}")

phone_number = input("Podaj numr tel: ")
phone_number=phone_number.replace("-","")
formatted_phone_number = ""
for index,digit in enumerate(phone_number):
    if index %3 == 0 and index != 0:
        formatted_phone_number +="-"
    formatted_phone_number += phone_number[index]

print(f"Twój numer telefonu to: {formatted_phone_number}")

# for in range
#zadania
#Medtoda zwraca liczbę wystąpień danego znaku w napisie
sentence = "Napis z dużą liczbą aaaa - sia laaa laaa"
print(sentence.count("a"))

#Zadania

phone_number = input("Podaj numer telefonu: ")
for digit in range(10):
    digit_times_in_number = phone_number.count(str(digit))
    print(f"Cyfra{digit} wystepuje w twoim numerze: {digit_times_in_number} razy")

#zadanie 3
capital = int(input("Na jaką kwote jest kredyt ? "))
interest_rate = float(input("Jakie jest oprocentowanie (%) ? "))
years = int(input("Na ile lat jest kredyt ? "))
inital_fees = int(input("Jakie są koszty początkowe? "))

crediet_time_in_months = years*12
monthly_paid_capital = capital / crediet_time_in_months
total_paid = inital_fees
for monthly_number in range(1,crediet_time_in_months + 1):
    capital_to_be_paid = capital - (monthly_number - 1) * monthly_paid_capital
    installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
    total_paid += installment
    print(f"Rata w miesiącu {monthly_number} wyniesie {installment:.2f}")

print(f"Zaciągajac {capital} na tych warunkach spłacisz z odsetkami {total_paid}")

expenditures = [120, 300, 250.45, 1001, 50, 75]
for expenditure in expenditures:
    if expenditure > 1000:
        print("Drugi wydatek znaleziony! ")
        break
else:
    print("Nie znaleziono nic super drogiego")
"""
favourite_sport=["bieganie","pływanie","jazda na rowerze","triathlon"]
for index, sport in enumerate(favourite_sport):
    if index %2!=0:
        continue
    print(sport)


