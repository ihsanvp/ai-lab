import pandas as pd
import statistics as st

df = pd.read_csv("data.csv")

#print(df.head())
#print(df["SITE_NAME"])
fl = df.query("SITE_NAME == 'Swale at Catterick Bridge'")
mean_temp = fl['Oxygen dissolved continuous'].astype("int32", errors="ignore")
print(fl.columns)
print(mean_temp)
