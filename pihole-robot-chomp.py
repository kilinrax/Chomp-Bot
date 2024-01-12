#!/usr/bin/env python

import json
import random
import requests
import time

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import scrollphathd

IMAGE_BRIGHTNESS = 0.5
FILE_BASE = '/home/pi/chompbot'

images = []

def load_image(filename):
    img = Image.open(filename)
    buffer = []
    for x in range(0, 17):
        buffer.append([])
        for y in range(0, 7):
            buffer[x].append(get_pixel(img, x, y))
    images.append(buffer)

def get_pixel(img, x, y):
    p = img.getpixel((x,y))
    if img.getpalette() is not None:
        r, g, b = img.getpalette()[p:p+3]
        p = max(r, g, b)
    elif type(p) is tuple:
        p = max(p)
    return (p / 255.0)

load_image(FILE_BASE+'/robot_chomp_open.bmp')
load_image(FILE_BASE+'/robot_chomp.bmp')

def chomp():
    for c in range(6):
        for img in images:
            for x in range(0, 17):
                for y in range(0, 7):
                    brightness = img[x][y]
                    scrollphathd.pixel(x, 6-y, brightness * IMAGE_BRIGHTNESS)
                #time.sleep(0.00001)
            scrollphathd.show()
            time.sleep(0.2)

f = open(FILE_BASE+'/apitoken')
API_TOKEN = f.readline().rstrip()
api_url = "http://localhost/admin/api.php?summaryRaw&auth="+API_TOKEN

blocked_count = 0
try:
    while True:
        try:
            r = requests.get(api_url)
            data = json.loads(r.text)
            blocked_today = data['ads_blocked_today']
        except KeyError:
            time.sleep(1)
            continue
        if blocked_today > blocked_count:
            print(blocked_today)
            chomp()
            blocked_count = blocked_today
        else:
            scrollphathd.fill(0)
            scrollphathd.show()
        time.sleep(1)
except KeyboardInterrupt:
    scrollphathd.clear()
    scrollphathd.show()
