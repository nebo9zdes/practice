import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = input('Укажите количество паролей для генерации:')
N = input('Укажите длину одного пароля:')
low_c = input('Включать прописные буквы? (y/n)')
up_c = input('Включать строчные буквы? (y/n)')
pun_c = input('Включать символы "!#$%&*+-=?@^_"? (y/n)')
pun_b = input('Исключать неоднозначные символы "il1Lo0O"? (y/n)')
