import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter location: ")
    if len(url) < 1: break


    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    #print(json.dumps(info, indent=2))

    lst = []
    for item in info["comments"]:
        vals = item["count"]
        lst.append(vals)

    print("count: ", len(lst))
    print("sum: ", sum(lst))
