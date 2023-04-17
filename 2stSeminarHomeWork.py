import math

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Input a sum of coins: '))
# coins = input('Input a coins with space: ')

# strcoins = coins.split()
# heads = 0 # количество орлов (нолики)
# tails = 0 # количество решек (единички)
# for i in range (0, n):
#     if strcoins[i] == '0':
#         heads += 1
#     elif strcoins[i] == '1':
#         tails += 1
# print(heads)
# print(tails)
 
# if heads < tails:
#     print('The result is: ', n - tails)
# elif heads > tails:
#     print('The result is: ', n - heads)





# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# P = int(input())
# S = int(input())
# for i in range(x):
#     for j in range(y):
#         if P == i + j and S == i * j:
#             print(i, j)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input('Input a number: '))
# i = 1

# while i <= n:
#     avg = pow(2, i)
#     i+=1
#     if avg > n:
#         break
#     else:
#         print(avg)

