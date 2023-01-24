#!/usr/bin/env python3

import uuid
import requests
from bs4 import BeautifulSoup
import json


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
        title = {"name":drones[i]}
        drone_dict.update(title)
        drone_uuid = {"uuid":str(uuid.uuid4())}
        drone_dict.update(drone_uuid)
        tmp_dict= {couple[0].strip(): couple[1].strip()}
        drone_dict.update(tmp_dict)
        j+=1
    formatted_drones.append(drone_dict)
    i+=1

# generate clusters/uavs.json from dictionary formatted HTML data
cluster = {"authors":["Enes AYATA"], "category" : "military equipment", "description": "Unmanned Aerial Vehicles / Unmanned Combat Aerial Vehicles", "name":"UAVs/UCAVs" ,"source": "Popular Mechanics","type":"uavs", "uuid":"bef5c29d-b0db-4923-aa9a-80921f26d3ab"}

values = []
for item in formatted_drones:
    tmp_dict ={"description":item.get("name")}
    meta = {}
    for key,value in item.items():
        if key != "name" and key != "uuid":
            key_value_dict = {key:value}
            meta.update(key_value_dict)

    tmp_meta = {"meta":meta}
    tmp_dict.update(tmp_meta)

    tmp_uuid= {"uuid":item.get("uuid")}
    tmp_dict.update(tmp_uuid)

    tmp_value_dict = {"value":item.get("name")}
    tmp_dict.update(tmp_value_dict)
    values.append(tmp_dict)

dict_values = {"values":values}
cluster.update(dict_values)
version_dict = {"version": 1}
cluster.update(version_dict)


with open("../clusters/uavs.json", "w") as outfile:
    json.dump(cluster, outfile,indent = 4)