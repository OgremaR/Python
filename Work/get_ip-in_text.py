file = open('kraken.md').read().split('\n')
reslt, r = open("result.md", "w"), ""
for i in file:
    r += i[53:65] + '\n'
reslt.write(r)
