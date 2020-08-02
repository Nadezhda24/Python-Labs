import math

def isint(value):
    return int(value) == str(value)

#x, n = map(int, input("Задание №1.\nВведите x и n: ").split())
#print("Ответ: ", (math.sqrt(abs(math.cos(x)) ** n + (math.exp(n ** 3)) / (math.log(x)) + abs(math.sin(x)) ** (1 / n))))

s = [['S','T','P','S','T','E'],[1,2,3,4,5,6,7,3,8,9,5,2]]
r = map(lambda x: s[1]*s[1], s[0])
print(r)