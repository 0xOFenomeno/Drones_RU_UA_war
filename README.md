# Drones_RU_UA_war

***Author***: Enes AYATA

***Teachers***: Mr. Alexandre DULAUNOY [@adulau](https://github.com/adulau) & Mr. Christian STUDER [@chris3rd](https://github.com/chrisr3d)

## Context
This repository is related to a university project which is about Threat Intelligence, and Malware Information Sharing Platform (MISP).

The geopolitical conflict between Russia :ru: and Ukraine :ukraine: which started in 2014 had a turning point with the Russian invasion of Ukraine on February 24th, 2022.
This war between two ex-members of U.S.S.R. has many technological actors like  weapons, ground vehicles, explosives, electronic warfare and communication equipments, ships, air defence weapons, aircrafts but also Unmmaned Aerial Systems with **Unmanned Aerial Vehicles (UAV)**  and  **Unmanned Combat Aerial Vehicles (UCAV)**.


## Purpose

~~**The purpose of this project is to integrate two galaxies in MISP, with their respective clusters**:~~
- ~~A galaxy for UAVs/UCAVs used by Ukraine in russo-ukrainian war~~
- ~~A galaxy for UAVs/UCAVs used by Russian in russo-ukrainian war~~

**The purpose of this project is to integrate a galaxy of UAVs ysed in russo-ukranian war, which will be updatable by adding new UAVs.**
- A galaxy named **uavs.json** has been created as well as its related cluster.

## Methodology

The methodology that I'm using for this project is the following:
- Scrap data of this interesting and complete [article](https://www.popularmechanics.com/military/a40298287/drone-fighting-ukraine-war-russia/) (Source: Popular Mechanics) using Python and BeautifulSoup.
- Structure scraped data into JSON format and integrated it locally into MISP galaxies and clusters (with Python)
- Check generated JSON files with **jq**
- ~~Try to integrate the two galaxies into MISP with a pull request~~
- Try to integrate this galaxy to **[misp-galaxy](https://github.com/MISP/misp-galaxy)** project

:heavy_check_mark: This galaxy has been successfully merged in **[misp-galaxy](https://github.com/MISP/misp-galaxy)** project!
