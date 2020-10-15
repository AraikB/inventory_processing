#!/usr/bin/env python3
import os
import requests
import re
desc_directory = "supplier-data/descriptions/"

files = os.listdir(desc_directory)
def make_a_son():
  """"Loads the contents of the filename as a Json file"""
  dontrepeat = []
  dict={}
  for filename in files:
    if not str(filename) in dontrepeat:
      with open(desc_directory+"/"+filename) as text:
        name, weight, description = [data.strip() for data in text]
        dict["name"]=name
        dict["weight"]=int(weight[:-4])
        dict["description"]=description
        f_param = r'(\w+).txt'
        image_name = re.search(f_param, str(filename))
        dict["image_name"]=str(image_name[1])+".jpeg"
        print(dict)
        #response = requests.post("https://localhost/fruits")
        #print(response.request.body)
        dontrepeat.append(str(filename))
make_a_son()
