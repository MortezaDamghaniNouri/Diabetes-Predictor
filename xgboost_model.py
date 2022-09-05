import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv("Dataset/cleaned_dataset.csv")
labels = pd.read_csv("Dataset/cleaned_dataset_labels.csv")
X_train, X_test, Y_train, Y_test = train_test_split(dataset, labels, test_size=0.2, random_state=0)
classifier = xgb.XGBClassifier()
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)
Y_test = Y_test.values.tolist()

# Calculating the precision of the model
i = 0
correct_counter = 0
while i < len(Y_pred):
    if Y_pred[i] == Y_test[i][0]:
        correct_counter += 1
    i += 1
print("Precision: " + str((correct_counter / len(Y_pred)) * 100))














