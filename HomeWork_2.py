S = int(input("Введите сумму двух натуральных чисел (не более 1000): "))
P = int(input("Введите произведение двух натуральных чисел (не более 1000): "))

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == S and x * y == P:
            print("Задуманные Петей числа: ", x, "и", y)
            break
    else:
        continue
    break