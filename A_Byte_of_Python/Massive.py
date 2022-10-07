def height(m, cm):
    total = (m * 100) + cm
    print(str(total) + '_cm tall')
height(1,70)

def calc(a,b):
    total = a + b
    return total
summ = calc(4,5)
print(summ)

def multiply(a, b=10):
    return a*b
print (multiply(6,3))
