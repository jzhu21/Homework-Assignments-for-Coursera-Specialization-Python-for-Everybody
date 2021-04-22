# Chapter 6, worked exercise 6.3

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (p. 104). Kindle Edition.
str = 'X-DSPAM-Confidence: 0.8475'

clpos = str.find(":")
num = str[clpos+2:]
num_f = float(num)
print(num_f)
