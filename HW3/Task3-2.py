# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

some_list=[10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
X=int(input('Введите число '))

diff_list=[abs(X-some_list[idx]) for idx in range(len(some_list))]
print(some_list[diff_list.index(min(diff_list))])

# Неудачная попытка решить по-другому, но запуталась с +/- 1
# for idx in range(-1, -len(some_list)-1, -1):
#     if abs(some_list[idx]-X)> abs(some_list[idx+1]-X):
#         result=some_list[idx+1]
# print(result)