#instalar pip
#"python -m pip install --upgrade pip"

 #istalar bibliotecas
#"pip install requests" #exemplo
#"python -m pip install -U matplotlib"

# import
import requests
import pandas as pd
import json
import numpy as np
import os
import matplotlib.pyplot as plt
import string


#mudando o wd
os.chdir('C:/Users/03001419')

#request api
#poderia ocorrer um input
def requestRandUsr():
    url = "https://randomuser.me/api/?results=500"
    data = requests.get(url).json()
    return data

#criando um arquivo json
json_obj = json.dumps(requestRandUsr(), indent=4)

with open('rduser.json', 'w') as outfile:
    outfile.write(json_obj)

#lendo o arquivo json
json_file = json.load(open('rduser.json'))
#dict
results = json_file['results']
#convertendo o arquivo
results_normal = pd.json_normalize(results)
#criando df
df = pd.DataFrame(results_normal)
#criando csv
df.to_csv('df.csv')

#lendo csv
csv = pd.read_csv('C:/Users/03001419/df.csv')
df = pd.DataFrame(csv)

#colunas
for col in df.columns:
    print(col)

#formatando números
df['phone'] = df['phone'].str.replace('\W', '')
df['cell'] = df['cell'].str.replace('\W', '')

#gerando o relatório

#dividindo em gênero
df_gender = df['gender']
df_gender
#dividindo em país
df_country = df['location.country']
df_country

df_gender = (df_gender.value_counts()/df_gender.value_counts().sum())*100

df_country = (df_country.value_counts()/df_country.value_counts().sum())*100

df_gender = df_gender.reset_index()
df_gender = df_gender.rename(columns={'index':'Gêneros', 'gender': 'Percentual'})
df_gender

df_country = df_country.reset_index()
df_country = df_country.rename(columns={'index':'País', 'location.country': 'Percentual'})
df_country

#criando arquivo de texto
df_gender.to_csv(r'C:\Users\03001419\df_gender.txt', header=None, index=None, sep='\t', mode='a')
text = df_country.to_csv(r'C:\Users\03001419\df_country.txt', header=None, index=None, sep='\t', mode='a')
file_object = open('df_gender.txt', 'a')
with open("sample.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write(text)

df_country.head()