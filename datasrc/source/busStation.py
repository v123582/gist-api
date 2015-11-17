import json
f = open('2014BusStation.txt','r')
for i in range(0,11):
    f.readline()
line = f.readline()
busStation = {}
while 1:
    if line == '':break
    char = line.strip().split(' ')
    busS = char[3].split('="')
    checkMat = busS[1][0:-1].split('捷運')
    if(len(checkMat)>1):
        temp = char[2].split('="')
        bus = temp[1][0:-1]
        bus_s = busS[1].strip('"')
        if(bus in busStation):
            value = busStation.get(bus)
            busStation[bus] = value + [bus_s]
        else:
            busStation[bus] = [bus_s]
    line = f.readline()

print json.dumps(busStation, encoding="UTF-8", ensure_ascii=False, sort_keys=True,indent=4, separators=(',', ': '))

#####Remove duplicate
for i in busStation:
    temp = busStation.get(i)
    temp2 = list(set(temp))
    busStation[i] = temp2
print json.dumps(busStation, encoding="UTF-8", ensure_ascii=False, sort_keys=True,indent=4, separators=(',', ': '))
####

f = open('2014BusStation.txt','r')
for i in range(0,11):
    f.readline()
line = f.readline()
result = {}
while 1:
    if line == '':break
    char = line.strip().split(' ')
    bus = char[2].strip('routeId="').strip('"')
    if(bus in busStation):
        busName = char[3].strip('nameZh="').strip('"')
        if(busName in result):
            temp = result[busName].get("路線")
            Mrt = busStation.get(bus)
            c = 0
            for i in result[busName]["路線"]:
                if(i["路線"] == bus):
                    c += 1
            if(c == 0):
                temp2 = {"路線":bus,"可到達捷運站":Mrt}
                result[busName]["路線"] = temp + [temp2]
        else:
            if('latitude' in char[9]):
                latitude = char[9].strip('latitude="').strip('"')
                longitude = char[10].strip('longitude="').strip('"')
            else:
                latitude = char[10].strip('latitude="').strip('"')
                longitude = char[11].strip('longitude="').strip('"')
            Mrt = busStation.get(bus)
            result[busName] = {"公車站名":busName,"座標":{"經度":latitude,"緯度":longitude},"路線":[{"路線":bus,"可到達捷運站":Mrt}]} 
    
    line = f.readline()  
print json.dumps(result, encoding="UTF-8", ensure_ascii=False, sort_keys=True,indent=4, separators=(',', ': '))
##
output = []
for item in result:
    output+= [result.get(item)]
final = {"公車站":output}
print json.dumps(final, encoding="UTF-8", ensure_ascii=False, sort_keys=True,indent=4, separators=(',', ': '))

with open('busStation.txt', 'w') as outfile:
    json.dump(final, outfile, sort_keys = True, indent = 4, ensure_ascii=False)