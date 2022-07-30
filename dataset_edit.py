import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
mood = ["Happy","Sad","Neutral"]
genre = ["Action","Horror","Thriller","Drama","Biopic","Fantasy","Sci/Fi","Comedy","Animated","Romantic"]
age = ["G-rated","PG-Rated","PG-13 Rated","R-Rated"]
ocn = ["Family","Friends","Date-Night","Alone"]
year = ["past 10 years","Past 20 years","Past 5 years","Recent"]
data = pd.read_excel("movies.xlsx")
updt = pd.ExcelWriter("final.xlsx")
data.drop('genres',axis=1,inplace=True)
data.to_excel(updt,'Sheet1')
# updt.save()
moodf = []
for i in range(data['title'].size):
    moodf.append(random.randint(0,2))
moods=[]
for i in moodf:
    moods.append(mood[i])
df = data.assign(Mood = moods)
df.to_excel(updt,'Sheet1')
genf = []
for i in range(data['title'].size):
    genf.append(random.randint(0,9))
gens=[]
for i in genf:
    gens.append(genre[i])
df2 = df.assign(Genre = gens)
df2.to_excel(updt,'Sheet1')
agef = []
for i in range(data['title'].size):
    agef.append(random.randint(0,3))
ages=[]
for i in agef:
    ages.append(age[i])
df3 = df2.assign(Age = ages)
df3.to_excel(updt,'Sheet1')

ocnf = []
for i in range(data['title'].size):
    ocnf.append(random.randint(0,3))
ocns=[]
for i in ocnf:
    ocns.append(ocn[i])
df4 = df3.assign(Occasion = ocns)
df4.to_excel(updt,'Sheet1')

yrf = []
for i in range(data['title'].size):
    yrf.append(random.randint(0,3))
yrs=[]
for i in yrf:
    yrs.append(year[i])
df5 = df4.assign(Year = yrs)
df5.to_excel(updt,'Sheet1')
updt.save()

