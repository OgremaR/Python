from random import *
def do_random():
    random = randint(1, 100)
    while do_random != 'Вы угадали, поздравляем!':
        x = int(input('Пропробуй угадать число, введи его: '))
        if x == random:
            return 'Вы угадали, поздравляем!'
        elif x > random:
            print('Слишком много, попробуйте еще раз')
        else:
            print('Слишком мало, попробуйте еще раз')

print(do_random())