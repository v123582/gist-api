# -*- coding: utf-8 -*- 
import json

# TODO: 輸入任何一個位置，回傳最近的站點
def nearlyStations(sourceLongitude, sourceLatitude):  #經緯
    f_read_MRT = open("./datasrc/MRT.json","r")
    f_read_Bus = open("./datasrc/busStation.json","r") #讀檔有改
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
        distance_temp =  (Longitude_difference*Longitude_difference)+(Latitude_difference*Latitude_difference)
        if distance_temp < min_MRT_distance:
            min_MRT_station = i_item[u"站名-出口"]
            min_MRT_distance = distance_temp
    for i_item in Bus_List:
        Longitude_difference = float(i_item[u"座標"][u"緯度"])-sourceLongitude  #經緯相反
        Latitude_difference = float(i_item[u"座標"][u"經度"])-sourceLatitude
        distance_temp =  (Longitude_difference*Longitude_difference)+(Latitude_difference*Latitude_difference)
        if distance_temp < min_Bus_distance:
            min_Bus_station = i_item[u"公車站名"]
            min_Bus_distance = distance_temp

    return min_MRT_station, min_Bus_station


#TODO: 輸入兩個bus節點，回傳坐公車怎麼到
def Bus2Bus(Source_BUS_Station, Target_BUS_Station):
    f_read_Bus = open("./datasrc/busStation.json","r") #讀檔有改
    Bus_Text = json.loads(f_read_Bus.read())
    f_read_Bus.close()
    Bus_List = Bus_Text[u"公車站"]
    Return_list = [] #回傳公車路線

    #if Source_BUS_Station == Target_BUS_Station:  #起站公車和終站公車相同站牌    
    if Source_BUS_Station != Target_BUS_Station: #起站公車和終站公車不同站牌
        Source_Bus_Path_Set = []  #起站公車有的公車路線
        Target_Bus_Path_Set  = [] #終站公車有的公車路線

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
            


# TODO: 輸入公車站和捷運站，回傳可以從此公車站到此捷運站的公車路線
def Bus2MRT(busStation, MRTStation):
    with open('./datasrc/busStation.json') as data_file:
        bus_stations = json.load(data_file)
    
    busNo = []
    for bus_station in bus_stations[u'公車站']:
        #print bus_station[u'公車站名'], busStation
        if bus_station[u'公車站名'] == busStation:
            for bus_path in bus_station[u'路線']:
                for mrt_station in [mrt_station for mrt_station in bus_path[u'可到達捷運站']]:
                    #print mrt_station.split('捷運')[1].split('站')[0], MRTStation
                    if mrt_station.split(u'捷運')[1].split(u'站')[0] in MRTStation:
                        busNo.append(bus_path[u'路線'])
            break
    return busNo



#包六個點的geoson
def GeoJson6Point(sourceLongitude, sourceLatitude,targetLongitude, targetLatitude):  
    # Step1: 找出離來源最近的站
    Source_MRT_Station, Source_BUS_Station =  nearlyStations(sourceLongitude, sourceLatitude)
    # Step2: 找出離目標最近的站
    Target_MRT_Station, Target_BUS_Station = nearlyStations(targetLongitude, targetLatitude)
    f_read_MRT = open("./datasrc/MRT.json","r")
    f_read_Bus = open("./datasrc/busStation.json","r") #讀檔有改
    MRT_Text = json.loads(f_read_MRT.read())
    MRT_List = MRT_Text[u"捷運站"]
    Bus_Text = json.loads(f_read_Bus.read())
    Bus_List = Bus_Text[u"公車站"]
    f_read_MRT.close()
    f_read_Bus.close()
    Source_MRT_Location = []
    Source_BUS_Location = []
    Target_MRT_Location = []
    Target_BUS_Location = []
    for item in MRT_List:
        if item[u"站名-出口"] == Source_MRT_Station:
                Source_MRT_Location = [item[u"座標"][u"經度"],item[u"座標"][u"緯度"]]
        if item[u"站名-出口"] == Target_MRT_Station:
                Target_MRT_Location = [item[u"座標"][u"經度"],item[u"座標"][u"緯度"]]
    for item in Bus_List:
        if item[u"公車站名"] == Source_BUS_Station:
                Source_BUS_Location = [float(item[u"座標"][u"緯度"]),float(item[u"座標"][u"經度"])]
        if item[u"公車站名"] == Target_BUS_Station:
                Target_BUS_Location = [float(item[u"座標"][u"緯度"]),float(item[u"座標"][u"經度"])]
    #得到六個點轉成geo json

    Point_Set_Location = [[sourceLongitude, sourceLatitude],[targetLongitude, targetLatitude], Source_MRT_Location, Source_BUS_Location, Target_MRT_Location, Target_BUS_Location] #順序是:來源地 目標地 來源捷運 來源公車 目標捷運 目標公車
    #print Point_Set_Location

    Point_Set_Location_GeoJson = {}
    Point_Set_Location_GeoJson[u"type"] = "FeatureCollection"
    feature_List = []
    for each_point_index in range(len(Point_Set_Location)):
        feature_dic = {}
        
        geometry_dic ={}
        geometry_dic[u"type"] = "Point"
        geometry_dic[u"coordinates"] = Point_Set_Location[each_point_index]
        feature_dic[u"type"] = "Feature"
        feature_dic[u"geometry"] = geometry_dic
        properties = {}
        if each_point_index == 0 :
            properties[u"icon"] = "http://i.imgur.com/kId2AWX.png?1"
        elif each_point_index == 1 :
            properties[u"icon"] = "http://i.imgur.com/ixnS17A.png?1"
        elif each_point_index == 2 or each_point_index == 4:
            properties[u"icon"] = "http://i.imgur.com/5gyooz5.png?1"
        else:
            properties[u"icon"] = "http://i.imgur.com/Kr4HlrI.png?1"

        feature_dic["properties"] = properties
        feature_List.append(feature_dic)
    Point_Set_Location_GeoJson[u"features"] = feature_List
    #print json.dumps(Point_Set_Location_GeoJson,indent = 1)

    return Point_Set_Location_GeoJson

    

