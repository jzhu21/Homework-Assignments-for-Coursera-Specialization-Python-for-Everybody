# Chapter 7- Files. Worked exercise 7.1

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (p. 120). Kindle Edition.
file_n = input("Enter the file name: ")

file = open(file_n, 'r')

for line in file:
    line = line.rstrip()
    print(line.upper())
