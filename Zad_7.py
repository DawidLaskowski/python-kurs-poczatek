#SŁowniki zawirające inne słwoniki w środku

"""teacher = {
    "first_name": "Jan",
    "last_name": "Kowalski",
    "age": 45,
    "contact": {
        "sign_date": "23-11-2018",
        "salary": 3500
    }
 }
print(teacher)

# Tak jak słownik może listy tak lista może zawierać słownik student students

students = [
    {
        "first_name": "Dawid",
        "last_name": "Laskowski",

    },
    {
        "first_name": "Alicja",
        "last_name": "Kowalska",

    }
]
print(students)
print(students[0])
print(students[1])
print(students[1]['last_name'])
"""
# Typ dict, czyli słownik
# zadanie nr_1
przedmioty = {
    "matematyka": [5,2,3,4,5],
    "J.polski": [4,2,1,4,5],
    "Fizyka": [3,5,4,3,3],
    "Religa": [5,5,4,2,3],
    }
print(przedmioty)

#zadanie nr_2

my_family = {
    "name": "Dawid",
    "surname": "Laskowski",
    "birth_date": "28-08-1996",
          }

print(my_family)

"""print(my_family)
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
wybor_kat = input("Wybierz jedną z kategorki wyadtków :")
print(f'Na {wybor_kat} wydajesz {wszystkie}')"""