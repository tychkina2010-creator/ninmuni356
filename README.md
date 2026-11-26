import random
a = random.randint(1, 6)
b = random.randint(1, 6)
sum = a + b
print("Первый кубик:", a)
print("Второй кубик:", b)
print("Сумма:" sum)
if a == b:
    print("Дубль!")
elif sum == 7 or sum == 11:
    print("Джекпот!")
else:
    print("Обычный ход суммой", sum)
n = input("Бросить ещё? (да/нет)": ).strip().lower()
if n != "да":
    print("Игра окончена!")
    break ninmuni356
