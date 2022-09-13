from scraper import get_data
import pandas as pd


def has_classifiation(input_str):
    return 'Classification' in input_str

def is_numerical(input_str):
    print(input_str)
    if input_str == 'Integer':
        return True
    if input_str == 'Real':
        return True
    if input_str == 'Integer, Real':
        return True
    if input_str == 'Real, Integer':
        return True
    return False

table = get_data()
table['Instances'] = pd.to_numeric(table['Instances'])
table['Attributes'] = pd.to_numeric(table['Attributes'])

selected_table = table[(table['Data_Types'] == 'Multivariate')
                       & (table['Instances'] < 1000)
                       & (table['Attributes'] < 100)
                       ]

selected_table = selected_table.loc[selected_table['Attribute_Types'].apply(is_numerical)]
selected_table = selected_table.loc[selected_table['Default_Task'].apply(has_classifiation)]
selected_table.to_csv('selected_data.csv')
