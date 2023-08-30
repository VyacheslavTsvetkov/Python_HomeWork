#  Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def translate (num: int, base: int) -> int:
    translate_number = ""
    while num > 0:
        remainder = num % base
        translate_number = str(remainder) + translate_number
        num = num // base
    return translate_number
        

number = int(input(f"введите число в десятичной системе счисления "))
base = int(input(f"введите основание системы, в которую нужно перевести "))
print(translate(number, base))