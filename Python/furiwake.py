# 必用なモジュールをインポート
import csv
import glob
import os
import zipfile
import shutil

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

# 抽出する行と列の情報を定義
column_indices = [30, 55, 81, 107, 133, 159, 185, 211]

# 条件に基づいて変数に値を入れる関数
def assign_value(value):
    if value == "311000":
        return "Right"
    elif value == "312000":
        return "Left"
    elif value == "313000":
        return "Right and Left"
    else:
        return "Unknown"

# inputフォルダ内のファイルを処理
for filename in os.listdir(input):
    if filename.endswith(".csv"):
        csv_file_path = os.path.join(input, filename)
        
        # CSVファイルを開いて指定した行の値を抽出
        with open(csv_file_path, 'r', newline='', encoding="SJIS") as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Read the header row (optional if you want to skip it)

            for row_num, row in enumerate(csv_reader, start=1):
                if row_num in column_indices:
                    for col_idx in column_indices:
                        if len(row) > col_idx - 1:
                            value = row[col_idx - 1].strip('"')
                            result = assign_value(value)
                            print(f"{filename} の{row_num}行目の{col_idx}列の値: {value} -> {result}")
                        else:
                            print(f"{filename} の{row_num}行目の{col_idx}列にデータがありません")