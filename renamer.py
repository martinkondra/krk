#!/usr/bin/env python
#-- coding: utf-8 --

_author_ = "Martin Kondra"

import os
import re

#carpeta donde están los directorios
path = '/media/martinkondra/Lexar/KARAOKE ANIVERSARIO + QUETZAL/'

for f in os.listdir(path):
    newName = re.sub(r'^(\d+\.\s?)', '', f)
    print newName
    os.rename(path + f, path + newName)

output = open('listaKrk.txt', 'w')
i = 0
for f in sorted(os.listdir(path)):
    print f,
    newName = f.lower()
    newName = re.sub('\(.*\)', '', newName)
    newName = re.sub('[!\'\"$%]', '', newName)
    newName = re.sub('\[.*\]', '', newName)
    newName = re.sub('karaoke|Karaoke|KARAOKE|MIX|mix|box', '', newName)
    newName = re.sub('\s\s', ' ', newName)
    newName = re.sub('^\s*', '', newName)
    newName = re.sub('\s*\.mp4', '.mp4', newName)
    newName = re.sub('\W*\.mp4', '.mp4', newName)
    newName = str(i) + ". " + newName
    print newName
    output.write(newName + '\n')
    os.rename(path + f, path + newName)
    i += 1