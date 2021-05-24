# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

name = input("Enter file:")
# Check if user entered correct file name
if len(name) < 1 :
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print('File cannot be opened:',name)
    quit()

# Create a list of emails of all senders
emails = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        email = words[1]
        emails.append(email)

# Count the frequency of each email
counts = dict()
for email in emails:
    counts[email] = counts.get(email, 0) + 1

# Find the most frequent email
largest = None
winner = None
for key in counts:
    if largest is None:
        largest = counts[key]
    elif counts[key] > largest:
        largest = counts[key]
        winner = key
    else:
        continue

print(counts)
# print(winner, largest)
