fileRU = open('fileRU_10m.md').read().split(' ')
fileCOM = open('fileCOM_10m.md').read().split(' ')
files = fileRU + fileCOM
res, r, temp = open("likcks.md", "w"), [], ""
for link in files:
    if ".ru" in link or ".com" in link:
        if "//" in link:
            if ".com" in link:
                r.append(link.rpartition('.com')[0]+'.com')
            else:
                r.append(link.rpartition('.ru')[0]+'.ru')
        else:
            r.append(link)
r.sort()
for i in r:
    temp += str(i) + "\n"
res.write(str(temp))