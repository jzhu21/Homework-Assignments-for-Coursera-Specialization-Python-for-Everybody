# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:03:40 2021

@author: Jing
"""

import xml.etree.ElementTree as ET
import sqlite3

# The below line of code will create the trackdb file when it runs
# conn is for connect
conn = sqlite3.connect('trackdb.sqlite')
# Cursor: Database handle
cur = conn.cursor()


# Make some fresh tables using executescript()
# The DROP TABLE code will do nothing the first time through
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name       TEXT UNIQUE
);

CREATE TABLE Genre (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name       TEXT UNIQUE
);

CREATE TABLE Album (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title      TEXT UNIQUE
);

CREATE TABLE Track (
    id        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title     TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len       INTEGER, 
    rating    INTEGER,
    count     INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
# We want to see all of the tracks, dictionary tag within dictionary tag
# So we get Artist, Album, etc.
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

# The following block of code populates the SQL database with data parsed from the xml.
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None: 
        continue

    print(name, artist, album, genre, count, rating, length)

    # The artist name is unique. INSERT OR IGNORE: if it's already there, 
    # Don't insert it again. Don't blow up.
    # (artist, ) is a tuple. 
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # Insert or replace: means to update it. 
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
    
    
cur.executescript('''
    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
''')
conn.commit()
