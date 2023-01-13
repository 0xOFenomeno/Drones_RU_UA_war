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


drones_ua = []
drones_ru =[]
for drones_data in formatted_drones:
    if "Ukraine" in drones_data['Operator']:
        drones_ua.append(drones_data)
    elif "Russia" in drones_data['Operator']:
        drones_ru.append(drones_data)

'''print("-------- UKRAINIAN DRONES --------")
print(drones_ua)
print("\n")
print("-------- RUSSIAN DRONES --------")
print(drones_ru)
print('\n')'''




#generate cluster json for UAVs used by Russia in russo-ukrainian war
cluster_russia_uuid = str(uuid.uuid4())
cluster_russia = {"authors":"Enes AYATA", "category" : "military equipment", "description": "UAVs/UCAVs used by Russia in russo-ukranian war", "source": "Popular Mechanics","type":"uav-russia", "uuid":"bbf4c013-a44d-430c-8223-a98a6a51db90"}

values_russia =[]    
for item in drones_ru:
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
    values_russia.append(tmp_dict)

dict_values_russia = {"values":values_russia}
cluster_russia.update(dict_values_russia)
version_dict = {"version": 1}
cluster_russia.update(version_dict)



with open("../clusters/uav-russia.json", "w") as outfile:
    json.dump(cluster_russia, outfile,indent = 4)

#generate cluster json for UAVs used by Ukraine in russo-ukrainian war
cluster_ukraine_uuid = str(uuid.uuid4())
cluster_ukraine = {"authors":"Enes AYATA", "category" : "military equipment", "description": "UAVs/UCAVs used by Russia in russo-ukranian war", "source": "Popular Mechanics","type":"uav-ukraine", "uuid":"0e6899bf-5670-4876-9940-5eb94fc89870"}

values_ukraine =[]    
for item in drones_ua:
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
    values_ukraine.append(tmp_dict)

dict_values_ukraine = {"values":values_ukraine}
cluster_ukraine.update(dict_values_ukraine)
version_dict = {"version": 1}
cluster_ukraine.update(version_dict)


with open("../clusters/uav-ukraine.json", "w") as outfile:
    json.dump(cluster_ukraine, outfile,indent = 4)
