#                             1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


# day =['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
# number = int(input('введите день недели '))
# # print(day[number-1])  показывает день недели, но не работает с отрицательными и >7 числами
# if number <1 or number >7:
#      print('неверный номер')
# elif number<=5:
#     print('будни')
# elif number==6 or number==7:
#     print('выходной')




#                                2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# table = [
#     [False,False,False],
#     [False,False,True],
#     [False,True,False],
#     [True,False,False],
#     [False,True,True],
#     [True,True,True],
#     [True,False,True],
#     [True,True,False], 
# ]
# result = True
# for i in table:
#     if not (not (i[0] or i[1] or i[2]))==(not i[0] and not i[1]and not i[2]):
#         result=False
# print(result)



#                        3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x= int(input('введить координаты оси x '))
# y= int(input('введите координаты оси y '))
# if x>0 and y>0:
#     print('координаты находятся в 1 плоскости')
# elif x<0 and y>0:
#     print('координаты находятся вo 2 плоскости')
# elif x<0 and y<0:
#     print('координаты находятся в 3 плоскости')
# elif x>0 and y<0:
#     print('координаты находятся в 4 плоскости')
# else:
#     print('введите значения больше нуля')





#                  4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a= int(input('введите номер четверти '))
# if a==1:
#     print('x>0 and y>0')
# elif a==2:
#     print('x<0 and y>0')
# elif a==3:
#     print('x<0 and y<0')
# elif a==4:
#     print('x>0 and y<0')
# else: 
#     print('не верный номер четверти')



#                   5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21

# import math


# print('введите координаты первой точки')
# x1=int(input('x= '))
# y1=int(input('y= '))
# print('введите координаты второй точки')
# x2=int(input('x= '))
# y2=int(input('y= '))
# s= math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
# s= round(s,3)
# print('расстояние между точками', s)