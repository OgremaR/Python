i = 100
count = 0
while i <= 200:
    if i % 3 == 0:
        print(i, end=" ")
        count += i
    i += 1
print(f"\n{count}")