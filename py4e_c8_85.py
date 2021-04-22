# Exercise 8.5

fname = input("Enter file name: ")
# Open the file mbox-short.txt and read it line by line

file = open(fname)

count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    words = line.split()
    email = words[1]
    print(email)
    count = count + 1

print("There were",count,"lines in the file with From as the first word")
