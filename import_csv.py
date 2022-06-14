import csv
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

#read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
df = pd.read_csv (r'D:\Users\yaima\Documents\Projects\players_20.csv')   

# # Name of columns
# print("\n")
# print("CSV File columns' names")
# print("\n")
# for col in df.columns:
#     print(col, end = ", ")
# print("\n")

# # Number of rows and columns
# print("CSV File number of rows and columns")
# print("\n")
# count_row = df.shape[0] # Gives number of rows
# count_col = df.shape[1] # Gives number of columns
# print(f"The number of rows in this dataset are {count_row}")
# print(f"The number of columns in this dataset are {count_col}")
# print("\n")

# # Load the csv file and show top 5 records from it.
# print("Top 5 records from CSV File")
# print("\n")
# print(df.head()) 
# print("\n")

# # Group by number of players and their countries.
# print("CSV File number of players and their countries")
# print("\n")
# gr = df.groupby(['nationality', 'short_name'])
# print(gr.first())
# print("\n")

# # # Top 10 countries and their number of players.
# print("\n")
# gr = df.groupby('nationality').count()
# df5 = pd.DataFrame(gr, columns= ['short_name'])
# print(df5.nlargest(10, 'short_name'))
# print("\n")

# Top 5 countries and their number of players, try to fill green color in bars.
# print("\n")
# gr = df.groupby('nationality').count()
# df5 = pd.DataFrame(gr, columns= ['short_name'])
# plotdata = df5.nlargest(5, 'short_name')
# print(plotdata)
# plotdata = plotdata.plot(df5, plotdata, color='g')
# print(plotdata.plot(kind="bar"))
# print("\n")
countries = df.groupby(['nationality'], as_index=False)['short_name'].count()
country_bar = countries.nlargest(5,'short_name')

print(country_bar)
# country_bar = plotdata.head()
# print(country_bar)
plt.figure(figsize=(15,6))
plt.bar(country_bar['nationality'],country_bar['short_name'],color='green')
plt.xlabel('Nationality', size = 15)
plt.ylabel('Number of Players', size=15)
plt.title('Players per Country')
plt.show()

