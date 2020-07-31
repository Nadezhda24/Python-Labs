import math

print("Введите x и n: ")
while True:
    try:
        x, n =map(int, input().split())
    except:
        print("Ошибка, введено не целое число")
        continue
    break
print("Ответ: ", (math.sqrt(abs(math.cos(x))**n + (math.exp(n ** 3))/(math.log(x)) + abs(math.sin(x)) ** (1/n))))