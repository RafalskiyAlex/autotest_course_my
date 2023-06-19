# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

def generate_random_name():
    while True:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        random1=random.randint(1,15)
        random2 = random.randint(1, 15)
        str = ''.join(random.choice(letters) for i in range(random1))
        str1 = ''.join(random.choice(letters) for i in range(random2))
        yield f'{str} {str1}'

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))