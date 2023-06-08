import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = input('Укажите количество паролей для генерации:')
N = input('Укажите длину одного пароля:')
num = input('Включать цифры? (y/n)')
low_c = input('Включать прописные буквы? (y/n)')
up_c = input('Включать строчные буквы? (y/n)')
pun_c = input('Включать символы "!#$%&*+-=?@^_"? (y/n)')
pun_b = input('Исключать неоднозначные символы "il1Lo0O"? (y/n)')


if num == 'y':
    chars += digits
if low_c == 'y':
    chars += lowercase_letters
if up_c == 'y':
     chars += uppercase_letters
if pun_c == 'y':
     chars += punctuation
if pun_b == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
print(chars)
