fname = input('Enter the file name: ')
'''
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()

    if line.startswith("From"):
        words = line.split()

        if words[0] == "From:": continue

        count += 1
        print(words[1])

print("There were %d lines in the file with From as the first word." %count)

''' #Alternative method without using rstrip to remove new enter lines and without using startswith
fhand = open(fname)
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 : continue #to skip empty lines if there exists any
    if words[0] != 'From' : continue
    count += 1
    print(words[1])
print("There were {} lines in the file with From as the first word." .format(count))
