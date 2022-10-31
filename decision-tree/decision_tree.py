from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car_evaluation.csv")

print(df.columns[-1])
print(df.shape)

Y = df.pop(df.columns[-1])
X = df

clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)

tree.plot_tree(clf)
plt.show()
