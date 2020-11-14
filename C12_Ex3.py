import urllib.request, urllib.parse, urllib.error

url = input("Enter url - ")

text = urllib.request.urlopen(url)
count = 0

while True:
    doc = text.read(512)
    if len(info) < 1:   break
    count += len(doc)
    if count <= 3000:
        print(doc.decode(), end='')
print("Overall number of characters in the document is",count)
