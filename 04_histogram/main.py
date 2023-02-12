import pandas as pd
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DATA_FILE = CURRENT_DIR / "data.csv"

df = pd.read_csv(DATA_FILE, low_memory=False)
df_new = df[df["SITE_NAME"] == "Swale at Catterick Bridge"]

t = df_new["Temperature water continuous"].astype(float)
o = df_new["Oxygen dissolved continuous"].astype(float)

print("mean of temperature =", np.mean(t))
print("median of dissolved oxygen =", st.median(o))

t.hist()
plt.title("Histogram")
plt.xlabel("Temperature")
plt.show()