# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random


def coinDistribution (N): #случайное распределение сторон монет 1 - решка/tails, 2 - орел/eagle.
    coin_list = []
    for i in range (N):
        coin_list.append(random.randint(1,2))
    print(f"Монетки распределились таким образом - {coin_list} \n 1 - решка, 2 - орел")
    return coin_list

def coinTurn (coin_list):
    tails = coin_list.count(1)
    eagle = coin_list.count(2)
    if tails > eagle:
        print(f"Нужно перевернуть минимум {eagle} монет")
    else:
        print(f"Нужно перевернуть минимум {tails} монет")

N = int(input("Сколько на столе лежит монеток? "))
Distrib = coinDistribution(N)
coinTurn(Distrib)