import re
s = input().lower()
s = re.sub("[.|,|!|?|:|;|-]", "", s).split()
w, answer = {}, []
for i in s:
    w[i] = w.setdefault(i, 0) + 1
for key, value in w.items():
    if value == min(w.values()):
        answer.append(key) 
print(min(answer))