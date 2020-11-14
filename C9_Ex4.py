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

vals = list(counts.values())
Max_Msg = None
for i in vals:
    if Max_Msg is None or i > Max_Msg:
        Max_Msg = i
for keys in counts:
    if counts[keys] == Max_Msg:
        print(keys, Max_Msg)

''' alternative using tuples
bigcount = None
bigword = None
for key, value in list(counts.items()):
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value

print(bigword, bigcount)
'''
