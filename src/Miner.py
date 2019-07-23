import os
from Rola import Rola
from DAO import DAO
from mutagen.id3 import ID3

class Miner():

    def __init__(self):
        self.files = []
        self.rolas = []

    def get_files(self):
        route = os.path.expanduser('~/Música')

        for root, directoryname, filename in os.walk(route):
            for file in filename:
                self.files.extend([os.path.join(root, file)])

    # Método que dada la ruta absoluta de una canción intenta obtener sus
    # etiquetas. Si tiene las etiquetas, las regresa. En caso de no tenerlas
    # le asignará un valor predeterminado.
    def get_tags(self):
        for i in self.files:
            audio = ID3(i)
            rola = Rola()

            path_rola = rola.property_path(i)

            if 'TIT2' in audio:
                title = rola.property_title(str(audio['TIT2']))
            else:
                title = rola.property_title('Unknown')

            if 'TPE1' in audio:
                artist = rola.property_artist(str(audio['TPE1']))
            else:
                artist = rola.property_artist('Unknown')

            if 'TALB' in audio:
                album = rola.property_albumname(str(audio['TALB']))
            else:
                album = rola.property_albumname('Unknown')

            if 'TDRC' in audio:
                year = rola.property_year(str(audio['TDRC']))
            else:
                year = rola.property_year(0)

            if 'TCON' in audio:
                genre = rola.property_genre(str(audio['TCON']))
            else:
                genre = rola.property_genre('Unknown')

            if 'TRCK' in audio:
                n = str(audio['TRCK'])
                try:
                    r = int(n)
                    number = rola.property_albumnumer(n)
                except:
                    l = n.split('/',1)
                    rola.property_albumnumer(l[0])
            else:
                number = rola.property_albumnumer(0)

            self.rolas.append(rola)

            print(rola.get_path())
            print(rola.get_title())
            print(rola.get_artist())
            print(rola.get_albumname())
            print(rola.get_year())
            print(rola.get_genre())
            print(rola.get_albumnumer())
            print('-------------------------------')

    def insert(self):
        dao = DAO()
        dao.create_database(self.rolas)
