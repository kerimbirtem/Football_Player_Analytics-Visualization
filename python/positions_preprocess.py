# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:53:28 2023

@author: kerim
"""



    

# positions sutunu icin calısmalar


# positions sütunundaki verileri al
positions = fm22d['Position'].str.split(', ')

# verileri ayrı ayrı alarak bir liste oluştur
position_list = [pos for sublist in positions for pos in sublist]

# benzersiz pozisyonları içeren bir dizi oluştur
unique_positions = pd.Series(position_list).unique()

# unique_positions'ı DataFrame olarak tanımlamak isterseniz
df_unique_positions = pd.DataFrame({'Position_uni': unique_positions})

# sonucu yazdır
print(df_unique_positions)


df_unique_positions['Position_uni'] = df_unique_positions['Position_uni'].str.strip()
print(df_unique_positions)

               
#####

import re
df_unique_positions['Position_uni_pr'] = df_unique_positions['Position_uni'].str.extract(r'\((.*?)\)')
# Sonucu yazdır
print(df_unique_positions)


# unique positionsları belriledim excel tarafında tüm pozisyonları kendime göre değiştir yaparak düzenledim.
df_unique_positions['Position_uni'] = df_unique_positions['Position_uni'].str.replace(r'\(.*?\)', '', regex=True)
# Sonucu yazdır
print(df_unique_positions)
unique_positions = pd.DataFrame(df_unique_positions['Position_uni'].unique(), columns=['Unique_Positions'])
# Sonucu yazdır
print(unique_positions)



###

# '/' ile ayrılan karakterleri ayrı ayrı alarak yeni bir DataFrame oluştur
separated_positions = unique_positions['Unique_Positions'].str.split('/', expand=True)
separated_positions = separated_positions.apply(lambda x: x.str.strip())  # Boşlukları kaldır

# Tüm ayrı pozisyonları unique şekilde al
all_positions = separated_positions.stack().unique()

# Yeni DataFrame oluştur
new_dataframe = pd.DataFrame(all_positions, columns=['Separated_Positions'])

# Sonucu yazdır
print(new_dataframe)    
secilen_sutunlar = ['Name', 'Position','Preferred Foot']
df_secilen = fm22d[secilen_sutunlar]
dosya_yolu = 'positions.xlsx'
df_secilen.to_excel(dosya_yolu, index=True)

# bu excel kullanarak tüm pozisyonları kendi mapime göre değiştirdim.




'''




''' Posizyonlar tablosu oluşturma   for sql

import pandas as pd

# Örnek Excel verilerini içeren DataFrame'i oluşturun
data = pd.read_excel('positions.xlsx')
data = data.iloc[:, 1:]
data.insert(0, "player_id", fm22d["UID"])
data = data.iloc[:, :-1]
# oyuncu id leri de ekledim.

df = pd.DataFrame(data)





data['Name'] = data['Name'].str.strip()
data['Position'] = data['Position'].str.strip()


df['Name'] = df['Name'].str.strip()
df['Position'] = df['Position'].str.strip()




df = pd.DataFrame(data)



# Pozisyonlar tablosunu oluştur
positions = df['Position'].str.split(', ')
positions_table = pd.DataFrame({
    'player_id': df['player_id'].repeat(positions.str.len()),
    'Name': df['Name'].repeat(positions.str.len()),
    'Position': [pos for sublist in positions for pos in sublist]
})


# Pozisyonlar tablosunu oluştur
positions_fullname = {
    'GK': 'Goalkeeper',
    'D': 'Defender',
    'DM': 'Defensive Midfielder',
    'B': 'Back',
    'WB': 'Wing Back',
    'WM': 'Wide Midfielder',
    'M': 'Midfielder',
    'AM': 'Attacking Midfielder',
    'ST': 'Striker'
}

# 'pst' sütununu oluştur
positions_table['pst'] = positions_table['Position'].apply(lambda x: x.split('(')[0].strip())
# Parantez içerisindeki ifadeleri silmek için
positions_table['pst'] = positions_table['pst'].str.replace(r'\(.*\)', '').str.strip()


# 'positions_fullname' sütununu oluştur
positions_table['positions_fullname'] = positions_table['pst'].map(positions_fullname)

# 'pst_directions' sütununu oluştur
positions_table['pst_directions'] = positions_table['Position'].apply(lambda x: x.split('(')[1].replace(')', '').strip() if '(' in x else 'std')

positions_table['Left'] = positions_table['pst_directions'].str.contains('L').astype(int)
positions_table['Center'] = positions_table['pst_directions'].str.contains('C').astype(int)
positions_table['Right'] = positions_table['pst_directions'].str.contains('R').astype(int)

# 'pst_directions' sütununu yeniden adlandır


# Tabloyu görüntüle
print(positions_table)



positions_table.to_excel('positions_table.xlsx', index=False)




#######


# Posizyonlar tablosu oluşturma   for ML
 
positions_table_encode = pd.read_excel('positions1.xlsx', sheet_name=1)

positions_table_encode = positions_table_encode.iloc[:, 1:-1]
positions_table_encode['Position'] = positions_table_encode['Position'].apply(lambda x: x.strip() if isinstance(x, str) else x)


# Sütunlar listesi
columns = ['GK', 'BL', 'DL', 'DC', 'DR', 'BR', 'DM', 'WBL', 'WBR', 'WML', 'WMR', 'ML', 'MC', 'MR', 'AML', 'AMC', 'AMR', 'ST']

# Sütunları dolaşarak değerleri ayarla

for col in columns:
    positions_table_encode[col] = positions_table_encode['Position'].apply(lambda x: int(col in x.split(', ')))

positions_table_encode.to_excel('positions_table_encoding.xlsx', index=False)







# positions table düzeltme positions_table_v2 olacak

import pandas as pd

# Örnek Excel verilerini içeren DataFrame'i oluşturun
data1 = pd.read_excel('positions1.xlsx',sheet_name=1)
data1 = data1.iloc[:, 1:-1]
data1.insert(0, "player_id", fm22d["UID"])
# oyuncu id leri de ekledim.


data1['Name'] = data1['Name'].str.strip()
data1['Position'] = data1['Position'].str.strip()



df1 = pd.DataFrame(data1)

# Pozisyonlar tablosunu oluştur
positions1 = df1['Position'].str.split(', ')
positions_table_v2 = pd.DataFrame({
    'player_id': df1['player_id'].repeat(positions1.str.len()),
    'Name': df1['Name'].repeat(positions1.str.len()),
    'Position': [pos for sublist in positions1 for pos in sublist]
})

# Pozisyonlar tablosunu oluştur
positions_fullname_1 = {
    'GK': 'Goalkeeper',
    'DC': 'Defender-Center',
    'DL': 'Defender-Left',
    'DR': 'Defender-Right',
    'DM': 'Defensive Midfielder',
    'BL': 'Back-Left',
    'BR': 'Back-Right',
    'WBL': 'Wing Back-Left',
    'WBR': 'Wing Back-Right',
    'WML': 'Wide Midfielder-Left',
    'WMR': 'Wide Midfielder-Right',
    'MC': 'Midfielder-Center',
    'ML': 'Midfielder-Left',
    'MR': 'Midfielder-Right',
    'AMC': 'Attacking Midfielder-Center',
    'AML': 'Attacking Midfielder-Left',
    'AMR': 'Attacking Midfielder-Right',
    'ST': 'Striker'
}


# 'positions_fullname' sütununu oluştur
positions_table_v2['positions_fullname'] = positions_table_v2['Position'].map(positions_fullname_1)

positions_table_v2 = positions_table_v2.reset_index(drop=True)

positions_table_v2.to_excel('positions_table_v2.xlsx', index=False)


#positions table_v2 duplicate düzenlemesi:
    
    


import pandas as pd

# Örnek Excel verilerini içeren DataFrame'i oluşturun
data1 = pd.read_excel('positions1.xlsx',sheet_name=1)
data1 = data1.iloc[:, 1:-1]
data1.insert(0, "player_id", fm22d["UID"])
# oyuncu id leri de ekledim.


data1 = data1.drop_duplicates(subset='player_id', keep='first')


data1['Name'] = data1['Name'].str.strip()
data1['Position'] = data1['Position'].str.strip()



df1 = pd.DataFrame(data1)

# Pozisyonlar tablosunu oluştur
positions1 = df1['Position'].str.split(', ')
positions_table_v2 = pd.DataFrame({
    'player_id': df1['player_id'].repeat(positions1.str.len()),
    'Name': df1['Name'].repeat(positions1.str.len()),
    'Position': [pos for sublist in positions1 for pos in sublist]
})

# Pozisyonlar tablosunu oluştur
positions_fullname_1 = {
    'GK': 'Goalkeeper',
    'DC': 'Defender-Center',
    'DL': 'Defender-Left',
    'DR': 'Defender-Right',
    'DM': 'Defensive Midfielder',
    'BL': 'Back-Left',
    'BR': 'Back-Right',
    'WBL': 'Wing Back-Left',
    'WBR': 'Wing Back-Right',
    'WML': 'Wide Midfielder-Left',
    'WMR': 'Wide Midfielder-Right',
    'MC': 'Midfielder-Center',
    'ML': 'Midfielder-Left',
    'MR': 'Midfielder-Right',
    'AMC': 'Attacking Midfielder-Center',
    'AML': 'Attacking Midfielder-Left',
    'AMR': 'Attacking Midfielder-Right',
    'ST': 'Striker'
}


# 'positions_fullname' sütununu oluştur
positions_table_v2['positions_fullname'] = positions_table_v2['Position'].map(positions_fullname_1)

positions_table_v2 = positions_table_v2.reset_index(drop=True)

positions_table_v2.to_excel('positions_table_v2_dup.xlsx', index=False)
