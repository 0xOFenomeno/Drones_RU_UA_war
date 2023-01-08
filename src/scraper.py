#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


URL = "https://www.popularmechanics.com/military/a40298287/drone-fighting-ukraine-war-russia/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# find names of UAVs
titles = soup.find_all("strong")
drones = []
for item in titles:
    if item.text:
        drones.append(item.get_text())


# find technical description of UAVs
descriptions = soup.find_all('p', class_ = 'body-tip css-bm3c8v et3p2gv0')
drones_descriptions= []
for item in descriptions:
    if item.text:
        drones_descriptions.append(item.get_text())

# structure UAVs data into dictionnaries
i=0
formatted_drones = []
while i < len(drones_descriptions):
    description = drones_descriptions[i].split('|')
    j=0
    drone_dict = dict()
    while j < len(description):
        couple = description[j].split(":")
        tmp_dict= {couple[0]: couple[1]}
        drone_dict.update(tmp_dict)
        j+=1
    formatted_drones.append(drone_dict)
    i+=1

print(formatted_drones)