import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv("Dataset/cleaned_dataset.csv")
labels = pd.read_csv("Dataset/cleaned_dataset_labels.csv")
X_train, X_test, Y_train, Y_test = train_test_split(dataset, labels, test_size=0.2, random_state=0)
classifier = xgb.XGBClassifier(learning_rate=0.05, max_depth=4, n_estimators=300, colsample_bytree=1, random_state=123, eval_metric="auc", verbosity=1)
eval_set = [(X_test, Y_test)]   # This is validation data, these data are used only for validation, and they can be used again for testing.
classifier.fit(X_train, Y_train, early_stopping_rounds=10, eval_set=eval_set)
Y_pred = classifier.predict(X_test)
Y_test = Y_test.values.tolist()

# Calculating the precision of the model
i = 0
correct_counter = 0
true_positive_counter = 0
false_positive_counter = 0
false_negative_counter = 0
true_negative_counter = 0
while i < len(Y_pred):
    if Y_pred[i] == Y_test[i][0]:
        correct_counter += 1
    if Y_pred[i] == Y_test[i][0] and Y_test[i][0] == 1:
        true_positive_counter += 1
    if Y_pred[i] == 1 and Y_test[i][0] == 0:
        false_positive_counter += 1
    if Y_pred[i] == 0 and Y_test[i][0] == 1:
        false_negative_counter += 1
    if Y_pred[i] == Y_test[i][0] and Y_pred[i] == 0:
        true_negative_counter += 1
    i += 1
print("Precision: " + str(round((correct_counter / len(Y_pred)) * 100, 2)) + " %")
print("Recall: " + str(round((true_positive_counter / (true_positive_counter + false_negative_counter)), 2)))
print("CONFUSION MATRIX:")
print("True positive = " + str(true_positive_counter) + "    " + "precision = " + str(round((true_positive_counter / len(Y_pred)) * 100, 2)) + " %")
print("True negative = " + str(true_negative_counter) + "    " + "precision = " + str(round((true_negative_counter / len(Y_pred)) * 100, 2)) + " %")
print("False positive = " + str(false_positive_counter) + "    " + "precision = " + str(round((false_positive_counter / len(Y_pred)) * 100, 2)) + " %")
print("False negative = " + str(false_negative_counter) + "    " + "precision = " + str(round((false_negative_counter / len(Y_pred)) * 100, 2)) + " %")









