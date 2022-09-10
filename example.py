from scraper import get_data

table = get_data()
selected_table = table[(table['Attribute_Types'] == 'Real')
                       & (table['Data_Types'] == 'Multivariate')
                       ]
selected_table.to_csv('selected_data.csv')