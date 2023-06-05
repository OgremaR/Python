fileRU = open('fileRU_10m.md').read().split(' ')
fileCOM = open('fileCOM_10m.md').read().split(' ')
reslt = open("result.md", "w")
files, value = fileRU + fileCOM, []
for link in files:
    if ".ru" in link or ".com" in link:
        if "//" in link:
            if ".com" in link:
                value.append(link.rpartition('.com')[0]+'.com')
            else:
                value.append(link.rpartition('.ru')[0]+'.ru')
        else:
            value.append(link)
links = dict.fromkeys(value, 0)
for link in links:
    for i in value:
        if i == link:
            links[i] += 1
srt_links = dict(sorted(links.items(), key=lambda item: item[1], reverse=True))
summa = sum(srt_links.values())
srt_links['ВСЕГО_ОБРАБОТАННО'] = summa
reslt.write(str(srt_links))