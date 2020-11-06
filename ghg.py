print("MathGEN 1.0")
print("Разработчики: StupidKuklovod, kukold-code, Evgenia003. Дрим тим так сказать.\n")
print("В следующем окне введите число от 1 до 3 - тип уравнения.")
import math
a = int(input("Введите номер, соответствующий виду уравнения, которое вы хотите решить: "))
if a == 1:
          #сюда модуль 1
elif a == 2:
          x1 = int(input("Please, введите x1: "))
          x2 = int(input("Please, введите x2: "))
          x3 = int(input("Please, введите x3: "))
          y = (math.pow(x1, 2)+math.pow(x2, 2)+math.pow(x3, 2)) - 100
          print(y)
elif a == 3:
          # сюда 3 модуль

