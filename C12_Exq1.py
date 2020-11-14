from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

lst = []

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#url http://py4e-data.dr-chuck.net/comments_431514.html
#url http://py4e-data.dr-chuck.net/comments_42.html
# code is to count the sum of the numbers in the page
url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("span")
#<span class="comments">7</span>
for tag in tags:
    t = tag.get_text()
    t = int(t)
    lst.append(t)

print(sum(lst))
