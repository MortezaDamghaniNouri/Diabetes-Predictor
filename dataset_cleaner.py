import pandas as pd
import csv

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



# Scaling BMIs
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][5]
    if 9 >= temp >= 0:
        cleaned_dataset_list[i][5] = 1
    if 19 >= temp >= 10:
        cleaned_dataset_list[i][5] = 2
    if 29 >= temp >= 20:
        cleaned_dataset_list[i][5] = 3
    if 39 >= temp >= 30:
        cleaned_dataset_list[i][5] = 4
    if 49 >= temp >= 40:
        cleaned_dataset_list[i][5] = 5
    if 59 >= temp >= 50:
        cleaned_dataset_list[i][5] = 6
    if 69 >= temp >= 60:
        cleaned_dataset_list[i][5] = 7
    if 79 >= temp >= 70:
        cleaned_dataset_list[i][5] = 8
    if 89 >= temp >= 80:
        cleaned_dataset_list[i][5] = 9
    if 100 >= temp >= 90:
        cleaned_dataset_list[i][5] = 10
    i += 1

# Scaling General Health
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][15]
    if temp == "Very_Low":
        cleaned_dataset_list[i][15] = 10000
    if temp == "Low":
        cleaned_dataset_list[i][15] = 1000
    if temp == "Medium":
        cleaned_dataset_list[i][15] = 100
    if temp == "Good":
        cleaned_dataset_list[i][15] = 10
    if temp == "High":
        cleaned_dataset_list[i][15] = 1
    i += 1

# Scaling Mental Health
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][16]
    if 9 >= temp >= 0:
        cleaned_dataset_list[i][16] = 1
    if 19 >= temp >= 10:
        cleaned_dataset_list[i][16] = 2
    if 30 >= temp >= 20:
        cleaned_dataset_list[i][16] = 3
    i += 1

# Scaling Physical Health
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][17]
    if 9 >= temp >= 0:
        cleaned_dataset_list[i][17] = 1
    if 19 >= temp >= 10:
        cleaned_dataset_list[i][17] = 2
    if 30 >= temp >= 20:
        cleaned_dataset_list[i][17] = 3
    i += 1

# Scaling Age
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][20]
    if 6 >= temp >= 1:
        cleaned_dataset_list[i][20] = 0
    else:
        cleaned_dataset_list[i][20] = 1
    i += 1

# Scaling Education
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][21]
    if temp == "Cat1":
        cleaned_dataset_list[i][21] = 100000
    if temp == "Cat2":
        cleaned_dataset_list[i][21] = 10000
    if temp == "Cat3":
        cleaned_dataset_list[i][21] = 1000
    if temp == "Cat4":
        cleaned_dataset_list[i][21] = 100
    if temp == "Cat5":
        cleaned_dataset_list[i][21] = 10
    if temp == "Cat6":
        cleaned_dataset_list[i][21] = 1
    i += 1

# Scaling Income
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][22]
    if temp == "Cat1":
        cleaned_dataset_list[i][22] = 10000000
    if temp == "Cat2":
        cleaned_dataset_list[i][22] = 1000000
    if temp == "Cat3":
        cleaned_dataset_list[i][22] = 100000
    if temp == "Cat4":
        cleaned_dataset_list[i][22] = 10000
    if temp == "Cat5":
        cleaned_dataset_list[i][22] = 1000
    if temp == "Cat6":
        cleaned_dataset_list[i][22] = 100
    if temp == "Cat7":
        cleaned_dataset_list[i][22] = 10
    if temp == "Cat8":
        cleaned_dataset_list[i][22] = 1
    i += 1

# Applying One hot encoding on Sex attribute
i = 0
while i < len(cleaned_dataset_list):
    temp = cleaned_dataset_list[i][19]
    if temp == "male":
        cleaned_dataset_list[i][19] = 10
    else:
        cleaned_dataset_list[i][19] = 1
    i += 1

# Removing extra attributes
diabetes_labels = []
i = 0
while i < len(cleaned_dataset_list):
    diabetes_labels.append(cleaned_dataset_list[i][1])
    cleaned_dataset_list[i].pop(0)
    cleaned_dataset_list[i].pop(0)
    i += 1

# Converting cleaned dataset to a csv file
csv_file = open("Dataset/cleaned_dataset.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerows(cleaned_dataset_list)
csv_file.close()
new_diabetes_label = []
i = 0
while i < len(diabetes_labels):
    temp = [diabetes_labels[i]]
    new_diabetes_label.append(temp)
    i += 1
csv_file = open("Dataset/cleaned_dataset_labels.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerows(new_diabetes_label)
csv_file.close()
print("The length of cleaned dataset and labels: " + str(len(cleaned_dataset_list)))















