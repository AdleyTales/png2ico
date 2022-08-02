import imp


import os
from PIL import Image

files = os.listdir()
size  = (256,256)

if not os.path.exists('icon'):
  os.mkdir('icon')

for inName in files:
  tmp = os.path.splitext(inName)

  if tmp[1] == '.png':
    outName = tmp[0] + '.ico'
    im = Image.open(inName).resize(size)
    try:
      path = os.path.join('icon', outName)
      im.save(path)
    except IOError:
      print('connot convert : ', inName)
