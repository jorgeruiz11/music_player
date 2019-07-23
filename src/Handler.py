from Miner import Miner
from DataBase import DataBase
from DAO import DAO

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


def main():
    db = DataBase()
    db.connect()
    m = Miner()
    m.get_files()
    m.get_tags()
    m.insert()

if __name__ == '__main__':
    main()
