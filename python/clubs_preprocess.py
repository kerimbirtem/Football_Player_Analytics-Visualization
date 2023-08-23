# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:10:57 2023

@author: kerim
"""





# clubs_t DataFrame'ini oluşturun
clubs_t = fm22d.drop_duplicates(subset=['Club'])
clubs_t.reset_index(drop=True, inplace=True)

# Based sütununu bölerek League ve Country sütunlarını elde edin
clubs_t[['League', 'Country']] = clubs_t['Based'].str.split(' \(', 1, expand=True)
clubs_t['Country'] = clubs_t['Country'].str.replace(')', '')

# Gereksiz sütunları kaldırın
clubs_t.drop(columns=['Based', 'Division'], inplace=True)

print(clubs_t)


# clubs_t DataFrame'ini sadece istediğiniz sütunları içerecek şekilde oluşturun
clubs_t = fm22d[['Based', 'Division', 'Club', 'nations_copy']].copy()

# Based sütununu bölerek League ve Country sütunlarını elde edin
clubs_t[['Country', 'Leauge']] = clubs_t['Based'].str.split(' \(', 1, expand=True)
clubs_t['Country'] = clubs_t['Country'].str.replace(')', '')


# clubs_t DataFrame'ini distinct (benzersiz) Club'lara göre oluşturun
clubs_t.drop_duplicates(subset=['Club'], inplace=True)
clubs_t.reset_index(drop=True, inplace=True)

print(clubs_t)

clubs_t.to_excel("clubs_t.xlsx", index=False)



empty_club_rows = fm22d[fm22d['Club'].isnull()]
print(empty_club_rows)


#
clubs_t= pd.read_excel("clubs_t.xlsx")

clubs_t.info()








clubs_d = fm22d[['Division', 'Club', 'nations_copy']].copy()

print(clubs_d.describe())

print(clubs_d.info())

clubs_d.isnull().any()
clubs_d.isna().any()


# Boşlukları silmek için strip() fonksiyonunu uygulayın
clubs_d['Division'] = clubs_d['Division'].str.strip()
clubs_d['Club'] = clubs_d['Club'].str.strip()
clubs_d['nations_copy'] = clubs_d['nations_copy'].str.strip()


distinct_clubs_df = clubs_d.dropna(subset=['Club']).drop_duplicates(subset=['Division', 'Club']).reset_index(drop=True)

distinct_leagues_df = clubs_d.groupby(['Division', 'nations_copy']).agg({'Club': 'first'}).reset_index()

distinct_leagues_df.drop_duplicates(subset=['Division'], keep='first', inplace=True)


division_counts = distinct_clubs_df['Division'].value_counts().reset_index()
division_counts.columns = ['Division', 'Count']
distinct_leagues_df.describe()


# Division sütununu "division_counts" DataFrame'inin "Division" sütunu ile karşılaştırın
distinct_in_df_not_in_counts = distinct_leagues_df[~distinct_leagues_df['Division'].isin(division_counts['Division'])]

print("distinct_leagues_df'de olan ve division_counts'da olmayan değerler:")
print(distinct_in_df_not_in_counts)


#Not 16 lig farkı aynı isimde kulüp olmasından distinct clubs yaptığında o tabloda 16 tane ligde kayıp yaşanıyor.

clubs_d.to_excel("clubs_d.xlsx", index=False)
division_counts.to_excel("division_counts.xlsx")
distinct_clubs_df.to_excel("distinct_clubs_df.xlsx")
distinct_leagues_df.to_excel("distinct_leagues_df .xlsx")













# clubs tablosu 

import pandas as pd

distinct_clubs_df = pd.read_excel("distinct_clubs_df.xlsx")
distinct_clubs_df['Division'] = distinct_clubs_df['Division'].replace('-', 'Unknown')


distinct_clubs_df = distinct_clubs_df.iloc[:,1:]


distinct_clubs_df = distinct_clubs_df.reindex(columns=['Club', *distinct_clubs_df.columns.difference(['Club'])])


# 'nations_copy', 'Division' ve 'Club' sütunlarına göre alfabetik olarak DataFrame'i sıralayın
distinct_clubs_df = distinct_clubs_df.sort_values(by=['nations_copy', 'Division', 'Club'])

# Indexleri sıfırlayın
distinct_clubs_df = distinct_clubs_df.reset_index(drop=True)

nations = pd.read_excel("nations.xlsx")
leauges = pd.read_excel("leauges.xlsx")


distinct_clubs_df['league_id'] = distinct_clubs_df['Division'].map(leauges.set_index('league_name')['leauge_id'])
distinct_clubs_df['nation_id'] = distinct_clubs_df['Division'].map(leauges.set_index('league_name')['nation_id'])


distinct_clubs_df.to_excel("clubs_table.xlsx")


