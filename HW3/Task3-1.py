# 3.1[16]: Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.
# Примеры/Тесты:
#     Примеры/Тесты:
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#     Output:  2

#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#     Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# ```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь тернарным оператором.

X= int(input('Введите число '))
some_lst=[5,10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
cnt=0
for idx in range(len(some_lst)):
    if X==some_lst[idx]:
        cnt+=1
print(cnt if cnt>0 else -1)
# print(some_lst.count(X)) 