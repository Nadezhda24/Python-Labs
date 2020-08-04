import math

x, n = map(int, input("Задание №1.\nВведите x и n: ").split())
f = lambda x, n: print("Ошибка, введено не целое число. Попробуйте снова.") if((x<0) or (n<0)) else print("Ответ: ", (math.sqrt(abs(math.cos(x)) ** n + (math.exp(n ** 3)) / (math.log(x)) + abs(math.sin(x)) ** (1 / n))))
f(x,n)

s = [['S','T','P','S','E'],[3,2,3]]
square = lambda a: (int(a) > 0 and int(a) ** 2) or print("Ошибка, введено отрицательное число. Попробуйте снова.")
trapezoid = lambda x,y,h: (int(x)>0 and int(y)>0 and int(h)>0 and 0.5 * int(h) * (int(x)+int(y))) or print("Ошибка, введено отрицательное число. Попробуйте снова.")
parallelogram = lambda a,h: (int(a)>0 and int(h)>0 and int(a)*int(h)) or print("Ошибка, введено отрицательное число. Попробуйте снова.")
exit = lambda : 0
f = list(map(str,s[0]))
d = list(map(str,s[1]))
choice = lambda : list(map(lambda x:(x =='S') and square(d[0]) or (x =='T') and trapezoid(d[0], d[1], d[2]) or (x =='P') and parallelogram (d[0],d[1]) or  (x =='E') and exit(),f ))
print("Задание №2\nОтвет:")
print(choice())
