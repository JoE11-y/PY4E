fname = input("Enter file name: ")
fhand = open(fname)
counts = dict()
for lines in fhand:
    words = lines.split()
    if len(words) == 0: continue #to skip empty lines if there exists any.
    if words[0] != "From": continue
    for item in range(len(words)):
        if item != 1: continue
        counts[words[item]] = counts.get(words[item],0) + 1

print(counts)
