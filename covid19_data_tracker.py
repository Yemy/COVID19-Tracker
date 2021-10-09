import requests as req
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


# request data from website
html = req.get("https://www.worldometers.info/coronavirus")
# check downloaded content
# html.content
# parse html with BeautifulSoup
html_parsed = BeautifulSoup(html.content, features="lxml")
# search for the required table
table = html_parsed.find('table', attrs={'id': 'main_table_countries_today'})
# check result
# table
# get all the rows
rows = table.find_all("tr")
# check result
# rows[0]
# remove the html tags
# rows[0].text.strip()
# tokenization
# rows[9].text.strip().split("\n")
# store rows into list (data).
data = []
for x in rows:
 data.append(x.text.strip().split("\n")[1:5]) # get only the first 9 columns

 # convert list into DataFrame
df = pd.DataFrame(data)
# check the DataFrame
# df.head()
# set the first row as the header, and remove the second row
df = pd.DataFrame(data[9:], columns=data[0])
# check the DataFrame
# df.head()
# save as csv file
df.to_csv('covid19.csv')
# get the required columns.
df_plot=df[['Country,Other','TotalCases']]
# get first 10 rows
df_plot = df_plot[:10]
# check the DataFrame
# df_plot.head()
# remove commas in digits, and convert string to int to plot the y axis
df_plot['TotalCases'] = df_plot['TotalCases'].apply(lambda x: x.replace(',', ''))
# check DataFrame
# print(df_plot.head())
# plot
# df_plot.plot(kind='bar',x='Country,Other',y='TotalCases')


from scipy import linalg

A = np.array([[3,4],[7,8]])
eigenvalue, eigenvector = linalg.eig(A)
print(eigenvector)
