# -*- coding: utf-8 -*- 
import json

# TODO: 輸入任何一個位置，回傳最近的站點
def nearlyStations(sourceLongitude, sourceLatitude):
    return stations

# TODO: 輸入來源及目標公車站，回傳包含此二車站的公車路線列表
def Bus2Bus(srcBusStation, targetBusStation):
    return [busNo]

# TODO: 輸入公車站和捷運站，回傳可以從此公車站到此捷運站的公車路線
def Bus2MRT(busStation, MRTStation):
    with open('./datasrc/busStation.json') as data_file:
        bus_stations = json.load(data_file)
    
    busNo = []
    for bus_station in bus_stations[u'公車站']:
        print bus_station[u'公車站名'], busStation
        if bus_station[u'公車站名'].encode('utf8') == busStation:
            for bus_path in bus_station[u'路線']:
                for mrt_station in [mrt_station.encode('utf8') for mrt_station in bus_path[u'可到達捷運站']]:
                    print mrt_station.split('捷運')[1].split('站')[0], MRTStation
                    if mrt_station.split('捷運')[1].split('站')[0] in MRTStation:
                        busNo.append(bus_path[u'路線'].encode('utf8'))
            break
    return busNo

# TODO: 整體工作
def api(sourceLongitude, sourceLatitude, targetLongitude, targetLatitude):
    # Step1: 找出離來源最近的站
    sourceNearlyStations = nearlyStations(sourceLongitude, sourceLatitude)
    # Step2: 找出離目標最近的站
    targetNearlyStations = nearlyStations(targetLongitude, targetLatitude)
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
