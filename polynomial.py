# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени,
# где все коэффициенты случайные от -10 до 10.
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

import random

def get_coefficient (N):
    coef_list = []
    for i in range(N + 1):
        coef_list.append(random.randint(-10,10))
    return coef_list

N = int(input("Введите степень многочлена "))

coeff = get_coefficient(N)
print(f"коэффициенты многочлена - {coeff}")
polynom = ""
power = len(coeff) - 1
for i in coeff:
    if i == 0:
        continue
    elif i > 0 and power == 1:
        polynom += " + " + str(i) + "X"
    elif i < 0 and power == 1:
        polynom += " " + str(i) + "X"
    elif i > 0 and power == 0:
        polynom += " + " + str(i)
    elif i < 0 and power == 0:
        polynom += " " + str(i)
    elif i > 0 and power == len(coeff) - 1:
        polynom += str(i) + "X^" + str(power)
    elif i < 0:
        polynom += " " + str(i) + "X^" + str(power)
    elif i > 0:
        polynom += " + " + str(i) + "X^" + str(power)
    power -= 1
polynom += " = 0"
print(f"многочлен:    {polynom}")