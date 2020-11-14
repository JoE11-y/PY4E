fname = input("Enter file name: ")
fhand = open(fname)
counts = dict()


for lines in fhand:
    words = lines.split()
    if len(words) == 0: continue #to skip empty lines if there exists any.
    if words[0] != "From": continue
    for i in range(len(words)):
        if i != 1:   continue
        wor = words[i]
        dmn = wor.find("@")
        domain = wor[dmn+1:]
'''
        name, domain = wor.split("@")
        #Using tuples to do it
'''
        counts[domain] = counts.get(domain,0) + 1

print(counts)
