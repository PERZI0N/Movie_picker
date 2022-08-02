import pandas as pd
import numpy as np
df = pd.read_excel("final.xlsx")
genre = ["Action","Horror","Thriller","Drama","Biopic","Fantasy","Sci/Fi","Comedy","Animated","Romantic"]
writer = pd.ExcelWriter("Mood.xlsx")
for i in range(2,df['title'].size):
    if(df.iloc[i]['Genre']):
        df.iloc[i][]
print(df.iloc[5]['title'])