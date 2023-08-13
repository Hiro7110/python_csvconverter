# 必用なモジュールをインポート
import csv
import glob
import os
import zipfile
import shutil
import pandas as pd

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
selected_columns = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8]

right_code = "311000"
left_code = "312000"
bilateral_code = "313000"

# 1. downloadにあるzipを解凍してworkに移動
for filename in os.listdir(download):
     if filename.endswith(".zip"):
        zip_path = os.path.join(download, filename)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(work)
            print(f"{filename} を解凍しました")
        os.remove(zip_path)
        print(f"{filename} を削除しました")

# 2. work内にある*.csvをinputに移動
for root, _, files in os.walk(work, topdown=False):
    for filename in files:
        if filename.endswith(".csv"):
            work_path = os.path.join(root, filename)
            input_path = os.path.join(input, filename)
            shutil.move(work_path, input_path)
            print(f"{filename} を移動しました")
    for filename in files:
        if filename.endswith(".pdf"):
            work_path = os.path.join(root, filename)
            ouput_path = os.path.join(output, filename)
            shutil.move(work_path, ouput_path)
            print(f"{filename} を移動しました")

# 3. workフォルダを空にする
shutil.rmtree(work)
os.mkdir(work)

# 4.csvの特定のcolumnだけ取り出す
# 4-1. csvファイルを読み込むための処理
def process_csv_files(input, column_indices):
    csv_data = []
    if file.endswith('.csv'):
        file_path = os.path.join(input, file)
        csv_data.extend(read_csv_file(file_path, column_indices))
    return csv_data

# 4-2. csvの特定のcolumnを抽出するための関数を設定
def read_csv_file(file_path, column_indices):
    data = []
    with open(file_path, 'r', newline='', encoding="SJIS") as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Read the header row (optional if you want to skip it)
        for row in csv_reader:
            selected_columns = [row[index-1] for index in column_indices]
            data.append(selected_columns)
    return data

# 4-3. 4-1/2で設定した関数を基にcsv_dataに特定のカラム（左右コードが入ったカラムのみ）の値を抽出
# csv_data = process_csv_files(input, selected_columns)

# 5. csvの値を全て抽出
# 元のcsvの項目を入れるための配列
original = []
filtered=[]

def read_original():
    if file.endswith(".csv"):
        file_path = os.path.join(input, file)
        with open(file_path, "r", encoding="SJIS", newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)  # Read the header row (optional if you want to skip it)
            for row in csv_reader:
                original.append(row)

def filter_and_overwrite_csv():
    if file.endswith(".csv"):
        file_path = os.path.join(input, file)
        with open (file_path,"r", newline="", encoding="SJIS") as f:
            rows = csv.reader(f)
        # 1-28項目のデータを取り出してfilteredに格納
            for row in rows:
                filtered_row = row[:28]  # 1-28項目を取り出す
                filtered.append(filtered_row)
            # print(filtered)
        with open(file_path, "w", newline="", encoding="SJIS") as i:
            csv.writer(i).writerows(filtered)

# print(original)

# 6-1. 4と5で抽出した情報を基に左右の振り分け実施
index = 0
right = []
left = []

def right_or_left():
    global index # index変数をglobal変数として扱う
    for row in csv_data:
        # print(row)
        index2 = 0
        R = None
        L = None
        while index2 < len(row):
            # print(row[index2])                                
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
           
# print(right)
# print(left)

# 6-2.振り分けた値で左右がNoneの場合にnullの値を25個代入
null_values_to_insert = 25
null_row = [''] * null_values_to_insert

def right_None():
    for i in range(len(right)):
        if right[i] is None:
            right[i] = null_row
def left_None():
    for i in range(len(left)):
        if left[i] is None:
            left[i] = null_row

for file in os.listdir(input):
    csv_data = process_csv_files(input, selected_columns)
    read_original()
    # print(original)
    filter_and_overwrite_csv()
    # print(filtered)
    filtered = []
    right_or_left()
    right_None()
    left_None()
    print(right)
    print(left)
    



# バッチファイルを起動する
# batch_file_path = "path/to/your/batch/file.bat"



        

