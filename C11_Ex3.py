import re
lst = list()
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        for item in x:
            item = int(item)
            lst.append(item)
print(int(sum(lst)/len(lst)))
