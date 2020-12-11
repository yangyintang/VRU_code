import sys

def get_vrus(ru, ruType, route, routeCount):
    vrus = []
    i = 0
    while i < len(ru):
        num = ru[i][1:len(ru[i]) - 1].split(",")[int( (route - 2) % routeCount)]
        temp = \
        '{\"type\" : \"' + ruType[i] + '\", \"number\" : ' + num + '}' + ',\n' \
        + '\t\t\t\t\t\t\t\t  '
        vrus.append(temp)
        i += 1
    return vrus

def add_vrus(string, vrus):
    string = string[0:len(string) - 2] + '],\n'
    string += '\t\t\t\t\"vrus\" : ['
    i = 0
    while i < len(vrus):
        string += vrus[i]
        i += 1
    string = string[0:len(string) - 12] + '],\n'
    return string

def convert(csvFile, currInputIndex):
    arr = []
    headers = []

    routeCount = int(sys.argv[currInputIndex])
    segment = int(sum(1 for line in csvFile) / routeCount)
    currInputIndex += 1

    ruType = ['BIKE', 'PEDESTRIAN', 'CAR', 'TRUCK', 'SKATER']
    ru = []
    
    while len(sys.argv) > currInputIndex:
        ru.append(sys.argv[currInputIndex])
        currInputIndex += 1

    csvFile.close()
    csvFile = open(sys.argv[1], 'r')

    for header in csvFile.readline().split(','):
        headers.append(header)

    headers[len(headers) - 1] = \
    headers[len(headers) - 1][0:len(headers[len(headers) - 1]) - 1]

    curr = 0
    prevRoute = 1
    string = '\t\t\t\t\"routename\" : \"Route ' + str(1) + '\",\n'
    flag = True

    for line in csvFile.readlines():
        route = int(curr / segment) + 1
        gps = []
        vrus = []
        if route != prevRoute and route <= routeCount:
            vrus = get_vrus(ru, ruType, route, routeCount)
            string = add_vrus(string, vrus)
            arr.append(string)
            string = '\t\t\t\t\"routename\" : \"Route ' + str(route) + '\",\n'
            prevRoute += 1
            flag = True

        for i, item in enumerate(line.split(',')):
            if headers[i] == "lat":
                lat = '{\"' + headers[i] + '\" : ' + item + ', '
                gps.append(lat)
            elif headers[i] == "long":
                long = '\"' + headers[i] + '\" : ' + item + '}'
                gps.append(long)

            if len(gps) == 2:
                if flag:
                    string += '\t\t\t\t"gps" : [' + gps[0] + gps[1] + ',\n'
                else:
                    string += '\t\t\t\t\t\t\t\t ' + gps[0] + gps[1] + ',\n'
                gps = []
                flag = False
        curr += 1

    vrus = get_vrus(ru, ruType, route, routeCount)
    string = add_vrus(string, vrus)
    arr.append(string)
    return arr

def get_output(arr, jsonName):
    output= \
    '{\n\t\"vru-simulation-data\":{\n' + '\t\t\"name\": \"' + jsonName + '\",\n' + '\t\t\"simdata\": [\n'

    for i in range(len(arr)):
            if i == len(arr) - 1:
                output += "\t\t\t{\n" + str(arr[i])[:-2] + "\n\t\t\t}\n"
            else:
                output += "\t\t\t{\n" + str(arr[i])[:-2] + "\n\t\t\t},\n"

    output += '\t\t]\n\t}\n\n}'
    return output

def main():
    if len(sys.argv) >= 2:
        currInputIndex = 2
        jsonName = "sim.json"

        if sys.argv[2].find(".json") == -1:
            csvFile = open(sys.argv[1], 'r')
            jsonFile = open(jsonName, 'w')
        else:
            jsonName = sys.argv[2]
            csvFile = open(sys.argv[1], 'r')
            jsonFile = open(jsonName, 'w')
            currInputIndex += 1
    else:
        print("Invalid arguements")
        sys.exit()

    arr = convert(csvFile, currInputIndex)
    csvFile.close()
    output = get_output(arr, jsonName)

    jsonFile.write(output)
    jsonFile.close()
    print(jsonName + " has been successfully generated.")

main()
