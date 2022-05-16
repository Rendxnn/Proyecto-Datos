import pandas as pd
import replaceAverage as av
import createGraphs as cg
import dijkstra as ds
import createJson as cs
import plotMap as pm

file = pd.read_csv('calles_de_medellin_con_acoso.csv', delimiter=';')
file.fillna(0, inplace=True)


def main():
    print('Reemplazando...')
    print('1. Consultar camino más corto')
    print('2. Consultar camino más seguro')
    print('3. Consultar camino más corto y seguro')
    n = int(input('Ingrese la opción que desea consultar: '))
    if n == 1:
        graph = cg.createGraphDistance(file)
        start = input('Ingrese coordenada inicial: ')
        goal = input('Ingrese coordenada final: ')
        respuestas = ds.dijkstra(graph, start, goal)
        camino = respuestas[0]
        peso = respuestas[1]
        print(f'La distancia es: {peso}')
        cs.createJson(camino)
        pm.plotMap()
        cs.resetJson()
    elif n == 2:
        graph = cg.createGraphHarassment(file, av.average)
        start = input('Ingrese coordenada inicial: ')
        goal = input('Ingrese coordenada final: ')
        respuestas = ds.dijkstra(graph, start, goal)
        camino = respuestas[0]
        peso = respuestas[1]
        print(f'El acoso promedio del recorrido es: {peso / len(camino)}')
        cs.createJson(camino)
        pm.plotMap()
        cs.resetJson()
    elif n == 3:
        graph = cg.createGraphBoth(file, av.average)
        start = input('Ingrese coordenada inicial: ')
        goal = input('Ingrese coordenada final: ')
        respuestas = ds.dijkstra(graph, start, goal)
        camino = respuestas[0]
        cs.createJson(camino)
        pm.plotMap()
        cs.resetJson()
        #valores = cg.findHarassmentDistance(file, camino)
        #print(f'La distancia es: {valores[0]}')
        #print(f'El acoso promedio es: {valores[1] / (len(camino))}')
    else:
        print('Ingrese un número válido')


main()
