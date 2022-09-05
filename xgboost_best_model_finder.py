import xgboost as xgb
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
dataset = pd.read_csv("Dataset/cleaned_dataset.csv")
labels = pd.read_csv("Dataset/cleaned_dataset_labels.csv")
X_train, X_test, Y_train, Y_test = train_test_split(dataset, labels, test_size=0.2, random_state=0)
classifier = xgb.XGBClassifier(subsample=0.5, random_state=123, eval_metric="auc", verbosity=1)
eval_set = [(X_test, Y_test)]   # This is validation data, these data are used only for validation, and they can be used again for testing.
parameters = {
    "learning_rate": [0.02, 0.05, 0.1, 0.3],
    "max_depth": [2, 3, 4],
    "n_estimators": [100, 200, 300],
    "colsample_bytree": [0.8, 1]
}
grid_search = GridSearchCV(estimator=classifier, param_grid=parameters, verbose=True)
grid_search.fit(X_train, Y_train, eval_set=eval_set)
print("The best parameters: " + str(grid_search.best_estimator_))




