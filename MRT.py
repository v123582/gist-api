# -*- coding: utf8 -*-
import json
File_Read = open("VP0270.kml","r")
line = File_Read.readline()
stop_name = ""
Json_MRT = {} 
Json_MRT_ItemSet = []
while True:
    if line == "": break
    if "landmarkna" in line:
        stop_name = line.split(">")[1].split("<")[0]
    if "<coordinates>" in line:
        coordinates = line.split("<Point><coordinates>")[1].split("<")[0]
        Latitude = coordinates.split(",")[1]  #緯度
        Longitude = coordinates.split(",")[0] #經度
        Json_MRT_Set = {}
        Json_MRT_Location = {}
        Json_MRT_Set[u"站名-出口"] = stop_name
        Json_MRT_Location[u"緯度"] = float(Latitude)
        Json_MRT_Location[u"經度"] = float(Longitude)
        Json_MRT_Set[u"座標"] = Json_MRT_Location
        Json_MRT_ItemSet.append(Json_MRT_Set)
    line = File_Read.readline()

Json_MRT[u"捷運站"] = Json_MRT_ItemSet
temp =  json.dumps(Json_MRT,indent=1).decode("unicode_escape").encode("utf-8")

File_Write = open("MRT.json","w")
File_Write.write(temp)
File_Write.close()
File_Read.close()



