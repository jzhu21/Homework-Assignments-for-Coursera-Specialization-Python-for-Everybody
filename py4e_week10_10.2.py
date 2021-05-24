# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
#   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


name = input('Enter file name: ')
# Check if user entered correct file name
if len(name) < 1 :
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print('File cannot be opened:',name)
    quit()

# Find all lines starting with 'From ', and extract the hour into list hours
hours = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        time = words[5]
        time_split = time.split(':')
        hour = time_split[0]
        hours.append(hour)

# Count the hours frequency
counts = dict()
for iter in hours:
    counts[iter] = counts.get(iter, 0) + 1

# Print out the hour with their counts
for k,v in sorted(counts.items()):
    print(k,v)
