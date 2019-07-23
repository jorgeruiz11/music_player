import os
import sqlite3
from mutagen.id3 import *

class DAO():

    def __init__(self):
        self.rolas = []

    def create_database(self, rolas):
        #pathway = os.path.expanduser('~/.local')
        #route = pathway + '/' + 'rolas.db'
        connection = sqlite3.connect('rolas.db')
        id_type = 2 #Comenzamos con 2 porque es el tipo por omisión.
        cur = connection.cursor()
        i = 0

        for rola in rolas:
            cur.execute("SELECT path FROM rolas")
            obtain = cur.fetchall()

            artist = rola.get_artist()
            title = rola.get_title()
            album_name = rola.get_albumname()
            album_numer = int(rola.get_albumnumer())
            path_rola = rola.get_path()
            year = int(rola.get_year())
            genre = rola.get_genre()

            #if path_rola in obtain:
                #pass
            cur.execute("INSERT INTO performers (id_type, name) VALUES (?,?)", (id_type, artist,))
            cur.execute("INSERT INTO groups (name) VALUES (?)", (artist,))
            cur.execute("INSERT INTO albums (path, name, year) VALUES (?,?,?)", (path_rola, album_name, year,))

            cur.execute("SELECT id_performer FROM performers")
            id_performer = cur.fetchall()
            cur.execute("SELECT id_album FROM albums")
            id_album = cur.fetchall()

            cur.execute('''INSERT INTO rolas (id_performer,id_album,path,title,track,year,genre) VALUES (?,?,?,?,?,?,?)''',
            (id_album.pop(len(id_album)-1)[0],id_performer.pop(len(id_performer) - 1)[0],path_rola,title,int(album_numer),int(year),genre,))
            # id_album.pop(len(id_album)-1)[0],id_performer.pop(len(id_performer) - 1)[0],rola.path_rola,title,int(album_numer),int(year),genre,)
            i+=1
            connection.commit()
