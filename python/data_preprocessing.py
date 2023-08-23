# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:13:22 2023

@author: kerim
"""

FM datas preprocessing.



# libraries

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt




# data read

fm22d = pd.read_excel('fm22data.xlsx')

# Sütun isimlerindeki boşlukları kaldırmak
fm22d = fm22d.rename(columns=lambda x: x.strip())
# satırlar için 
fm22d = fm22d.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# tekrar eden oyuncular var
deduplicated_fm22d = fm22d.drop_duplicates(subset='UID', keep='first')
fm22d = fm22d.drop_duplicates(subset='UID', keep='first')

fm22_head = fm22d.head(10)
fm22_info = fm22d.info()
fm22_describe = fm22d.describe()

null_count = fm22d.isnull().sum()


print("fm 22 info ",fm22_info)
print("fm 22 describe" ,fm22_describe)
print("HEAD", fm22_head)
print("null count",null_count)      


print(fm22_head.columns)



    



# Data oluşturma

data = fm22d[['UID', 'Name']].copy()
data.columns = ['player_id', 'player_name']

# birdhday sütunu için 
# Parantezli ifadeyi silme işlemi
print(fm22d.columns)
fm22d['DoB'] = fm22d['DoB'].str.replace(r'\s*\([^)]*\)', '', regex=True)

data['birthdate'] = fm22d['DoB']

#'Nat', 'Based', 'Division', 'Club'

data['nation'] = fm22d['Nat']
data['based'] = fm22d['Based']
data['division'] = fm22d['Division']
data['club'] = fm22d['Club']

data['based'] = data['based'].str.replace(r'\s*\([^)]*\)', '', regex=True)


positions_table_encode = pd.read_excel('positions1.xlsx', sheet_name=1)
data = pd.concat([data, positions_table_encode.iloc[:, 1:]], axis=1)

data['Position'] = data['Position'].apply(lambda x: x.strip() if isinstance(x, str) else x)

data = data.drop(columns=['Name', data.columns[-1]])

data['preferred_foot'] = fm22d['Preferred Foot']
data['left_foot'] = fm22d['Left Foot']
data['right_foot'] = fm22d['Right Foot']

data['height'] = fm22d['Height']
data['weight'] = fm22d['Weight']

# ' cm' ve ' kg' ifadelerini kaldırma ve veri tipini integer yapma
data['height'] = data['height'].str.replace(' cm', '').astype(int)
data['weight'] = data['weight'].str.replace(' kg', '').astype(int)

# control

print('data info', data.info())
print('data describe', data.describe())

columns_to_convert = ['GK', 'BL', 'DL', 'DC', 'DR', 'BR', 'DM', 'WBL', 'WBR', 'WML', 'WMR', 'ML', 'MC', 'MR', 'AML', 'AMC', 'AMR', 'ST']
data[columns_to_convert] = data[columns_to_convert].astype(bool)

data.to_excel('data1.xlsx', index=False)

#data 1 adlı bir veriseti hazırlandı.

# player_name length
# data_length = data[['player_name']].copy()
# data_length['name_length'] = data_length['player_name'].str.len()


# boşluk temizleme 
import pandas as pd
df = pd.read_excel("nations_1.xlsx")
# Sütun isimlerinin sondaki boşlukları temizleyin
df.columns = df.columns.str.rstrip()
# Hücrelerin sondaki boşluklarını temizleyin
df = df.applymap(lambda x: x.rstrip() if isinstance(x, str) else x)
# Hücrelerdeki ve sütun adlarında başındaki boşlukları silmek için strip() yöntemini kullanın
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# Temizlenmiş veri setini başka bir dosyaya kaydedin (isteğe bağlı)
df.to_excel("nations_1.xlsx", index=False)
leauges_df.to_excel("leauges_1.xlsx")



#player_features tablosu 


ilk_2_sutun = fm22d.iloc[:, :2]

# 27. sütundan sonraki sütunlar
sonraki_sutunlar = fm22d.iloc[:, 26:]

# İki DataFrame'i birleştirelim
player_features = pd.concat([ilk_2_sutun, sonraki_sutunlar], axis=1)

player_features.to_excel("player_features.xlsx")


# player tablosu 

players = data.iloc[:, :4]

nations = pd.read_excel("nations.xlsx")
clubs = pd.read_excel("clubs_table.xlsx")
players['nation_id'] = players['nation'].map(nations.set_index('nation_short')['nation_id'])

# Suriname 2 kere yazılmış nation table da  193 no id HOLD a çekildi. Guyana 2 kere yazılmış nation table da 88 nolu id hold oldu.
# duplicated_values = nations.duplicated(subset='nation_short', keep=False)
# duplicated_nations = nations[duplicated_values]


players['club']=data['club']
players['division']= data['division']

players['club_id'] = players['club'].map(clubs.set_index('Club')['club_id'])

# 'club' sütunundaki boş değerleri 'Unknown' olarak değiştirelim
players['club'].replace('', 'Unknown', inplace=True)

# 'division' sütunundaki '-' değerlerini 'Unknown' olarak değiştirelim
players['division'].replace('-', 'Unknown', inplace=True)


duplicated_values = clubs.duplicated(subset='Club', keep=False)
duplicated_nations = clubs[duplicated_values]


#1
for index, row in players.iterrows():
    division_filter = clubs['Division'] == row['division']
    filtered_club = clubs[division_filter]['Club']
    club_filter = clubs['Club'] == row['club']
    club_id = clubs[club_filter]['club_id'].values[0]
    players.at[index, 'club_id'] = club_id


#2
# players tablosundaki her satır için işlem yapalım
for index, row in players.iterrows():
    division_filter = clubs['Division'] == row['division']
    filtered_club = clubs[division_filter]['Club']
    
    if not filtered_club.empty:
        club_filter = filtered_club == row['club']
        club_id = clubs[division_filter][club_filter]['club_id'].values[0]
    else:
        club_id = -1
        
    players.at[index, 'club_id'] = club_id


#3 Not 2 çalıştı 3 denenmedi

# players tablosundaki her satır için işlem yapalım
for index, row in players.iterrows():
    division = row['division']
    club = row['club']
    
    if division in grouped_clubs.groups:
        group = grouped_clubs.get_group(division)
        club_id = group.loc[group['Club'] == club, 'club_id'].values[0]
        players.at[index, 'club_id'] = club_id
    else:
        players.at[index, 'club_id'] = -1
        
        
data_from_9th_column = data.iloc[:, 8:]

# players DataFrame'ini data DataFrame'inin 9. sütunundan sonrasıyla birleştirelim
players = pd.concat([players, data_from_9th_column], axis=1)
        

players.to_excel("players.xlsx")

#club_id ler doğru mu oldu diğer yaklaşımlara bak.




# player_id ler duplicate ediyor mu ?

import pandas as pd 
players= pd.read_csv("Tables/csv/players.csv")



duplicate_rows = players[players.duplicated('player_id', keep=False)]

deduplicated_df = players.drop_duplicates(subset='player_id', keep='first')

deduplicated_df.to_excel("players_dup.xlsx")



duplicate_rows_fm22d = fm22d[fm22d.duplicated('UID', keep=False)]
deduplicated_fm22d = fm22d.drop_duplicates(subset='player_id', keep='first')


# player_feauters tablosu için 

player_features = pd.read_excel("player_features.xlsx")

player_features = player_features.drop_duplicates(subset='UID', keep='first')

player_features.to_excel("player_features_dup.xlsx")