# TODO: 整體工作
def api(sourceLongitude, sourceLatitude, targetLongitude, targetLatitude):
    # Step1: 找出離來源最近的站
    Source_MRT_Station, Source_BUS_Station =  nearlyStations(sourceLongitude, sourceLatitude)
    # Step2: 找出離目標最近的站
    Target_MRT_Station, Target_BUS_Station = nearlyStations(targetLongitude, targetLatitude)
    # Step3: 檢查這兩個站有沒有一條線可以連起來
    # Step3-1: 找出離來源最近的公車站可到達的捷運站
    # Step3-2: 找出離目標最近的公車站可到達的捷運站
    # Step4: 完成

    Rule_1 = []
    for path in Bus2Bus(Source_BUS_Station, Target_BUS_Station):
        Rule_1.append([Source_BUS_Station, path, Target_BUS_Station])
    
    Rule_2 = []
    if Source_MRT_Station != Target_MRT_Station:
        Rule_2 = [Source_MRT_Station,Target_MRT_Station]

    Rule_3 = []
    for path_1 in Bus2MRT(Source_BUS_Station, Source_MRT_Station):
        for path_2 in Bus2MRT(Target_BUS_Station, Target_MRT_Station):
            Rule_3.append([Source_BUS_Station, path_1, Source_MRT_Station, Target_MRT_Station, path_2, Target_BUS_Station])

    Rule_4 = []
    for path in Bus2MRT(Source_BUS_Station, Source_MRT_Station):
        Rule_4.append([Source_BUS_Station, path, Source_MRT_Station, Target_MRT_Station])

    Rule_5 = []
    for path in Bus2MRT(Target_BUS_Station, Target_MRT_Station):
        Rule_5.append([Source_MRT_Station, Target_MRT_Station, path, Target_BUS_Station])

    API={}
    api_rule_dic = {}
    API["SOURCE_BUS"] = Source_BUS_Station
    API["SOURCE_MRT"] = Source_MRT_Station
    API["TARGET_BUS"] = Target_BUS_Station
    API["TARGET_MRT"] = Target_MRT_Station
    api_rule_dic["type1"] = Rule_1
    api_rule_dic["type2"] = Rule_2
    api_rule_dic["type3"] = Rule_3
    api_rule_dic["type4"] = Rule_4
    api_rule_dic["type5"] = Rule_5
    API["Rule"] = api_rule_dic
    API["GeoJson6Point"] = GeoJson6Point(sourceLongitude, sourceLatitude, targetLongitude, targetLatitude)
    return json.dumps(API,indent=1).decode("unicode_escape").encode("utf-8")


##
##print api (120.3021,22.6332,120.3521,22.6732) #測試六合夜市到六合夜市

def get_result(longitude, latitude):
    result = {
        'bus_no': '藍7', 
        'expected_time': 12, 
        'expected_cost': 45, 
        'attractions': ['維元家', '新崛江']
    }

    # with open('./datasrc/Bus.json') as data_file:
    #     bus_info = json.load(data_file)
    # with open('./datasrc/MRT.json') as data_file:
    #     mrt_info = json.load(data_file)
    
    return json.dumps(result, sort_keys= True, encoding = 'utf8', ensure_ascii= False)
