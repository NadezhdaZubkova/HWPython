# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Примечание.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети. Обойдите дополнительной проверкой возможность комплексных решений. 
# Можно игнорировать то, что получаться рациональные решения вместо натуральных.

# Для вычисления квадратного корня используйте возведение в степень 0.5 или 
# (*) Усложнение. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.

from math import sqrt

sum_of_numbers=int(input('Сумма чисел равна: '))
product_of_numbers=int(input('Произведение чисел равно: '))
# x^2-x*sum_of_numbers+producn_of_numbers=0  -уравнение для решения
if ( sum_of_numbers**2 +4*sum_of_numbers) >0:
    print(f'x1 = {(sum_of_numbers+(sum_of_numbers**2 - 4*product_of_numbers)**0.5)/2}')
    print(f'x2 = {(sum_of_numbers-(sum_of_numbers**2 - 4*product_of_numbers)**0.5)/2}')
elif  sum_of_numbers**2 +4*sum_of_numbers==0:
     print(f'x = {sum_of_numbers/2}')
else: print('нет корней')