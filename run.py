#!/usr/bin/env python3
import os
import requests
import re
import json

desc_directory = "supplier-data/descriptions/"
dontrepeat = []
dict = {}
output = []
def make_a_dict():
  """"Loads the contents of the filename as a Json file"""

  for filename in os.listdir(desc_directory):
    with open(desc_directory+"/"+filename) as text:
      name, weight, description = [data.strip() for data in text]
      dict={"name":name, "weight":weight[:-4], "description":description}
      f_param = r'(\w+).txt'
      image_name = re.search(f_param, str(filename))
      dict["image_name"]=str(image_name[1])+".jpeg"
      response = requests.post("https://localhost/fruits", dict)
      #print(response.request.body)
      dontrepeat.append(str(filename))
      output.append(dict)
      out_file = open("test1.json", "w")
      json.dump(output, out_file, indent = 4, sort_keys = False)


make_a_dict()
