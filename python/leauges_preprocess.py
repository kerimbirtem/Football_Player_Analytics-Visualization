# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:15:51 2023

@author: kerim
"""




leauges_df = pd.read_excel("leauges_1.xlsx")


# leagues_df DataFrame'indeki hücrelerin başındaki ve sonundaki boşlukları temizle
leauges_df = leauges_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# df DataFrame'indeki hücrelerin başındaki ve sonundaki boşlukları temizle
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Eşleştirme işlemini gerçekleştirelim
for index, row in leauges_df.iterrows():
    nation_copy_value = row['nations_copy']
    matched_row = df[df['nation_full'] == nation_copy_value]
    if not matched_row.empty:
        leauges_df.at[index, 'nation_id'] = matched_row['nation_id'].values[0]

distinct_nations_copy = leauges_df['nations_copy'].unique()
print(distinct_nations_copy)



# df DataFrame'inin sütun isimlerini yazdır
print("df DataFrame sütun isimleri:")
print(list(df.columns))

# leauges_df DataFrame'inin sütun isimlerini yazdır
print("\nleauges_df DataFrame sütun isimleri:")
print(list(leauges_df.columns))



# Eşleştirme işlemini gerçekleştirelim
merged_df = leauges_df.merge(df[['nation_id', 'nation_full']], left_on='nations_copy', right_on='nation_full', how='left')

# Yalnızca gerekli sütunları alalım
leauges_df['nation_id'] = merged_df['nation_id_y']




# "leauges_df" veri setini "df" veri seti ile birleştirelim
merged_df = leauges_df.merge(df[['nation_id', 'nation_continent', 'nation_full']], left_on='nations_copy', right_on='nation_full', how='left')

# Yalnızca gerekli sütunları alalım ve gereksiz sütunları kaldıralım
leauges_df['nation_id'] = merged_df['nation_id_y']
leauges_df['nation_continent'] = merged_df['nation_continent']

nan_leauges = leauges_df[leauges_df['nation_id'].isna()].copy()


# "nations_copy" sütunundaki verileri distinct olacak şekilde "distinct_nan_leagues" DataFrame'ine aktaralım
distinct_nan_leauges = nan_leauges.drop_duplicates(subset='nations_copy', keep='first').copy()


leauges_df = leauges_df.drop(columns=['nations_copy', 'nation_id_x'])



# "nation_full" ve "nation_id" sütunlarından bir sözlük oluşturalım
nation_dict = df.set_index('nation_full')['nation_id'].to_dict()

# "nations_copy" sütunundaki değerlere göre "nation_id" sütununu dolduralım
leauges_df['nation_id'] = leauges_df['nations_copy'].map(nation_dict)