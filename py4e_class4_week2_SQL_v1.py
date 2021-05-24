# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:36:11 2021

@author: Jing
"""


import sqlite3

# The below line of code will create the emaildb file when it runs
# conn is for connect
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# The following code will do nothing the first time through
cur.execute('DROP TABLE IF EXISTS Counts')

# Pretend the content in the () is a dictionary. 
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]
    # The following section is like the dictionary part
    # The ? is a placeholder. Do not allow SQL injection. It will be replaced by email
    # (email,) is a tuple with nothing in it. 
    # This is not really reading the data. We are opening a set of records
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    # row is info we get from the database. 
    row = cur.fetchone()
    # If row is not there, we will insert something
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
