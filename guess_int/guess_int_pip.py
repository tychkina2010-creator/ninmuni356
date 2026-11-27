
import random 

dice = random.randint 


import random
while True:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sum = a + b
    print("Первый кубик:", a)
    print("Второй кубик:", b)
    print("Сумма:", sum)
    if a == b:
        print("Дубль!")
        n = input("Бросить ещё? (да/нет):" ).strip().lower() 
        if n != "да":
            print("Игра окончена!")
            break 
    elif sum == 7 or sum == 11:
        print("Джекпот!")
        n = input("Бросить ещё? (да/нет):" ).strip().lower() 
        if n != "да":
            print("Игра окончена!")
            break 
    else:
        print("Обычный ход суммой", sum)
        n = input("Бросить ещё? (да/нет):" ).strip().lower() 
        if n != "да":
            print("Игра окончена!")
            break 

import random 
number = random.randint(1, 100)
count = 0 
print("Я загадала число от 1 до 100. Угадай!")
while True: 
    guess = int(input("Выведи число: "))
    count = count + 1
    if guess < number: 
        print("БОЛЬШЕ")
    elif guess > number:
        print("МЕНЬШЕ")
    else:
        print("Ты угадал!")
        print("Число попыток: ", count)
        break 
