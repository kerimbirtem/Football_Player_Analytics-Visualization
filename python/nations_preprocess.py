# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:22:34 2023

@author: kerim
"""


# nations table düzenlemeleri

# nation tablosu olusturma 

nations_table = data[['nation']].copy()
unique_nations = nations_table['nation'].unique()
unique_nations_df = pd.DataFrame({'nation': unique_nations})

unique_nations_df = unique_nations_df.sort_values(by='nation')
unique_nations_df.reset_index(drop=True, inplace=True)

print(unique_nations_df)


# Iso 3166-3 standartlarına göre ülke kodları

country_codes = [
    ("AFG", "Afghanistan"),
    ("AIA", "Anguilla"),
    ("ALB", "Albania"),
    ("ALG", "Algeria"),
    ("AND", "Andorra"),
    ("ANG", "Angola"),
    ("ARG", "Argentina"),
    ("ARM", "Armenia"),
    ("ARU", "Aruba"),
    ("ASA", "American Samoa"),
    ("ATG", "Antigua & Barbuda"),
    ("AUS", "Australia"),
    ("AUT", "Austria"),
    ("AZE", "Azerbaijan"),
    ("BAH", "Bahamas"),
    ("BAN", "Bangladesh"),
    ("BDI", "Burundi"),
    ("BEL", "Belgium"),
    ("BEN", "Benin"),
    ("BER", "Bermuda"),
    ("BFA", "Burkina Faso"),
    ("BHR", "Bahrain"),
    ("BHU", "Bhutan"),
    ("BIH", "Bosnia & Herzegovina"),
    ("BLM", "Saint Barthélemy"),
    ("BLR", "Belarus"),
    ("BLZ", "Belize"),
    ("BOE", "Bonaire"),
    ("BOL", "Bolivia"),
    ("BOT", "Botswana"),
    ("BRA", "Brazil"),
    ("BRB", "Barbados"),
    ("BRU", "Brunei Darussalam"),
    ("BUL", "Bulgaria"),
    ("CAM", "Cambodia"),
    ("CAN", "Canada"),
    ("CAY", "Cayman Islands"),
    ("CGO", "Congo"),
    ("CHA", "Chad"),
    ("CHI", "Chile"),
    ("CHN", "China"),
    ("CIV", "Ivory Coast"),
    ("CMR", "Cameroon"),
    ("COD", "Congo DR (Zaire)"),
    ("COK", "Cook Islands"),
    ("COL", "Colombia"),
    ("COM", "Comoros Islands"),
    ("CPV", "Cape Verde Islands"),
    ("CRC", "Costa Rica"),
    ("CRO", "Croatia"),
    ("CTA", "Central African Republic"),
    ("CUB", "Cuba"),
    ("CUW", "Curaçao"),
    ("CYP", "Cyprus"),
    ("CZE", "Czech Republic"),
    ("DEN", "Denmark"),
    ("DJI", "Djibouti"),
    ("DMA", "Dominica"),
    ("DOM", "Dominican Republic"),
    ("ECU", "Ecuador"),
    ("EGY", "Egypt"),
    ("ENG", "England"),
    ("EQG", "Equatorial Guinea"),
    ("ERI", "Eritrea"),
    ("ESP", "Spain"),
    ("EST", "Estonia"),
    ("ETH", "Ethiopia"),
    ("FIJ", "Fiji"),
    ("FIN", "Finland"),
    ("FLK", "Falkland Islands"),
    ("FRA", "France"),
    ("FRO", "Faroe Islands"),
    ("FSM", "Micronesia"),
    ("GAB", "Gabon"),
    ("GAM", "Gambia"),
    ("GEO", "Georgia"),
    ("GER", "Germany"),
    ("GHA", "Ghana"),
    ("GIB", "Gibraltar"),
    ("GLP", "Guadeloupe"),
    ("GNB", "Guinea-Bissau"),
    ("GRE", "Greece"),
    ("GRN", "Grenada"),
    ("GUA", "Guatemala"),
    ("GUF", "French Guiana"),
    ("GUI", "Guinea"),
    ("GUM", "Guam"),
    ("GUY", "Guyana"),
    ("HAI", "Haiti"),
    ("HKG", "Hong Kong"),
    ("HON", "Honduras"),
    ("HUN", "Hungary"),
    ("IDN", "Indonesia"),
    ("IND", "India"),
    ("IRL", "Ireland"),
    ("IRN", "Iran"),
    ("IRQ", "Iraq"),
    ("ISL", "Iceland"),
    ("ISR", "Israel"),
    ("ITA", "Italy"),
    ("JAM", "Jamaica"),
    ("JOR", "Jordan"),
    ("JPN", "Japan"),
    ("KAZ", "Kazakhstan"),
    ("KEN", "Kenya"),
    ("KGZ", "Kyrgyzstan"),
    ("KIR", "Kiribati"),
    ("KOR", "Korea Republic"),
    ("KSA", "Saudi Arabia"),
    ("KUW", "Kuwait"),
    ("KVX", "Kosovo"),
    ("LAO", "Laos"),
    ("LIB", "Lebanon"),
    ("LBR", "Liberia"),
    ("LBY", "Libya"),
    ("LCA", "St Lucia"),
    ("LES", "Lesotho"),
    ("LIE", "Liechtenstein"),
    ("LTU", "Lithuania"),
    ("LUX", "Luxembourg"),
    ("LVA", "Latvia"),
    ("MAC", "Macao"),
    ("MAD", "Madagascar"),
    ("MAR", "Morocco"),
    ("MAS", "Malaysia"),
    ("MAY", "Mayotte"),
    ("MON", "Monaco"),
    ("MDA", "Moldova"),
    ("MDV", "Maldives"),
    ("MEX", "Mexico"),
    ("MGL", "Mongolia"),
    ("MKD", "Macedonia FYR"),
    ("MLI", "Mali"),
    ("MLT", "Malta"),
    ("MNE", "Montenegro"),
    ("MOZ", "Mozambique"),
    ("MRI", "Mauritius"),
    ("MSR", "Montserrat"),
    ("MTN", "Mauritania"),
    ("MTQ", "Martinique"),
    ("MWI", "Malawi"),
    ("MYA", "Myanmar"),
    ("NAM", "Namibia"),
    ("NCA", "Nicaragua"),
    ("NCL", "New Caledonia"),
    ("NED", "Netherlands"),
    ("NEP", "Nepal"),
    ("NGA", "Nigeria"),
    ("NIG", "Niger"),
    ("NIR", "Northern Ireland"),
    ("NIU", "Niue"),
    ("NMI", "Northern Mariana Islands"),
    ("NOR", "Norway"),
    ("NZL", "New Zealand"),
    ("OMA", "Oman"),
    ("PAK", "Pakistan"),
    ("PLE", "Palestine"),
    ("PAN", "Panama"),
    ("PAR", "Paraguay"),
    ("PER", "Peru"),
    ("PHI", "Philippines"),
    ("PNG", "Papua New Guinea"),
    ("POL", "Poland"),
    ("POR", "Portugal"),
    ("PRK", "North Korea"),
    ("PUR", "Puerto Rico"),
    ("QAT", "Qatar"),
    ("REU", "Réunion"),
    ("ROU", "Romania"),
    ("RSA", "South Africa"),
    ("RUS", "Russia"),
    ("RWA", "Rwanda"),
    ("SAM", "Samoa"),
    ("SCO", "Scotland"),
    ("SUD", "Sudan"),
    ("SEN", "Senegal"),
    ("SEY", "Seychelles"),
    ("SIN", "Singapore"),
    ("SKN", "St Kitts & Nevis"),
    ("SLE", "Sierra Leone"),
    ("SLV", "El Salvador"),
    ("SMA", "Sint Maarten"),
    ("SMN", "Saint Martin"),
    ("SMR", "San Marino"),
    ("SOL", "Solomon Islands"),
    ("SOM", "Somalia"),
    ("SRB", "Serbia"),
    ("SRI", "Sri Lanka"),
    ("SSD", "South Sudan"),
    ("STP", "Sao Tome e Principe"),
    ("SUI", "Switzerland"),
    ("SUR", "Surinam"),
    ("SVK", "Slovakia"),
    ("SVN", "Slovenia"),
    ("SWE", "Sweden"),
    ("SWZ", "Swaziland"),
    ("SYR", "Syria"),
    ("TAH", "Tahiti"),
    ("TAN", "Tanzania"),
    ("TCA", "Turks & Caicos Islands"),
    ("TGA", "Tonga"),
    ("THA", "Thailand"),
    ("TJK", "Tajikistan"),
    ("TKM", "Turkmenistan"),
    ("TLS", "East Timor"),
    ("TOG", "Togo"),
    ("TPE", "Chinese Taipei"),
    ("TRI", "Trinidad & Tobago"),
    ("TUN", "Tunisia"),
    ("TUR", "Turkey"),
    ("TUV", "Tuvalu"),
    ("UAE", "United Arab Emirates"),
    ("UGA", "Uganda"),
    ("UKR", "Ukraine"),
    ("URU", "Uruguay"),
    ("USA", "United States of America"),
    ("UZB", "Uzbekistan"),
    ("VAN", "Vanuatu"),
    ("VEN", "Venezuela"),
    ("VGB", "British Virgin Islands"),
    ("VIE", "Vietnam"),
    ("VIN", "St Vincent & The Grenadines"),
    ("VIR", "United States Virgin Islands"),
    ("WAL", "Wales"),
    ("YEM", "Yemen"),
    ("ZAM", "Zambia"),
    ("ZIM", "Zimbabwe")
]

# Bosnia & Herzegovina , Netherlands, China , Ireland, Ivory Coast, North Korea değişmiştir.
country_dict = dict(country_codes)

sorted_countries = sorted(countries_full.items(), key=lambda x: x[1])


unique_nations_df['nation_full_name'] = unique_nations_df['nation'].map(country_dict)


# Filtrelenmiş DataFrame'i yazdırın
print(unique_nations_df[unique_nations_df['nation_full_name'].isna()])


# çıkan ülke kodları yani unique_nations_df yi kendim nations isimli excele atarak 
# id ve continent sütunlarını manuel oluşturdum.

nations = pd.read_excel('nations.xlsx')

# "Based" sütunundaki "nations_copy" sütununu oluşturun
fm22d['nations_copy'] = fm22d['Based'].str.split(' \(').str[0]



# İstenen değişiklikleri bir sözlükte tanımlayın:
replace_dict = {
    'Cape Verde': 'Cape Verde Islands',
    'South Korea': 'Korea Republic',
    'The Gambia': 'Gambia',
    'N.Ireland': 'Northern Ireland',
    'United States': 'United States of America',
    'Macau': 'Macao',
    'Zanzibar': 'Tanzania',
    'Comoros': 'Comoros Islands',
    'Crimea': 'Ukraine',
    'DR Congo': 'Congo DR (Zaire)',
    'U.A.E.': 'United Arab Emirates',
    'Central African Rep.': 'Central African Republic',
    'Eq. Guinea': 'Equatorial Guinea',
    'São Tomé & Príncipe': 'Sao Tome e Principe',
    'British Virgin Is.': 'British Virgin Islands',
    'Brunei': 'Brunei Darussalam'
}

# Veri çerçevesindeki 'nations_copy' sütunundaki değerleri replace metodu ile değiştirin:
fm22d['nations_copy'] = fm22d['nations_copy'].replace(replace_dict)

# Ülkelerin benzersiz bir listesini alın ve başındaki/sonundaki boşlukları kaldırın
unique_countries = fm22d['nations_copy'].str.strip().unique()


# Ülkelerin "nation_id" değerlerini belirleyin
nation_id_map = nations.set_index('nation_full')['nation_id']
nation_id_values = nation_id_map.loc[unique_countries].values

'''
"['Cape Verde', 'South Korea', 'The Gambia', 'N.Ireland', 'United States', 'Macau', 
 'Zanzibar', 'Comoros', 'Crimea', 'DR Congo', 'U.A.E.', 'Central African Rep.', 
 'Eq. Guinea', 'São Tomé & Príncipe', 'British Virgin Is.', 'Brunei'] not in index"
'''
# Yukarıdaki isimler değiştirildi.

nation_id_dict = nation_id_map.to_dict()

fm22d['nation_id'] = fm22d['nations_copy'].map(nation_id_dict)

#control 
# 'nation_id' sütunundaki sayılardan kaç adet olduğunu görmek için value_counts() kullanın:
count_values = fm22d['nation_id'].value_counts()

# 'nation_id' sütunundaki null değerlerin sayısını görmek için isnull() kullanın:
null_values = fm22d['nation_id'].isnull().sum()

print("Sayıdan kaç adet:")
print(count_values)

print("\nNull değer var mı?")
print(null_values)


# Gereksiz sütunları kaldırın ve sonuç tablosunu oluşturun
result_table = fm22d[['Division', 'Club', 'nation_id']]
result_table.columns = ['league_name', 'takım sayısı', 'nation_id']

print(result_table)


