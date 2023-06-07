import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

print('Введите следующие данные:')
n = int(input('Количество паролей для генерации'))
N = int(input('Длину одного пароля'))

print('Включать прописные буквы?')
answer = input('Y или N')
if answer == 'Y':
    chars += lowercase_letters
else:
    chars += 0


