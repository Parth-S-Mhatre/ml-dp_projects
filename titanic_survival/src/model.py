import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import xgboost

X = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\parth\\Machine learning and deep learning project\\titanic_surival\\data\\X_data.csv')
y = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\parth\\Machine learning and deep learning project\\titanic_surival\\data\\y_data.csv').values.ravel()

# X.head()
# print(f"X shape:{X.shape}")
# print(f"y shape:{y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# # model
# model=LogisticRegression(max_iter=1000)
# model.fit(X_train,y_train)

# # Model Performance 
# y_pred = model.predict(X_test)

# print("Accuracy of the Logistic Regression model:", accuracy_score(y_test, y_pred))
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("Classification Report:\n\n", classification_report(y_test, y_pred))
# # Random forest model
# from sklearn.ensemble import RandomForestClassifier

# model_rn = RandomForestClassifier(n_estimators=100, random_state=101)
# model_rn.fit(X_train, y_train)
# # Model Performance 
# y_pred = model_rn.predict(X_test)

# print("Accuracy of the Random Forest Model:", accuracy_score(y_test, y_pred))
# print("Confusion Matrix:\n\n", confusion_matrix(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))

#
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

model_xg = XGBClassifier(random_state=101)
model_xg.fit(X_train, y_train)

# Model Performance 
y_pred = model_xg.predict(X_test)

print("Accuracy of the Xgboost:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


import joblib  

# Train the model
xgb_model = XGBClassifier(random_state=101)
xgb_model.fit(X_train, y_train)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler

# Feature scaling (important for neural networks)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Neural Network Architecture
nn_model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

# Compile the model
nn_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = nn_model.fit(X_train_scaled, y_train, validation_data=(X_test_scaled, y_test), epochs=100, batch_size=32, verbose=1)

# Evaluate performance
loss, accuracy = nn_model.evaluate(X_test_scaled, y_test)
print(f"\n✅ Neural Network Accuracy: {accuracy:.4f}")


# Save the model
joblib.dump(xgb_model, 'xgb_titanic_model.pkl')
print("✅ Model saved!")