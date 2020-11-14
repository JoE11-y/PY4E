fname = input('Enter the file name: ')

fhand = open(fname)
lines = fhand.read()
lines.rstrip()
words = lines.split()

Newlist = list()

for item in words: #this just uses the for loop directly to iterate
    if item in Newlist: continue
    Newlist.append(item)

print(Newlist)

#or
'''
# this method uses the indices(plural of index) to format each of the items one at a time
# and can be used to direct;y format a specific item in the list.

for item in range(len(words)):

    if words[item] in Newlist:  continue

    Newlist.append(words[item])

    Newlist.sort()

print(Newlist)

'''
