import re

lst = []
fname = input("Enter file: ")
fhand = open(fname)
for line in fhand:
    y = re.findall("[0-9]+", line)
    if len(y) == 0: continue
    for item in y:
        item = int(item)
        lst.append(item)
print(sum(lst))
print(len(lst))
