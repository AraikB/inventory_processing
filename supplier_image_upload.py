#!/usr/bin/env python3

import requests
import os


# This example shows how a file can be uploaded using
# The Python Requests module
url = "http://localhost/upload/"
#image_DIR = os.path.expanduser('~') + '/supplier-data/images/'
image_DIR = "supplier-data/images/"
list_image = os.listdir(image_DIR)
jpeg_images = [image_name for image_name in list_image if '.jpeg' in image_name]

for image in jpeg_images:
  with open(IMAGE_DIR + image, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
