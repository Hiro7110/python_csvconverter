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

mammoCsv = "マンモ動作確認用オーダー.csv"

with open (mammoCsv,"r", encoding="SJIS") as f:
     rows = csv.reader(f)
     for row in rows:
          for i in row:
            print(i)

        

