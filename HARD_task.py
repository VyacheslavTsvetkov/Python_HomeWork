# Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4
import math

def countDigit (n):
    count = 0
    if (n - math.trunc(n)) == 0:
        while n % 10 >= 1:
            n /= 10
            count += 1
        print(f"Во введенном числе количество цифр - {count} ")
    else:
        if n < 1:
            while n % 1 != 0:
                count += 1
                n *= 10
            count = count + 1
            print(f"Во введенном числе количество цифр - {count} ")
        else:
            while n % 1 != 0:
                n *= 10
            while n % 10 >= 1:
                count += 1
                n /= 10
            print(f"Во введенном числе количество цифр - {count} ")

try:
    a = float(input("введите число "))
except ValueError:
    print("Вы ввели не число. Попробуйте заново")
countDigit(a)
