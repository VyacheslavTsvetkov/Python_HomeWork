# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def power(n):
    k = 0
    while 2**k < n:
        print(2**k, end = " " )
        k += 1


N = int(input("Введите число "))
power(N)