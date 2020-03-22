#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = "Martin Kondra"
'''
from pytube import YouTube

links = open('links.txt', 'r').readlines()
print(links)

n = 1
for i in links:
    print('downloading: ' + str(n) + ' ' + i)
    n += 1
    #try:
    #YouTube(i).streams.filter(subtype='mp4').filter(progressive=True).order_by('resolution').desc().first().download()
    YouTube(i).streams.filter(subtype='mp4').download()
    
    print('Ok: ' + i)
    #except Exception as e:
    # 	print(e)
    #    print '************************************Problems with ' + i

'''

import youtube_dl
import os

links = open('links.txt', 'r').readlines()
print(links)
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download(links)