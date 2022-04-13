from ast import literal_eval
import pandas as pd
import re

class Preprocessing:
    def __init__(self):

        return


    def organizeData(self, featuresFile, patientNotesFile, trainFile):
        self.fDF = pd.read_csv(featuresFile)
        self.pnDF = pd.read_csv(patientNotesFile)
        self.tDF = pd.read_csv(trainFile)

        self.tDF['annotation'] = self.tDF['annotation'].apply(literal_eval)
        self.tDF['location'] = self.tDF['location'].apply(literal_eval)

        self.removeORs(self.fDF['feature_text'])
        self.removeSpecialChars(self.pnDF['pn_history'])

    def removeORs(dataFrameEntry):
        for x in dataFrameEntry:
            x.replace("-OR-", ";-").replace("-", " ")

    def removeSpecialChars(dataFrameEntry):
        dataFrameEntry.apply(lambda x: x.lower())
        for x in dataFrameEntry:
            x = x.replace("(", " ")
            x = x.replace(")", " ")
            x = x.replace(":", " ")
            x = x.replace(";", " ")
            x = x.replace("-", " ")
            x = x.replace("/", " ")
            x = x.replace("\n", " ")
            x = x.replace("\'", "")
            x = x.replace("\"", "")
            x = x.replace(",", " ")
            x = x.replace(".", " ")
            x = re.sub(r'\bzero\b', '0', x)
            x = re.sub(r'\bone\b', '1', x)
            x = re.sub(r'\btwo\b', '2', x)
            x = re.sub(r'\bthree\b', '3', x)
            x = re.sub(r'\bfour\b', '4', x)
            x = re.sub(r'\bfive\b', '5', x)
            x = re.sub(r'\bsix\b', '6', x)
            x = re.sub(r'\bseven\b', '7', x)
            x = re.sub(r'\beight\b', '8', x)
            x = re.sub(r'\bnine\b', '9', x)

