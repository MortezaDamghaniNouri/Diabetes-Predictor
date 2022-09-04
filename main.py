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













