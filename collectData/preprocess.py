import pandas as pd
import pickle

"""
df1 = pd.read_pickle("finalDataset")
df2 = pd.read_pickle("finalDataset2")

finalDF = pd.concat([df1,df2])
finalDF.to_pickle("finalDF")
"""


"""
def convert(x):
    x = x.replace("[","")
    x = x.replace("]","")
    x = x.replace("'","")
    x = x.replace(" ","")
    x = x.split(",")
    return x

df["Tags"] = df["Tags"].apply(lambda x: convert(x))

print(df.head())

df.to_pickle("finalDataset2")
"""
