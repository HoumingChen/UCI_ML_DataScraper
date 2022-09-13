import pandas as pd
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def get_data():
    page = requests.get("https://archive.ics.uci.edu/ml/datasets.php")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', {'border': '1', 'cellpadding': '5'})
    datasets_list = []
    for c in list(table.children):
        new_dataset = {}
        for d in c.children:
            if isinstance(d, NavigableString):
                continue
            if isinstance(d, Tag):
                info = str(d.p.contents)
                if 'datasets/' in info:
                    new_dataset["Name"] = str(d.p.contents[0].contents[0].contents[0])
                    new_dataset["Link"] = 'https://archive.ics.uci.edu/ml/' + str(d.p.contents[0].contents[0]['href'])
                elif 'Name' in new_dataset:
                    content = str(d.p.contents[0])
                    content = content.replace(u'\xa0', u'')
                    if 'Data_Types' not in new_dataset:
                        new_dataset['Data_Types'] = content
                    elif 'Default_Task' not in new_dataset:
                        new_dataset['Default_Task'] = content
                    elif 'Attribute_Types' not in new_dataset:
                        new_dataset['Attribute_Types'] = content
                    elif 'Instances' not in new_dataset:
                        new_dataset['Instances'] = content
                    elif 'Attributes' not in new_dataset:
                        new_dataset['Attributes'] = content
                    elif 'Year' not in new_dataset:
                        new_dataset['Year'] = content
        if 'Name' in new_dataset:
            datasets_list.append(new_dataset.copy())
    table = pd.DataFrame(datasets_list)
    return table




