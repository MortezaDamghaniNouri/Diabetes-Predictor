import pandas as pd
import numpy as np
dataset = pd.read_csv("Dataset/diabetes.csv")
dataset_list = dataset.values.tolist()
# Finding the indexes of Nan values
null_indexes = []
column_names = []
for name in dataset.columns:
    column_names.append(name)
column_names.pop(0)
for name in column_names:
    temp = dataset[dataset[name].isnull()].index.tolist()
    for i in temp:
        null_indexes.append(i)
i = 0
cleaned_dataset_list = []
while i < len(dataset_list):
    if i not in null_indexes:
        cleaned_dataset_list.append(dataset_list[i])
    i += 1

# Removing white spaces in different tuples
i = 0
while i < len(cleaned_dataset_list):
    j = 0
    while j < len(cleaned_dataset_list[0]):
        if str(cleaned_dataset_list[i][j]).find(" ") != -1:
            cleaned_dataset_list[i][j] = cleaned_dataset_list[i][j].replace(" ", "_")
        j += 1
    i += 1




























