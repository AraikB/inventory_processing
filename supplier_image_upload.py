#!/usr/bin/env python3
import os
import requests
url = "http://localhost/upload"
directory = "supplier-data/images/"
dontrepeat = []
def upload_images():
  for filename in os.listdir(directory):
    if filename.endswith(".jpeg") and not str(filename) in dontrepeat :
      with open(directory+"/"+filename, "rb") as opened:
        r = requests.post(url, files={'file':opened})
        return r
