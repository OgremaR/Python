def is_valid(n):
    x = False
    while x != True:
        if n.isdigit() == True and 1 <= int(n) <= 100:
            x = True
            n = int(n)
            return n
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            n = input('Введите пожалуйста число от 1 до 100 - ')

def do_random():
    counter = 0
    a = randrange(1, 101)
    while do_random != 'Вы угадали, поздравляем!':
        n = is_valid(n = input('Введите пожалуйста число от 1 до 100 - '))
        if n < a:
            counter += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > a:
            counter += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            return print('Вы угадали, поздравляем!'), print('Количество попыток угадать число', counter)

from random import randrange
print('Добро пожаловать в числовую угадайку')
do_random()
while True:
    b = input('Хотите продолжить нажмите +. Если нет, то любой другой символ. \n')
    if b == '+':
        do_random()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break