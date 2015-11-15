# -*- coding: utf-8 -*- 
import json

def get_result(longitude, latitude):
    result = {
        'bus_no': '藍7', 
        'expected_time': 12, 
        'expected_cost': 45, 
        'attractions': ['維元家', '新崛江']
    }

    with open('./datasrc/Bus.json') as data_file:
        bus_info = json.load(data_file)
    with open('./datasrc/MRT.json') as data_file:
        mrt_info = json.load(data_file)
    
    return json.dumps(result, sort_keys= True, encoding = 'utf8', ensure_ascii= False)

print get_result(123.22, 23.8)