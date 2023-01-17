# Оператор * упаковывает значение в список
def sum_numbers(a,b,*x):#х - это список, который содержит все оставшиеся значения
    s = a + b
    for i in x:
        s+= i
    print(s)

sum_numbers(1,2,3,4,5)


# Функция может возвращать несколько значенией в виде кортежа
def func():
    return 10,20 # Выполняется упаковка в значение кортеж
print(func())


# Вложенные функции - имеют прямой доступ к любым переменным внешней фунции
def pc(title):
    def ram(size):
        print(f'ПК {title} имеет размер оперативной памяти: {size}Mb')
    def hard(size):
        print(f'ПК {title} имеет размер оперативной памяти: {size}Mb')
    return ram, hard

# print(pc('Acer')[1](800))
info = pc('Acer') #получил кортеж из двух функций
ram = info[0] #обращаемся к любому возвращаемому значению по индексу
hard = info[1]

ram(1000)


# Пример 1
def calc(a,b):
    def sum():
        return a + b
    def dif():
        return a - b
    def comp():
        return a * b
    def div():
        if b != 0:
            return a / b

    return sum,dif,comp,div

print(calc(2,4)[2]()) # скобки запускают функцию. Индекс 2, т.к. функция comp на 3 месте в возращаемом значении, а индексация начинается с нуля


# Пример 2
def cal(sign):
    def sum(a,b):
        return a + b
    def dif(a,b):
        return a - b
    def comp(a,b):
        return a * b
    def div(a,b):
        if b != 0:
            return a / b
    if sign == '+':
        return sum
    if sign == '-':
        return dif
    if sign == '*':
        return comp
    if sign == '/':
        return div
print(cal('+')(2,3))


#Ананимные функции
def sum(a,b):
    return a + b
a = sum # Епеременной присвоить функцию без скобок, то переменная станет той функцией
print(a(1,2))

