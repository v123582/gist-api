# -*- coding: utf-8 -*- 
import json

# TODO: 輸入任何一個位置，回傳最近的站點
def nearlyStations(sourceLongitude, sourceLatitude):  #經緯
    f_read_MRT = open("datasrc/MRT.json","r")
    f_read_Bus = open("busStation.json","r") 
    MRT_Text = json.loads(f_read_MRT.read())
    MRT_List = MRT_Text[u"捷運站"]
    Bus_Text = json.loads(f_read_Bus.read())
    Bus_List = Bus_Text[u"公車站"]
    min_MRT_distance = 1000000000
    min_MRT_station = ""
    min_Bus_distance = 1000000000
    min_Bus_station = ""

    f_read_MRT.close()
    f_read_Bus.close()
    
    for i_item in MRT_List:
        Longitude_difference = i_item[u"座標"][u"經度"]-sourceLongitude
        Latitude_difference = i_item[u"座標"][u"緯度"]-sourceLatitude
        distance_temp =  (Longitude_difference * Longitude_difference)+(Latitude_difference*Latitude_difference)
        if distance_temp < min_MRT_distance:
            min_MRT_station = i_item[u"站名-出口"]
            min_MRT_distance = distance_temp
    for i_item in Bus_List:
        Longitude_difference = float(i_item[u"座標"][u"緯度"])-sourceLongitude  #經緯相反
        Latitude_difference = float(i_item[u"座標"][u"經度"])-sourceLatitude
        distance_temp =  (Longitude_difference * Longitude_difference)+(Latitude_difference*Latitude_difference)
        if distance_temp < min_Bus_distance:
            min_Bus_station = i_item[u"公車站名"]
            min_Bus_distance = distance_temp

    return min_MRT_station, min_Bus_station


#TODO: 輸入兩個bus節點，回傳坐公車怎麼到
def BusToBus(Source_BUS_Station, Target_BUS_Station):
    f_read_Bus = open("busStation.json","r")
    Bus_Text = json.loads(f_read_Bus.read())
    f_read_Bus.close()
    Bus_List = Bus_Text[u"公車站"]
    Return_list = [] #回傳公車路線

    #if Source_BUS_Station == Target_BUS_Station:  #起站公車和終站公車相同站牌
     
    if Source_BUS_Station != Target_BUS_Station: #起站公車和終站公車不同站牌
        Source_Bus_Path_Set = []  #起站公車有的公車路線
        Source_Bus_MRT = ""       #起站公車有的公車路線
        Target_Bus_Path_Set  = [] #終站公車有的公車路線
        Target_Bus_MRT = ""       #終站公車有的公車路線

        for i_item in Bus_List:
            if i_item[u"公車站名"] == Source_BUS_Station:
                for j_item in i_item[u"路線"]:
                    Source_Bus_Path_Set.append(j_item[u"路線"])
        for i_item in Bus_List:
            if i_item[u"公車站名"] == Target_BUS_Station:
                for j_item in i_item[u"路線"]:
                    Target_Bus_Path_Set.append(j_item[u"路線"])

        
        for each_source_path in Source_Bus_Path_Set:   #起站和終站有共同公車路線就回傳公車路線
            if each_source_path in Target_Bus_Path_Set:
                Return_list.append(each_source_path)

        return Return_list
            


# TODO: 輸入一個公車站，回傳這個公車可以投過哪些公車到達哪些捷運站
def Bus2MRT(busStation,MRTStation):
    return [{busNo}] 

# TODO: 整體工作
def api(sourceLongitude, sourceLatitude, targetLongitude, targetLatitude):
    # Step1: 找出離來源最近的站
    # Step2: 找出離目標最近的站
    # Step3: 檢查這兩個站有沒有一條線可以連起來
    # Step3-1: 找出離來源最近的公車站可到達的捷運站
    # Step3-2: 找出離目標最近的公車站可到達的捷運站
    # Step4: 完成
    Source_MRT_Station, Source_BUS_Station =  nearlyStation(sourceLongitude, sourceLatitude)
    Targe_MRT_Station, Target_MRT_Station = nearlyStation(targetLongitude, targetLatitude)
    API_Json = {}
    API_Json["最近捷運站"], API_Json["最近公車站"] = Source_MRT_Station, Source_MRT_Station
    Path = {}
    
    return ""



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
