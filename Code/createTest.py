import pandas as pd

featuresFile = "CSVs\\features.csv"
patientNotesFile = "CSVs\\patient_notes.csv"
trainFile = "CSVs\\train.csv"
testFile = "CSVs\\exhaustiveTest.csv"

featuresList = []
patientNotesList = []
testList = []

file = open(featuresFile, 'r')
for line in file:
    lineSplit = line.split(',')
    featuresList.append([lineSplit[0]])

featuresList.pop(0)
#print(featuresList)
file.close()

file = open(patientNotesFile, 'r')
for line in file:
    if not line[0].isdigit():
        continue
    lineSplit = line.split(',')
    if len(lineSplit) < 2 or len(lineSplit[0]) != 5:
        continue
    patientNotesList.append([lineSplit[0], lineSplit[1]])

file.close()

testList = []
for pn in patientNotesList:
    for feature in featuresList:
        id = pn[0] + "_" + feature[0]
        caseNum = pn[1]
        pnNum = pn[0]
        featureNum = feature[0]
        testList.append(id + ',' + caseNum + ',' + pnNum + ',' + featureNum)

file = open(testFile, 'w')
for testItem in testList:
    file.write(testItem + '\n')