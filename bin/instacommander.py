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
from instacommander.images import ANSIImage
from instacommander import renderers

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

# Unauthorized Client
client = InstagramAPI(
    client_id='b8fd789f28cc4db8801fcda9a733e3ae',
    client_secret='b7f009145f604e6190f420ef1d3ec350',
)

get_tty_width = lambda: int(os.popen('stty size').read().split()[1])
# output_size = round(get_tty_width() / 1.15)  # Leaves a margin
width = get_tty_width()


def ansi_feed():
    feed = [i for i in client.media_popular() if i.type == 'image']  # Filter for only images
    for post in feed:
        img = BytesIO(requests.get(post.images['standard_resolution'].url).content)
        img = ANSIImage(img, width)
        # img = A(img, output_size)
        print(view.format(media=post, img=img.stream))


def ascii_feed():
    feed = [i for i in client.media_popular() if i.type == 'image']  # Filter for only images
    for post in feed:
        img = BytesIO(requests.get(post.images['standard_resolution'].url).content)
        img = renderers.to_ascii(img, width)
        print(view.format(media=post, img=img))


def main():
    # ansi_feed()
    ascii_feed()


if __name__ == '__main__':
    main()
