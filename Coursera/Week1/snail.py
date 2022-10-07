h = int(input('Шест длиной м.: '))
a = int(input('Проползает за день: '))
b = int(input('Сползает за ночь: '))
d = h // (a - b)
d1 = (a - b) * d
d2 = h % d1
d3 = d2 // (d2+1)
print(d+d3)