import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv("Dataset/cleaned_dataset.csv")
labels = pd.read_csv("Dataset/cleaned_dataset_labels.csv")
X_train, X_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.2, random_state=0)

















