import random
print('Добро пожаловать в числовую угадайку')

num1 = random.randint(1, 101)


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


while True:
    num2 = input('Введите число от 1 до 100')
    if is_valid(num2) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        num2 = int(num2)
        break


count = 0
while True:
    count += 1
    if num2 == num1:
        print('Вы угадали, поздравляем!')
        break
    if num2 < num1:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    if num2 > num1:
        print('Ваше число больше загаданного, попробуйте еще разок')
    num2 = int(input('Введите число от 1 до 100'))

print('Количество ваших попыток:', count)
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
