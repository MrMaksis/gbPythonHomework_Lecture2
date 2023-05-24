import random

nMoney = [random.randint(0, 1) for _ in range(5)]

print(nMoney)

count_heads = nMoney.count(1)  # количество монеток гербом
count_tails = nMoney.count(0)  # количество монеток решкой

if count_heads == 0 or count_tails == 0:
    print("Все монетки лежат одной стороной")
else:
    print(f"Число монеток лежащие решкой: {count_tails}")