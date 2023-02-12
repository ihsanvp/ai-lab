from pathlib import Path
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

DATA_FILE = Path(__file__).parent / "car_evaluation.csv"

df = pd.read_csv(DATA_FILE,
                 names=[
                     "buying_price", "maint_cost", "doors", "person_capacity",
                     "lug_boot", "safety", "class"
                 ],
                 header=None)

target_feature = "class"
input_features = list(filter(lambda x: x != target_feature, df.columns))

X = df[input_features]
Y = df[[target_feature]]

enc = OneHotEncoder().fit(X)

print(input_features)
print(X.head())
print(Y.head())

print(enc.transform(X))