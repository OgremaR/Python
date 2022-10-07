import random

def generate_password(length, chars):
    n = []
    for _ in range(length):
        n += random.choice(chars)
    return n

digits = ['2','3','4','5','6','7','8','9']
lowercase_letters = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']
uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
punctuation = ['!','#','$','%','&','*','+','-','=','?','@','^','_']
chars = []

number_pass = int(input('Напиши количество паролей для генерации - '))
len_pass = int(input('Какая длина одного пароля - '))
digit_question = input('Должен ли пароль включать цифры? (y/n) ').lower()
lower_question = input('Должен ли пароль включать большие буквы? (y/n) ').lower()
upper_question = input('Должен ли пароль включать маленькие буквы? (y/n) ').lower()
symbols_question = input('Должен ли пароль включать символы? (y/n) ').lower()
symbols2_question = input('Должен ли пароль включать "il1Lo0O" символы? (y/n) ').lower()

if digit_question == 'y':
    chars += digits
if lower_question == 'y':
    chars += lowercase_letters
if upper_question == 'y':
    chars += uppercase_letters
if symbols_question == 'y':
    chars += punctuation
if symbols2_question == 'y':
    chars += 'il1Lo0O'

for _ in range(number_pass):
    print(*generate_password(len_pass, chars), sep='')