#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Prototype for InstaCommander
import sys
import os
sys.path.insert(0, '.')
MODULE_PATH = os.path.split(os.path.realpath(__file__))[0]

from instagram.client import InstagramAPI
import requests
from io import BytesIO

view = """\
--------
{img}

{media.user}
{media.created_time}
{media.link}
Likes: {media.like_count}
Comments: {media.comment_count}
{media.tags}\
"""

from PIL import Image
import random
from bisect import bisect


class ASCIIGenerator(object):

    def __init__(self):
        self.greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
        ]
        self.zonebounds = [36, 72, 108, 144, 180, 216, 252]

    def generate(self, img):
        im = Image.open(img)
        im = im.resize((160, 75), Image.BILINEAR)
        im = im.convert("L")

        str = ""
        for y in range(0, im.size[1]):
            for x in range(0, im.size[0]):
                lum = 255 - im.getpixel((x, y))
                row = bisect(self.zonebounds, lum)
                possibles = self.greyscale[row]
                str = str + possibles[random.randint(0, len(possibles) - 1)]
            str = str + "\n"

        return str

ascii_gen = ASCIIGenerator()

# Unauthorized Client
client = InstagramAPI(
    client_id='b8fd789f28cc4db8801fcda9a733e3ae',
    client_secret='b7f009145f604e6190f420ef1d3ec350',
)


def poll_feed():
    feed = [i for i in client.media_popular() if i.type == 'image']  # Filter for only images
    for post in feed:
        img = BytesIO(requests.get(post.images['low_resolution'].url).content)
        print(view.format(media=post, img=ascii_gen.generate(img)))


def main():
    poll_feed()


if __name__ == '__main__':
    main()
