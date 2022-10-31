import pandas as pd
import statistics as st
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", low_memory=False)

#print(df.head())
#print(df["SITE_NAME"])
df_new = df.query("SITE_NAME == 'Swale at Catterick Bridge'")

t = df_new["Temperature water continuous"].astype(float)
o = df_new["Oxygen dissolved continuous"].astype(float)

print("mean of temperature =", np.mean(t))
print("median of dissolved oxygen =", st.median(o))

t.hist()
plt.title("Histogram")
plt.xlabel("Temperature")
plt.show()
