# -*- coding: utf-8 -*- 
import json

# TODO: 輸入任何一個位置，回傳最近的站點
def nearlyStations(sourceLongitude, sourceLatitude):
    return stations

# TODO: 輸入一個公車站，回傳這個公車可以投過哪些公車到達哪些捷運站
def Bus2MRT(busStation):
    return [{MRTStations, busNo}] 

# TODO: 整體工作
def api(sourceLongitude, sourceLatitude, targetLongitude, targetLatitude):
    # Step1: 找出離來源最近的站
    # Step2: 找出離目標最近的站
    # Step3: 檢查這兩個站有沒有一條線可以連起來
    # Step3-1: 找出離來源最近的公車站可到達的捷運站
    # Step3-2: 找出離目標最近的公車站可到達的捷運站
    # Step4: 完成
    return ''

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
