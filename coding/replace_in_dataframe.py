import pandas as pd
import logging
logging.basicConfig(filename="tokenlog.log",level=logging.INFO,format='%(message)s')

def replacing(i):
    chars = ['"',"'"]
    for j in chars:
        if j in i:
            i=i.replace(j,"")
    return i

def replacing1(i):
    if len(i)>2:
        return i

df123=pd.read_csv("path/to/csv")#,encoding='latin-1')
print("df123:",df123)
df123['Header'] = df123['Header'].apply(replacing)
df123['Header1'] = df123['Header'].apply(replacing1)

df123.dropna(inplace=True)
print("df123:",df123)

df123['Header1'] = df123['Header1'].str.lower()
df1234=df123['Header1']
print("df1234",df1234)
