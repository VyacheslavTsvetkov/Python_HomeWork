# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя 
#  делает две подсказки. Он называет сумму этих чисел S и 
#  их произведение P. Помогите Кате отгадать задуманные Петей числа.
def findNumbers(S, P):
    number1 = (S + (S * S - 4 * P)**0.5)/ 2 
    return number1


Sum = int(input("Введите сумму двух искомых чисел "))
Prod = int(input("Введите произведение двух искомых чисел "))
first_number = int(findNumbers(Sum, Prod))
second_number = Sum - first_number
print(f"были загаданы числа {first_number} и {second_number}")