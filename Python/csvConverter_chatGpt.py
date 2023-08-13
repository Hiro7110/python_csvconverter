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

# Print the data


right = []
left = []
right_code = "311000"
left_code = "312000"
bilateral_code = "313000"

for row in csv_data:
    print(row)
    original=[]
    for filename in os.listdir(input_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_path, filename)
            with open(file_path, "r", encoding="SJIS") as csvfile:
                csv_reader = csv.reader(csvfile)
                header = next(csv_reader)  # Read the header row (optional if you want to skip it)
                for original in csv_reader:
                    index = 0
                    for i in row:
                        # print(i)                                
                        if i == "null":
                            break
                        elif i == bilateral_code:
                            right.append(original[selected_columns[index]-1:selected_columns[index+1]-1])
                            left.append(original[selected_columns[index]-1:selected_columns[index+1]-1])
                            break
                        elif i == right_code:
                            right.append(original[selected_columns[index]-1:selected_columns[index+1]-1])
                            break
                        elif i == left_code:
                            left.append(original[selected_columns[index]-1:selected_columns[index+1]-1])
                            break
                        index += 1
                        
for row in csv_data:
    for i in row:
        print(i)                
                    
# print(right)
# print(left)



    
    
# 左右に振り分ける



