#!/usr/bin/env python
# -*- coding: utf-8 -*-

from caca.canvas import Canvas
from PIL import Image
from io import BytesIO


def first_demo():
    c = Canvas(5, 5)
    c.fill_box(0, 0, 5, 5, "#")
    c2 = Canvas(2, 2)

    c2.put_str(0, 0, "x")
    c2.put_str(1, 0, "x")
    c2.put_str(1, 1, "x")
    c2.put_str(0, 1, "x")

    c.blit(1, 2, c2)
    print(c.export_to_memory("irc"))

# first_demo()

cv = Canvas(80, 80)
img = Image.open("./cyberpunk1.jpg").convert("L").resize((80, 80))  # Open, "L" converts to luminscience mode, used for greyscale, resize it
cv.put_str(0, 0, img)
