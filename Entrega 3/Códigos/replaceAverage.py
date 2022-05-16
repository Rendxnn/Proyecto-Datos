def replaceAverage(file):
    aux = 0
    average = 0
    for index, row in file.iterrows():
        if (row['harassmentRisk']) != 1.0 and row['harassmentRisk'] != 0:
            average += float(row['harassmentRisk'])
            aux += 1
    average /= aux
    return average


average = 0.8513629071805722