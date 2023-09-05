#  Задача 30:  Заполните массив элементами арифметической прогрессии. 
#  Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#   Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#  Каждое число вводится с новой строки.

def input_data (string: str ) -> int:
    res = int(input(string))
    return res

def calculate (a1, n, d):
    a_n = a1 + (n - 1) * d
    return a_n

first_elem = input_data("введите первый элемент прогрессии ")
total_elem = input_data("введите общее количество элементов прогрессии ")
difference = input_data("введите разность прогрессии ")
result = []
i = 1
for i in range(1, total_elem + 1):
    result.append(calculate(first_elem, i, difference))

print(result)