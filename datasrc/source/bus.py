import json
f = open('test.txt','r')
line =  f.readline()
d = {}
while 1:
    if line == '' : break
    char = line.strip().split('\t')
    bus_line = char[2].strip().split(',')
    #     STOPID STOPNAME BLINES POINT_X POINT_Y
    for line in bus_line:
        if(line in d):
            temp = d.get(line)
            d[line] = temp + [{'座標':{'經度':char[3],'緯度':char[4]},'站名':char[1]}]
        else:
            d[line] = [{'座標':{'經度':char[3],'緯度':char[4]},'站名':char[1]}]
    line = f.readline()
total = []
for bus_line in d:
    total += [{'站點':d.get(bus_line),'路線':bus_line}]
final = {'公車路線':total}
with open('bus_line.txt', 'w') as outfile:
    json.dump(final, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
print json.dumps(final, encoding="UTF-8", ensure_ascii=False, sort_keys=True,indent=4, separators=(',', ': '))