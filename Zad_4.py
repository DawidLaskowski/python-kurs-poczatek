# typy zmiennych int i float
# Przykłady zastsowania zmiennych
"""
int_value = 30
print('int value:\t',int_value,'\t Typ:', type(int_value), sep='\t\t')

float_value = 7.8
print('float value:',float_value,'\t Typ:', type(float_value), sep='\t\t')

float_from_int = float(15)
print('float from int:',float_from_int,'Typ:', type(float_from_int), sep='\t\t')

float_from_str = float("27.375")
print('float from str:',float_from_str,'Typ:', type(float_from_str), sep='\t\t')

int_from_str = float("10")
print('int from str:',int_from_str,'\t Typ:', type(int_from_str), sep='\t\t')

int_from_float = int(7.8)
print('int from float',int_from_float,'\t Typ:', type(int_from_float), sep='\t\t')
"""
# Następny przykład zmiennych wybieranie liczb
"""
math_grade = 4
bio_grade = 3
chemistry_grade = 5
physisc_grade = 2
best_grade = max(math_grade,bio_grade, chemistry_grade,physisc_grade)
worst_grade = min(math_grade,bio_grade, chemistry_grade,physisc_grade)
print("Najlepsza ocena to: ", best_grade)
print("Njagorsza ocena to: ", worst_grade)

#Funkcja wbudowana abs (wartosć bezwxlędna

print(abs(-4))
print(abs(8))
print(abs(-3.15))
"""
# Zadanie nr 1
# Napisz program, który zapyta użytkownika jaka jest cena jabłek w Biedronce, Lidlu i Żabce.

cena_bied = input("Jaka jest cena jabłek w biedronce ? ")
cena_bied=float(cena_bied)
print("Jabłka w biedronce kosztują:",cena_bied)
cena_lidl = input("Jaka jest cena jabłek w lidlu ? ")
print("Cena jabłek w lidlu:",cena_lidl)
cena_lidl=float(cena_lidl)
print("Jabłka w biedronce kosztują:",cena_lidl)
cena_zabka = input("Jaka jest cena jabłek w zabka ? ")
cena_zabka=float(cena_zabka)
print("Jabłka w żabce kosztują:",cena_zabka)
Najdrozsze = max(cena_bied,cena_lidl,cena_zabka)
Najtansze = min(cena_bied,cena_lidl,cena_zabka)
print("Najdroższe jabłka kosztują: ", Najdrozsze)
print("Najtańsze jabłka kosztują: ", Najtansze)

