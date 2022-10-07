n = int(input('Проезжает в день км: '))
m = int(input('КМ маршрута: '))
a = m // n
b = m % n
c = b // (b+1)
print(a+c)