from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

#http://py4e-data.dr-chuck.net/known_by_Fikret.htm
#
def html_reader(url, times = 1, sequence = " "):

    if times == 1:
        name = re.findall('http://.+_([A-Za-z]+)', url)
        sequence += "".join(name) + " "

    if times > 7:
        return print("Sequence of names: {}".format(sequence))

# Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a') #creates of tags of a

    count = 1
    for tag in tags:
        if count > 18:   break
        url = tag.get("href")
        if count == 18:
            sequence += tag.get_text() + " "
        count += 1

    times += 1

    html_reader(url, times, sequence)

    return "Done"

url = input("Enter url - ")
print(html_reader(url))
