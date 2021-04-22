# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

name = input('Enter file name: ')
# Check if user entered correct file name
if len(name) < 1 :
    name = "regex_sum_42.txt"
try:
    handle = open(name)
except:
    print('File cannot be opened:',name)
    quit()

# Find all numbers in the txt file.
import re

sum_all = 0
numbers = list()
for line in handle:
    if len(line)>1:
        line = line.rstrip()
        number_inline = re.findall('[0-9]+', line)
        for number in number_inline:
            numbers.append(number)
            n = int(number)
            sum_all = sum_all + n

print(numbers)
print(sum_all)
