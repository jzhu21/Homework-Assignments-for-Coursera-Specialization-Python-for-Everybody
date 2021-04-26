import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

myurl = input('Enter URL Here: ')
uh = urllib.request.urlopen(myurl, context=ctx)
data = uh.read()
mystring = data.decode()
tree = ET.fromstring(mystring)

lst = tree.findall('comments/comment')

print(lst)

total = 0
mycount = 0
for item in lst:
    #print('Name', item.find('name').text)
    #print('Count', item.find('count').text)
    number = int(item.find('count').text)
    total = total + number
    mycount = mycount + 1
    
print('Sum:', total)
print('Count:', mycount)

