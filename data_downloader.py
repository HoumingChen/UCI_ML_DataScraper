import urllib

import pandas as pd
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

import os
if not os.path.exists('download'):
    os.makedirs('download')

def download(base_path, page_link):
    page = requests.get(page_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(f"*{page_link}")
    children = soup('ul')[0].findChildren("li")
    for child in children:
        file_name = child.a['href']
        if 'ml/machine-learning-databases' in file_name:
            continue
        if file_name == 'Index':
            continue
        print(page_link + file_name)
        if file_name[-1] == '/':
            new_page_link = page_link + file_name
            new_base_path = os.path.join(base_path, file_name)
            if not os.path.exists(new_base_path):
                os.makedirs(new_base_path)
            download(new_base_path, new_page_link)
        else:
            download_link = page_link + file_name
            download_path = os.path.join(base_path, file_name)
            urllib.request.urlretrieve(download_link, download_path)


selected_table = pd.read_csv('selected_data.csv')
base_link = 'https://archive.ics.uci.edu/ml/'
for index, row in selected_table.iterrows():
    name = row['Name'].replace(':', '_').replace(' ', '_')
    dataset_path = os.path.join('download', name)
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
    print(row['Link'])
    page = requests.get(row['Link'])
    soup = BeautifulSoup(page.content, 'html.parser')
    if soup('a',text='Data Folder'):
        datafolder_element = (soup('a',text='Data Folder'))[0]
        link = base_link + datafolder_element['href'][3:]
        download(dataset_path, link)

