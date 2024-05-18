import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import joblib


filename = 'classifier.sav'
classifier = joblib.load(filename)
dt_realtime = pd.read_csv('features-file-Mitm.csv',header=None).iloc[:, :]
result = classifier.predict(dt_realtime)

with open('result.txt', 'w') as f:
    f.write(str(result[0][0])+'  ')
    f.write(str(result[0][1]))