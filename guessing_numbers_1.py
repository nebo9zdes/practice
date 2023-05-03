import random

num1 = random.randint(1, 100)
num2 = int(input())

while True:
    if num1 == num2:
        print('Вы угадали, поздравляем!')
        break

    if num1 > num2:
        print('Слишком мало, попробуйте еще раз')

    if num1 < num2:
        print('Слишком много, попробуйте еще раз')
    num2 = int(input())
