#!/usr/bin/env python3

import os

import json

import requests

feed_dir = "~/data/feedback"
path = os.path.expanduser(feed_dir)
file_list = os.listdir(path)
url = "http://httpbin.org/post"
# Iterate over the files in the feedback directory
for filename in file_list:
  filename = path + "/" + filename
  if filename.endswith('.txt'):
    with open(filename, "r") as file:
      # Extract the title, name, date, and feedback
      lines = file.readline()
      title = lines.strip()
      name = lines.strip()
      date = lines.strip()
      feedback = file.read().strip()
      feedback_data = {"title": title, "name": name, "date": date,"feedback": feedback}
    
      response = requests.post(url, data=feedback_data)
    if response.status_code == 200:
      print('Data sent accepted')
    else:
      print('Data sent rejected')
