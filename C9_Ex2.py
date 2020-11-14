fname = input("Enter file name: ")

''' The method I created during my first trial
fhand = open(fname)
counts = dict()
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith("From"):
        words = lines.split()
        if words[0] ==  "From:":    continue
        for item in range(len(words)):
            if item != 2:   continue

            #(Basic style of counting doubles in dictionaries)
            #if words[item] not in counts:
            #    counts[words[item]] = 1
            #else:
            #    counts[words[item]] += 1

            # Python's own method
            counts[words[item]] = counts.get(words[item],0) + 1

print(counts)
'''
#Alternative Method without using rstripand startswith
fhand = open(fname)
counts = dict()
for lines in fhand:
    words = lines.split()
    if len(words) == 0: continue #to skip empty lines if there exists any.
    if words[0] != "From": continue
    for item in range(len(words)):
        if item != 2: continue
        counts[words[item]] = counts.get(words[item],0) + 1

print(counts)
