import pandas as pd

#import csv file

cities_df = pd.read_csv('Resources\cities.csv')


cities_df = cities_df.drop(columns=['Unnamed: 0'])

html = cities_df.to_html()
print(html)

#write html to file
html_file = open("data.html", "w")
html_file.write(html)
html_file.close()
