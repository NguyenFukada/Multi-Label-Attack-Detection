import xgboost as xgb
import pandas as pd
import joblib
from sklearn.datasets import make_multilabel_classification
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
df = pd.read_csv('f3.csv').iloc[:, :]
df.head()      # printing first five rows of the file
X = df.drop(columns=['ARP Spoofing', 'IP Spoofing'])  # Bỏ ba cột nhãn để có ma trận đặc trưng X
y = df[['ARP Spoofing', 'IP Spoofing']]  # Chọn ba cột nhãn để có ma trận nhãn y

# # split dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
# # create XGBoost instance with default hyper-parameters
xgb_estimator = xgb.XGBClassifier(objective='binary:logistic')

# # create MultiOutputClassifier instance with XGBoost model inside
multilabel_model = MultiOutputClassifier(xgb_estimator)

# # fit the model
multilabel_model.fit(X_train, y_train)

# # evaluate on test data

print('Accuracy on test data: {:.1f}%'.format(accuracy_score(y_test, multilabel_model.predict(X_test))*100))
# Export model
filename = 'classifier.sav'
joblib.dump(multilabel_model, filename)

print("Model exported!")