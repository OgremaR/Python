n = int(input('секунд: '))
s = n % 60
m = n // 60 % 60
h = n // 3600
print(h % 24,':',m,':',s, sep='')