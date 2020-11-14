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
        counts[wor] = counts.get(wor,0) + 1

lst = list()
for key, value in list(counts.items()):
    lst.append((value, key))

lst.sort(reverse=True)

for value, key in lst[:1]:
    print(key, value)
