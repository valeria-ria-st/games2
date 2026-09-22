import random
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Введите число: "))
    attempts += 1

    if guess < number:
        print("Не угадал! Загаданное число БОЛЬШЕ")
    elif guess > number:
        print("Не угадал! Загаданное число МЕНЬШЕ")
    else:
        print("Ты угадал число")
        print("Неудачных попыток: ", attempts - 1)
        break