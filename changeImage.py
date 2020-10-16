#!/usr/bin/env python3

import os
import re
from PIL import Image

def convert_resize_image():
    '''RESIZES AND ROTATES 90 clockwise and saves in opt icons naming system as a jpeg format
    Ideas for improvement
    1. Improve naming system from serialized to a rename using Regex to replace filename with filename_size_revised
    2. Expand formats to include all image types
    3. Ensure the repeater is optimized
    4. Add in multi-processor use and load balance among them
    '''
    directory = "supplier-data/images/"
    dontrepeat = []
    for filename in os.listdir(directory):
        if filename.endswith(".tiff") and not str(filename) in dontrepeat :
            im = Image.open(directory+"/"+filename)
            f_param = r'(\w+).tiff'
            thefile = re.search(f_param, filename)
            new_im = im.convert('RGB').resize((600,400)).save("supplier-data/images/"+str(thefile.group(1))+".jpeg", "JPEG")
            dontrepeat.append(str(filename))

convert_resize_image()
