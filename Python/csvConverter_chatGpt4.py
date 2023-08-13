import csv
import os

# 処理に必用な値を定義
download = "download"
work = "./work"
input = "./input"
output = "./output"
col_1 = 29
col_2 = 55
col_3 = 81
col_4 = 107
col_5 = 133
col_6 = 159
col_7 = 185
col_8 = 211

def read_csv_file(file_path, column_indices):
    data = []
    with open(file_path, 'r', newline='', encoding="SJIS") as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Read the header row (optional if you want to skip it)
        for row in csv_reader:
            selected_columns = [row[index-1] for index in column_indices]
            data.append(selected_columns)
    return data

def process_csv_files(input_path, column_indices):
    csv_data = []
    for filename in os.listdir(input_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_path, filename)
            csv_data.extend(read_csv_file(file_path, column_indices))
    return csv_data

input_path = input
selected_columns = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8]
csv_data = process_csv_files(input_path, selected_columns)

right_code = "311000"
left_code = "312000"
bilateral_code = "313000"

original = []

for filename in os.listdir(input_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_path, filename)
        with open(file_path, "r", encoding="SJIS", newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)  # Read the header row (optional if you want to skip it)
            for row in csv_reader:
                original.append(row)

# print(original)

index = 0
right = []
left = []

for row in csv_data:
    print(row)
    index2 = 0
    R = None
    L = None
    while index2 < len(row):
        print(row[index2])                                
        if row[index2] == right_code and R is None:
            R = original[index][selected_columns[index2]-1:selected_columns[index2+1]-1]
        elif row[index2] == left_code and L is None:
            L = original[index][selected_columns[index2]-1:selected_columns[index2+1]-1]
        elif row[index2] == bilateral_code and R is None:
            R = original[index][selected_columns[index2]-1:selected_columns[index2+1]-1]
        elif row[index2] == bilateral_code and L is None:
            L = original[index][selected_columns[index2]-1:selected_columns[index2+1]-1]
        else:
            break
        index2 += 1
    right.append(R)
    left.append(L)   
    index += 1
           
print(right)
print(left)

null_values_to_insert = 25
null_row = [''] * null_values_to_insert

for i in range(len(right)):
    if right[i] is None:
        right[i] = null_row

for i in range(len(left)):
    if left[i] is None:
        left[i] = null_row

print(right)
print(left)


