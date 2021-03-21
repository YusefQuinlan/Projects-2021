# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:11:19 2021

@author: Yusef quinlan
"""
# Imports from PIL so images can be drawn from text.
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
"""
Opens the file i.e. the file opens itself whilst running, then it takes all
of the text in itself and stores it in a variable, it also prints this text.
Including comments such as this one.
"""
with open("Self-Print-Image.py", "r") as f:
   x = f.read()
   print(x)

"""
    This creates a 600 * 600 image, the image is black RGB(0,0,0) .
    The image is then drawn into creation, and then the text overlay for the
    image is set to be the text contained within this file (including this),
    and will appear as white text RGB(255,255,255). This image is then saved
    as the file 'Self-Print-Image.jpg'
"""
img = Image.new('RGB', (600, 600), (0,0,0))
drawn = ImageDraw.Draw(img)
drawn.text((10, 10), x, fill=(255, 255, 255))
img.save('Self-Print-Image.jpg')
