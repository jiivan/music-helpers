#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

def main():
    path = "/home/jiivan/Music/Kapela ze Wsi Warszawa/Uprooting/Warsaw Village Band - uprooting - 1 - Roots; J˘zef Lipiďnski.mp3"
    path = "/media/jiivan/WALKMAN/Kapela ze wsi warszawa/Uprooting/Warsaw Village Band - uprooting - 1 - Roots; J˘zef Lipiďnski.mp3"
    print "*"*50
    print EasyID3.valid_keys.keys()
    print "*"*50
    audio = MP3(path, ID3=EasyID3)
    print audio.pprint()

if __name__ == '__main__':
    main()
