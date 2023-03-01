# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum(a: int, b: int)-> int:
    if a==b==0:
        return 0
    if a==0:
        return b
    return sum(a-1,b+1)

print(sum(0,0))
print(sum(0,2))
print(sum(3,0))
print(sum(5,7))