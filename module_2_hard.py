num = int(input("Введите число: "))
result = ''

for i in range(1, num):
    for i2 in range(i + 1, num):
        if num%(i + i2) == 0:
            result += str(i) + str(i2)

print(result)