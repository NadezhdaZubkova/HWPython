# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

count_coins=int(input('Введите колличество монет '))
eagle=0
tails=0
while count_coins>0:
    heads_or_tails=int(input('Введите положение монеты: орел-1, решка -0 : '))
    if heads_or_tails==1:
        eagle+=1
    else: tails+=1
    count_coins-=1
print('Кол-во монет,чтобы перевернуть: ', eagle if eagle<tails else tails)

