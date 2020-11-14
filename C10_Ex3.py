import string
fname  = input("Enter file name: ")
fhand = open(fname)
words = fhand.read()
words = words.strip()
words = words.translate(words.maketrans('','', string.punctuation))#removes punctuation
words = words.translate(words.maketrans('','', string.digits))#removes numbers
words = words.translate(words.maketrans('','', string.whitespace))#removes spaces
words = words.lower()

dic = dict()
for L in words:
    dic[L] = dic.get(L, 0) + 1

lst = list()
vlst = list()

for key, val in list(dic.items()):
    lst.append((key, val))
    vlst.append(val)

v = sum(vlst)
frq = 100/ v

lst.sort(reverse=False)
print("L F")
for key, val in lst:
    freq = val*frq

    print(key,"%.3f" %freq)

'''
#alternative using list comprehension
lst = sorted([(key,val) for key,val in dic.items()])
v = sum([val for key,val in dic.items()])
frq = 100/v
print([(key, "%.3f" %(int(val)*frq)) for key,val in lst])
'''
