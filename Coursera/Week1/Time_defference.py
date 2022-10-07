s1 = int(input('S1: '))
m1 = int(input('M1: '))
h1 = int(input('H1: '))
s2 = int(input('S2: '))
m2 = int(input('M2: '))
h2 = int(input('H2: '))
sum1 = (s1 + (m1 * 60) + (h1 * 3600)) % 86400
sum2 = (s2 + (m2 * 60) + (h2 * 3600)) % 86400
print('Разность в секундах составила:',sum1 % sum2)