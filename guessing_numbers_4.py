import random
print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= right_n

def game():
    while True:
        right_n = input('Введите правую границу угадываемого диапазона чисел')
        num1 = random.randint(1, int(right_n) + 1)
        num2 = input(f'Введите число от 1 до {right_n}?')
        if 1 <= int(num2) <= int(right_n) == False:
            print(f'А может быть все-таки введем целое число от 1 до {right_n}?')
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
        num2 = int(input(f'Введите число от 1 до {right_n}'))

    print('Количество ваших попыток:', count)
    print('Сыграем ещё?')

game()

while True:
    answer = input('Введите Y, если согласны, или N, если нет')
    if answer == 'Y':
        game()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
