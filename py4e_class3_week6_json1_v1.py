# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:10:38 2021

@author: Jing
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for URL
myurl = input('Enter URL Here: ')

# Read data from URL
json_text = urllib.request.urlopen(myurl, context=ctx)
data = json_text.read()
mystring = data.decode()

# Parse Json code
info = json.loads(mystring)
# print(info)


# Count the total number of names and sum up the count
total = 0
mycount = 0
for item in info['comments']:
    #print('Name', item['name'])
    #print('Count', item['count'])
    number = int(item['count'])
    total = total + number
    mycount = mycount + 1

print(total)