# Проверка на простое число
def is_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Проверка на четное число
def is_even(n):
    return n % 2 == 0

# Если параместры фунции простые и четные числа,
# то вернем сумму этих чисел, а иначе вернем произведение этих чисел
def calc(a,b):
    if is_even(a) and is_even(b) and is_simple(a) and is_simple(b):
        return a + b
    return a * b

