from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np


def get_table_additives():
    url_web = "https://e-aditivos.com/"

    response = requests.get(url_web)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
            output_rows.append(output_row)
    additives= pd.DataFrame(output_rows,columns=['id','tipo','origen','aditivo','clasificación'])[1:]
    additives_obj = additives.select_dtypes(['object'])
    additives[additives_obj.columns] = additives_obj.apply(lambda item: item.str.strip())
    allergic_e = 'E-1404', 'E-1410', 'E-1412', 'E-1413', 'E-1414', 'E-1420', 'E-1422', 'E1440', 'E-1442', 'E-1450', 'E-4511', 'E-4512', 'E-4513', 'E-327', 'E-106', 'E-101', 'E-270', 'E-325', 'E-326', 'E-472', 'E-478', 'E-480', 'E-482', 'E-481', 'E-966', 'E-150', 'E-260', 'E-330', 'E-300'
    additives['aditivos_alergicos'] = np.where(additives['id'].isin(allergic_e), "Warning, this could kill you!", 'Dont worry, be happy!')
    additives['id'].replace('E-', 'E', regex=True, inplace=True)
    additives.drop_duplicates(keep='first',inplace=True)
    return additives
