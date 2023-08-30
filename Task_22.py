# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def fill_set (N):
    new_set = set ()
    for i in range (N):
        new_set.add(input(f"введите {i}-й элемент множества "))
    return new_set

first_set_number = int(input(f"введите количество элементов первого множества "))
first_set = fill_set(first_set_number)
second_set_number = int(input(f"введите количество элементов второго множества "))
second_set =fill_set(second_set_number)

sorted_union = sorted(first_set.union(second_set))
print(sorted_union)

