from preprocessing import Preprocessing
from model import Model

featuresFile = "CSVs\\features.csv"
patientNotesFile = "CSVs\\patient_notes.csv"
trainFile = "CSVs\\train.csv"

prep = Preprocessing()
prep.organizeData(featuresFile, patientNotesFile, trainFile)

print(prep.fDF['feature_text'][0])
print(prep.pnDF['pn_history'][0])