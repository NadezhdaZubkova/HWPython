# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 	Примеры/Тесты:
# 	3 2 4 -> yes
# 	3 2 1 -> no

n,m,k = int(input('Введите размер n ')),int(input('Введите размер m ')), int(input('Введите колличество долек '))
print('YES' if (k<= n*m and (k//n or k//m)) else 'NO')