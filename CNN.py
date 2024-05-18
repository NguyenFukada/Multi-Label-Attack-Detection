# !pip install multilabel-eval-metrics
from tensorflow import keras
import tensorflow as tf
import joblib
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

train = pd.read_csv('f3.csv').iloc[:, :]    # reading the csv file
train.head()      # printing first five rows of the file
X = train.drop(columns=['ARP Spoofing', 'IP Spoofing'])  # Bỏ ba cột nhãn để có ma trận đặc trưng X
y = train[['ARP Spoofing', 'IP Spoofing']]  # Chọn ba cột nhãn để có ma trận nhãn y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# Initialize StandardScaler
scaler = StandardScaler()

# Fit scaler on training data and transform both training and test data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
n_inputs, n_outputs = X_train_scaled.shape[1], y_train.shape[1]
X_train_scaled= X_train_scaled.reshape((X_train.shape[0],X_train.shape[1],1))
# X_train_scaled = np.array([np.array(val) for val in X_train_scaled])
# X_train_scaled  = tf.convert_to_tensor(X_train_scaled, dtype=tf.float32)

def get_model(n_inputs, n_outputs):
        model = Sequential()
        model.add(Conv1D(filters=64,kernel_size= (3),activation='relu',input_shape=(n_inputs,1),padding='same'))
        model.add(MaxPooling1D(pool_size=2))
        Dropout(0.5),  # Thêm dropout để tránh overfitting
        model.add(Conv1D(filters=128,kernel_size=(3),activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2))
        Dropout(0.5)
        model.add(Conv1D(filters=256,kernel_size= (3),activation='relu',padding='same'))
        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(n_outputs, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['BinaryAccuracy'])
        return model

model = get_model(n_inputs, n_outputs)
model.fit(X_train_scaled, y_train, epochs=100, batch_size=64, verbose=1)
# Evaluate the model on the scaled test set
y_pred = model.predict(X_test_scaled)
y_pred_rounded = np.round(y_pred)
y_pred_rounded = y_pred_rounded.astype(np.int32)
# Export model
filename = 'classifier.sav'
joblib.dump(model, filename)

print("Model exported!")
