import pandas as pd

# This function sorts the input numerical list by bubble sort
def sorter(input_list):
    k = len(input_list)
    while k != 1:
        m = 0
        while m < (k-1):
            if input_list[m] > input_list[m + 1]:
                template = input_list[m + 1]
                input_list[m + 1] = input_list[m]
                input_list[m] = template
            m += 1
        k = k - 1


# This function removes repetitious values in the input list
def repetition_remover(input_list):
    template = []
    for k in input_list:
        if k not in template:
            template.append(k)
    return template


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
null_indexes = []
i = 0
while i < len(cleaned_dataset_list):
    if cleaned_dataset_list[i][22] == "Unknown":
        null_indexes.append(i)
    i += 1
new_cleaned_dataset = []
i = 0
while i < len(cleaned_dataset_list):
    if i not in null_indexes:
        new_cleaned_dataset.append(cleaned_dataset_list[i])
    i += 1
cleaned_dataset_list = new_cleaned_dataset


# Removing white spaces in different tuples
i = 0
while i < len(cleaned_dataset_list):
    j = 0
    while j < len(cleaned_dataset_list[0]):
        if str(cleaned_dataset_list[i][j]).find(" ") != -1:
            cleaned_dataset_list[i][j] = cleaned_dataset_list[i][j].replace(" ", "_")
        j += 1
    i += 1

BMIs = []
i = 0
while i < len(cleaned_dataset_list):
    BMIs.append(cleaned_dataset_list[i][20])
    i += 1
BMIs = repetition_remover(BMIs)
sorter(BMIs)
print(BMIs)
























