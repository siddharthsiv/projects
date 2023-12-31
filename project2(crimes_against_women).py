# -*- coding: utf-8 -*-
"""project2(crimes against women).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PEdz2QRVnjp6QfB2eWCFk4jLJu3D-o6p
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import jovian

!pip install jovian --upgrade --quiet pip

jovian.commit(project='crime-against-women', environment=None)

from google.colab import files
uploaded=files.upload()

data=pd.read_csv('crimes_against_women_2001-2014.csv')
data

data.dropna()
data

data.info()

data.describe()

districts = len(data.DISTRICT.unique())
districts

data.drop(['DISTRICT', 'Unnamed: 0'], axis = 1, inplace=True)

data.rename( columns = {'Kidnapping and Abduction':'Kidnapping_Abduction','Dowry Deaths':'Dowry_Deaths',
                             'Assault on women with intent to outrage her modesty':'Hurting_of_womens_modesty',
                             'Insult to modesty of Women':'Insult_to_womens_modesty',
                             'Cruelty by Husband or his Relatives':'Domestic_Cruelty',
                             'Importation of Girls':'Importation_of_Girls'}, inplace = True)
data

states=len(data['STATE/UT'].unique())
states

print(data['STATE/UT'].unique())

def remove_uppercase(r):
    r = r['STATE/UT'].strip()
    r = r.upper()
    return r
data['STATE/UT'] = data.apply(remove_uppercase, axis=1)

data['STATE/UT'].replace("A&N ISLANDS", "A & N ISLANDS", inplace = True)
data['STATE/UT'].replace("D&N HAVELI", "D & N HAVELI", inplace = True)
data['STATE/UT'].replace("DELHI UT", "DELHI", inplace = True)

print(data['STATE/UT'].unique())

data

fig, axes = plt.subplots(2, 3, figsize=(25, 12))

axes[0,0].set_title("Chart of rape cases in India in 2001-2014")
axes[0,0].bar(data.Year, data.Rape, color = 'black');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Rape in India') #Y-axis

axes[0,1].set_title("Chart of Kidnapping and Abduction cases in India in 2001-2014")
axes[0,1].bar(data.Year,data.Kidnapping_Abduction, color = 'violet');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Kidnapping and Abduction in India') #Y-axis

axes[0,2].set_title("Chart of Dowry death cases in India in 2001-2014")
axes[0,2].scatter(data.Year, data.Dowry_Deaths, color = 'navy');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Dowry deaths in India') #Y-axis

axes[1,0].set_title("Chart of Assault to her modesty in 2001-2014")
axes[1,0].bar(data.Year, data.Hurting_of_womens_modesty, color = 'cyan');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Assaulting a women for her modesty in India') #Y-axis

axes[1,1].set_title("Chart of Domestic Violence cases in India in 2001-2014")
axes[1,1].scatter(data.Year, data.Domestic_Cruelty, color = 'orange');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases of Domestic Violence in India') #Y-axis

axes[1,2].set_title("Chart of Importation of girls in India in 2001-2014")
axes[1,2].bar(data.Year, data.Importation_of_Girls, color = 'red');
plt.xlabel('Year') #X-axis
plt.ylabel('Cases ofImportation of girls in India') #Y-axis

plt.figure(figsize=(20,8))
plt.xticks(rotation=75)
plt.title("States with most crime")
sns.barplot(x=data['Rape'],y=data['STATE/UT'])

count_df = data.groupby('Year')[['STATE/UT']].count()
count_df

plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
plt.title("States with most crime")
sns.heatmap(count_df)