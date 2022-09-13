from scraper import get_data
import pandas as pd


def has_classifiation(input_str):
    return 'Classification' in input_str

table = get_data()
table['Instances'] = pd.to_numeric(table['Instances'])
table['Attributes'] = pd.to_numeric(table['Attributes'])

selected_table = table[(table['Attribute_Types'] == 'Real')
                       & (table['Data_Types'] == 'Multivariate')
                       & (table['Instances'] < 1000)
                       & (table['Attributes'] < 100)
                       ]

selected_table = selected_table.loc[selected_table['Default_Task'].apply(has_classifiation)]
selected_table.to_csv('selected_data.csv')
pd.set_option('display.max_columns', None)
print(selected_table)
print(selected_table.shape)
