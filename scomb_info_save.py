"""
designer : 坂下直樹
date : 編集日(2020.06.30)
purpose : 入力フォームにて入力されたものをscomb.iniに保存する
"""

import configparser 

#iniファイルへの書き込む情報
def save(ID,PASSWORD):
 config = configparser.ConfigParser()
 section1 = 'Scomb'
 config.add_section(section1)
 config.set(section1, 'ID', ID)    
 config.set(section1, 'PASSWORD', PASSWORD)

#iniファイルへの書き込み
 with open('scomb.ini','w') as file:
     config.write(file)