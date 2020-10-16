#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import run
import datetime
import json
import os
dict = {}
table_data = []
empty_line = Spacer(1,20)
styles = getSampleStyleSheet()
desc_directory = "supplier-data/descriptions/"
def make_a_dict():
  for filename in os.listdir(desc_directory):
    with open(desc_directory+"/"+filename) as text:
      name, weight, description = [data.strip() for data in text]
      dict={"name":name, "weight":weight, "description":description}
      table_data.append(["Name: "+dict['name']])
      table_data.append(["Weight: "+dict['weight']])
      table_data.append("")
make_a_dict()



report = SimpleDocTemplate("/tmp/report.pdf")
report_table = Table(data=table_data, hAlign="LEFT")
print(report_table)
report_title = Paragraph("Processed Update on {}".format(datetime.date.today()), styles["h1"])

report.build([report_title, report_table, empty_line])
