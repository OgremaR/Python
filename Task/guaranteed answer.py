n = int(input())
counter = 0
while n != 1:
    if n % 2 == 1:
        n += 1
    n //= 2
    counter += 1
print(counter)