# -*- coding: utf-8 -*- 
import json
import geojson

with open('./mrt_path_original.json') as data_file:
    mrt_path_original = json.load(data_file, encoding = 'utf8')

mrt_path_processed = []
for path in mrt_path_original['features']:
    between_stations = {
        'source': path['geometry']['coordinates'][0],
        'target': path['geometry']['coordinates'][-1],
        'path': path
    }
    mrt_path_processed += [between_stations]

mrt_path = {
    '捷運線': mrt_path_processed
}

output = geojson.dumps(mrt_path, sort_keys= False, indent= 2).decode("unicode_escape").encode("utf-8")
fw = open("MRTPath.geojson","w")
fw.write(output)
fw.close()
