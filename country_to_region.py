

def country_to_region(str):
    if(str in States_Ex_Yugoslavia):
        return '88'
    elif(str in Europe):
        return '89'
    elif(str in North_Sahara):
        return '189'
    elif(str in South_Sahara):
        return '289'
    elif(str in Africa):
        return '298'
    elif(str in West_Indies):
        return '380'
    elif(str in North_and_Central_America):
        return '389'
    elif(str in South_America):
        return '489'
    elif(str in America):
        return '498'
    elif(str in Middle_East):
        return '589'
    elif(str in Central_Asia):
        return '619'
    elif(str in South_Asia):
        return '679'
    elif(str in South_and_Central_Asia):
        return '689'
    elif(str in Far_East_Asia):
        return '789'
    elif(str in Asia):
        return '798'
    elif(str in Oceania):
        return '889'
    else:
        return '998'



States_Ex_Yugoslavia = ['Bosnia and Herzegovina','Croatia','Macedonia','Montenegro','Serbia','Slovenia']

Europe = ['Albania''Andorra','Austria','Belarus','Belgium','Bulgaria''Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland',
'Ireland','Italy','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Netherlands','Norway','Poland','Portugal','Romania','Russia',
'San Marino','Slovakia','Spain','Sweden','Switzerland','Ukraine','United Kingdom'
]

North_Sahara = [ 'Algeria', 'Egypt', 'Libya', 'Morocco', 'Sudan', 'Tunisia' ]

South_Sahara = ['Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Comoros',"""Congo [Republic]""",
'Democratic Republic of Congo',"""Côte d'Ivoire""",'Djibouti','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Kenya',
'Lesotho','Liberia', 'Madagascar','Malawi','Mali','Mauritania','Mauritius','Mozambique','Namibia','Niger','Nigeria','Réunion','Rwanda','São Tomé and Príncipe','Senegal',
'Seychelles','Sierra Leone','Somalia','South Africa','Sudan','Swaziland','Tanzania','Togo','Uganda','Western Sahara','Zambia','Zimbabwe']

Africa = []

West_Indies = ['Bahamas','Barbados','Cuba','Jamaica','Haiti','Dominican Republic','Puerto Rico','U.S. Virgin Islands','British Virgin Islands', 'Anguilla',
'Saint Lucia','Dominica', 'Saint Vincent and the Grenadines', 'Grenada', 'Martinique','Guyana','Suriname','Trinidad and Tobago'
]

North_and_Central_America = ['United States','Belize', 'Canada', 'Costa Rica', 'Cuba', 'El Salvador', 'Guatemala', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama']

South_America = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Uruguay','Venezuela']

America = []

Middle_East = ['Bahrain','Cyprus','Egypt','Iran','Iraq','Israel','Jordan','Kuwait','Lebanon','Oman','Qatar','Saudi Arabia','Syria','Turkey','United Arab Emirates','Yemen']

Central_Asia = ['Afghanistan', 'Kyrgyzstan','Tajikistan','Turkmenistan','Mongolia','Kazakhstan','Uzbekistan']

South_Asia = ['Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']

South_and_Central_Asia = []

Far_East_Asia = ['China', 'Hong Kong', 'Macau', 'Japan', 'North Korea', 'South Korea', 'Siberia', 'Taiwan','Brunei', 'Cambodia','East Timor', 'Malaysia', 'Laos',
'Indonesia','Myanmar','Singapore','Philippines','Thailand','Vietnam']

Asia = ['Armenia','Bahrain','Cyprus','Georgia','Iran','Iraq','Israel','Jordan','Kuwait','Lebanon','Oman','Palestine','Philippines','Qatar','Russia','Saudi Arabia',
'Syria','Timor-Leste','Turkey','United Arab Emirates ','Yemen']

Oceania = ['Australia','New Zealand','New Caledonia','Papua New Guinea','Fiji','Solomon Islands','Vanuatu','French Polynesia','Samoa','Guam','Kiribati','Tonga',
'Micronesia','Marshall Islands','Northern Mariana Islands','American Samoa','Palau','Cook Islands','Wallis and Futuna ','Tuvalu','Nauru','Norfolk Island',
'Niue ','Tokelau','Pitcairn Islands']

Developing_countries_unspecified = []
