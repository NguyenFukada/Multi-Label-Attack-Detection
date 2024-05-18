import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
import joblib

# Import the dataset
df = pd.read_csv('f3.csv')

# Shuffle dataset
# ds = df.sample(frac=1)
# ds.to_csv('dataset.csv')

# Splitting dataset into features and label
# df = df.drop('INDEX', axis=1)
X = df.drop(columns=['ARP Spoofing', 'IP Spoofing'])  # Bỏ ba cột nhãn để có ma trận đặc trưng X
y = df[['ARP Spoofing', 'IP Spoofing']]  # Chọn ba cột nhãn để có ma trận nhãn y
print(df.head(20))
y = y.reshape(1, -1)
# Splitting the dataset into the training set and the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature scaling (or standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


# Fitting SVM with the training set
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

# Testing the model by classifying the test set
y_pred = classifier.predict(X_test)

# # Creating confusion matrix for evaluation
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)

# # Print out confusion matrix and report
# print(y_pred)
print(cm)
print(cr)

# Response time = 7s

# Export model
filename = 'classifier.sav'
joblib.dump(classifier, filename)
print("Model exported!")
