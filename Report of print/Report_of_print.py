OIDTotalPages = ".1.3.6.1.2.1.43.10.2.1.4.1"
OIDPrinterName = ".1.3.6.1.2.1.25.3.2.1.3"
#Date = Get-Date -Format 'yyyy-MM-dd-hh-mm-ss' -OutVariable date
file = open('Printers.txt').read().split('\n')
printers = []
for line in file:
    printers.append(line.split())
for i in printers:
    kab = i[0]
    ip = i[1]
    print()
