file = open('links.md').read().split("\n")
reslt = open("result.md", "w")
value, links = list(set(file)), dict()
links = dict.fromkeys(value, 0)
for link in value:
    for i in file:
        if i == link:
            links[i] += 1
srt_links = dict(sorted(links.items(), key=lambda item: item[1], reverse=True))
print(srt_links)
reslt.write(str(srt_links))