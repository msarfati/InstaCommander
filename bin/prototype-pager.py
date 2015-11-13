#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Prototype for InstaCommander
import sys
import os
sys.path.insert(0, '.')
MODULE_PATH = os.path.split(os.path.realpath(__file__))[0]

from instagram.client import InstagramAPI
import requests
from objectpath import Tree

view = """\
--------

{0.user}
{0.created_time}
{0.link}

{0.images[low_resolution].url}

Likes: {0.like_count}
Comments: {0.comment_count}
{0.tags}\
"""

access_token = 'b8fd789f28cc4db8801fcda9a733e3ae'
client_secret = 'b7f009145f604e6190f420ef1d3ec350'

# Unauthenticated Client
# client = InstagramAPI(client_id='b8fd789f28cc4db8801fcda9a733e3ae')

# Unauthenticated Client
# client = InstagramAPI(
#     access_token=access_token,
#     client_secret=client_secret,
# )

# Unauthorized Client
client = InstagramAPI(
    client_id='b8fd789f28cc4db8801fcda9a733e3ae',
    client_secret='b7f009145f604e6190f420ef1d3ec350',
)

feed = client.media_popular()
for post in feed:
    print(view.format(post))

# # Manipulate image
# post = feed[0]
# img = post.images['standard_resolution']  # Image object is returned
# img.url
# img.height
# img.width


# redirect_uri = client.get_authorize_login_url(scope='basic')
# response = requests.get(redirect_uri)

# print("--- Welcome to the InstaCommander prototype. ---\n")
