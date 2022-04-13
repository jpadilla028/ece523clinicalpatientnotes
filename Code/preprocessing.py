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

        self.removeORs()
        self.removeSpecialChars()

    def removeORs(self):
        for i in range(len(self.fDF['feature_text'])):
            self.fDF['feature_text'][i] = self.fDF['feature_text'][i].replace("-OR-", ";-").replace("-", " ")

    def removeSpecialChars(self):
        self.pnDF['pn_history'].apply(lambda x: x.lower())
        for i in range(len(self.pnDF['pn_history'])):
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace("(", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace(")", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace(":", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace(";", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace("-", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace("/", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace("\n", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace("\'", "")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace("\"", "")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace(",", " ")
            self.pnDF['pn_history'][i] = self.pnDF['pn_history'][i].replace(".", " ")
            self.pnDF['pn_history'][i] = re.sub(r'\bzero\b', '0', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bone\b', '1', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\btwo\b', '2', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bthree\b', '3', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bfour\b', '4', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bfive\b', '5', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bsix\b', '6', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bseven\b', '7', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\beight\b', '8', self.pnDF['pn_history'][i])
            self.pnDF['pn_history'][i] = re.sub(r'\bnine\b', '9', self.pnDF['pn_history'][i])

