n = int(input())
good_grade = []
main_tuple = []
for i in range(n):
    main_tuple.append(input().split())
    temp = main_tuple[i][-1]
    if int(temp) >= 4:
        good_grade.append(main_tuple[i])

for i in main_tuple:
    print(*i)
print()
for i in good_grade:
    print(*i)