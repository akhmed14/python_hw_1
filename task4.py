#  Напишите программу, которая по заданному номеру четверти, 
#  показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Введите номер четверти оси:  "))

if   a == 1: print(" Первая ось: x from 0 to + ∞, y from 0 to + ∞") 
elif a == 2: print(" Вторая ось: x from 0 to  - ∞, y from 0  to + ∞ ")  
elif a == 3: print(" Третья ось: x from 0 to  - ∞, y from 0  to - ∞ ")
elif a == 4: print(" Четвертая ось: x from 0 to  + ∞, y from 0  to - ∞ ")
else:        print("Ошибка") 