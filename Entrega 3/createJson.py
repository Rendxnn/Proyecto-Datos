def createJson(path):
    timestamp = 1554772579000
    with open('example.json', 'w') as file:
        file.write('[\n{\n"waypoints": [\n')
        for x in range(len(path)):
            if x != len(path) - 1:
                file.write('{\n"coordinates": [\n' + path[x][1: len(path[x]) - 1] + '\n],\n"timestamp": ' + str(timestamp) + '},\n')
            else:
                file.write('{\n"coordinates": [\n' + path[x][1: len(path[x]) - 1] + '\n],\n"timestamp": ' + str(timestamp) + '}\n')
        file.write(']\n}\n]')
