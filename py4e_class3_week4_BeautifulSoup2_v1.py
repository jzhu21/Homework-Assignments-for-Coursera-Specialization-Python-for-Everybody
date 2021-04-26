# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for input data
url = input('Enter url:')
enter_count = input('Enter count: ')
enter_position = input('Enter position: ')

# Convert string to integer
enter_count = int(enter_count)
enter_position = int(enter_position)

# Start from the given URL, find the 3rd link, and repeat 4 times

counter = 0
while counter <= enter_count:
    if counter == 0:
        name = re.findall('by_([a-zA-Z]+)', url)
        counter = counter + 1
        print(name)
    else:
        url_list = list()
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        for tag in tags:
            url = tag.get('href', None)
            url_list.append(url)
        url = url_list[enter_position-1]
        print(url)
        counter = counter + 1

# Extract the last person's last name and print it
final_name = re.findall('by_([a-zA-Z]+)', url)
print(final_name)
    