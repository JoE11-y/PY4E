fhand = open("words.txt")
lines = fhand.read()
lines.rstrip()
story = lines.split()
print(len(story))
count = 0
Dct = dict()

''' This was done to test for the fact that lists actually removed doubles
clean_story = list()
for item in story:
    if item in clean_story: continue
    clean_story.append(item)

for item in clean_story:
    count = count + 1
    Dct[item] = count
    print(Dct)
'''#print(story)

for item in range(len(story)): #turns items to the indices of the list story
    Dct[story[item]] = 1 #creating a dictionary

'''
to check for the keys use a particular word from the word.txt
if key in Dct:
    print(found)
'''

vals = list(Dct.values()) #to check for values in the dictionary
if 2 in vals:
    print("yes")
if 1 in vals:
    print("6 found")

#print(vals)
