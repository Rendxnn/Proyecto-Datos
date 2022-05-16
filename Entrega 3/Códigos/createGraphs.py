import replaceAverage as av


def createGraphDistance(file):
    graph = {}
    for index, row in file.iterrows():
        if row['origin'] not in graph:
            graph[row['origin']] = {row['destination']: row['length']}
        else:
            graph[row['origin']][row['destination']] = row['length']
        if row['destination'] not in graph:
            graph[row['destination']] = {row['origin']: row['length']}
        else:
            graph[row['destination']][row['origin']] = row['length']
    return graph


def createGraphHarassment(file, average):
    graph = {}
    for index, row in file.iterrows():
        if row['origin'] not in graph:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['origin']] = {row['destination']: row['harassmentRisk']}
            else:
                graph[row['origin']] = {row['destination']: average}
        else:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['origin']][row['destination']] = row['harassmentRisk']
            else:
                graph[row['origin']][row['destination']] = average
        if row['destination'] not in graph:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['destination']] = {row['origin']: row['harassmentRisk']}
            else:
                graph[row['destination']] = {row['origin']: average}
        else:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['destination']][row['origin']] = row['harassmentRisk']
            else:
                graph[row['destination']][row['origin']] = average
    return graph


def createGraphBoth(file, average):
    graph = {}
    for index, row in file.iterrows():
        if row['origin'] not in graph:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['origin']] = {row['destination']: row['harassmentRisk'] * row['length']}
            else:
                graph[row['origin']] = {row['destination']: average * row['length']}
        else:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['origin']][row['destination']] = row['harassmentRisk'] * row['length']
            else:
                graph[row['origin']][row['destination']] = average * row['length']
        if row['destination'] not in graph:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['destination']] = {row['origin']: row['harassmentRisk'] * row['length']}
            else:
                graph[row['destination']] = {row['origin']: average * row['length']}
        else:
            if row['harassmentRisk'] != 0 and row['harassmentRisk'] != 1:
                graph[row['destination']][row['origin']] = row['harassmentRisk'] * row['length']
            else:
                graph[row['destination']][row['origin']] = average * row['length']
    return graph


def findHarassmentDistance(file, camino):
    distancia = 0
    acoso = 0
    for x in range(len(camino)):
        for index, row in file.iterrows():
            if x + 1 >= len(camino):
                break
            if camino[x] == row['origin'] and camino[x + 1] == row['destination']:
                distancia += row['length']
                if row['harassmentRisk'] == 0 or row['harassmentRisk'] == 1:
                    acoso += av.average
                else:
                    acoso += row['harassmentRisk']

            elif camino[x] == row['destination'] and camino[x + 1] == row['origin']:
                distancia += row['length']
                if row['harassmentRisk'] == 0 or row['harassmentRisk'] == 1:
                    acoso += av.average
                else:
                    acoso += row['harassmentRisk']
    return [distancia, acoso]
