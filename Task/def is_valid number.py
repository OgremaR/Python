# Функция
def is_valid(n):
    if n.isdigit() == True and 1 <= int(n) <= 100:
        return True
    else:
        False

# Импорт и переменные
from random import randrange
a = randrange(1, 101)
x = False
print('Добро пожаловать в числовую угадайку')

# Цикл проверки введеного числа
while x != True:
    n = input('Введите пожалуйста число от 1 до 100 - ')
    if is_valid(n) != True:
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        n = int(n)
        x = True

print(n*n) # Проверка - стереть строку