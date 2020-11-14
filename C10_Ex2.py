fname  = input("Enter file name: ")
fhand = open(fname)
counts = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != "From":  continue
    timeStr = words[-2]
    timeSpl = timeStr.split(":")
    hour = timeSpl[0]
    counts[hour] = counts.get(hour,0) + 1

lst = list()
for key, value in list(counts.items()):
    lst.append((key, value))
lst.sort(reverse=False)

for key, value in lst:
    print(key, value)

#another method using list comprehension
#print(sorted([(val,key) for k,v in list.items()]))


''' Alternative method to get the hour
    line.rstrip()
    if not line.startswith("From"): continue
    if line.startswith("From:"): continue

    id = line.find(":")
    hour = line[id-2:id]
    counts[hour] = counts.get(hour,0) + 1
'''




#print(counts)
