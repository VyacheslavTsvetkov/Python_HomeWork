# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше 
# заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

def fill_array (N):
    arr = []
    for i in range (N):
        arr.append(random.randint(1,10))
    return  arr

def find_index (array, low, up):
    res = []
    for i in range(len(array)):
        if array[i] > low and array[i] < up:
            res.append(i)
    return res

N = int(input("Введите количество элементов массива "))
array = fill_array(N)
print(array)
L_bound = int(input("Введите нижнюю границу диапазона "))
U_bound = int(input("Введите верхнюю границу диапазона "))
print(find_index(array, L_bound, U_bound))