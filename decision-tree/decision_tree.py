import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("car_evaluation.csv", names=["buying_price", "maint_cost", "doors", "person_capacity", "lug_boot", "safety", "class"], header=None)

input_features = df.columns[:-1]
target_features = df.columns[-1]

X = df[input_features]
Y = df[target_features]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2)
enc = OneHotEncoder(sparse=False, handle_unknown="ignore")
enc.fit(X_train)

encoded_features = enc.get_feature_names_out(X_train.columns)
X_train[encoded_features] = enc.transform(X_train)
X_test[encoded_features] = enc.transform(X_test)

X_train.drop(columns=input_features, axis=1, inplace=True)
X_test.drop(columns=input_features, axis=1, inplace=True)

clf = tree.DecisionTreeClassifier(criterion="gini")
clf.fit(X_train, Y_train)

plt.figure(figsize=(120, 100))
plt.title("Decision Tree Classification using Gini Index")
tree.plot_tree(clf, max_depth=10, filled=True, rounded=True, feature_names=X_train.columns, class_names=clf.classes_)

print("train dataset size:", X_train.shape)
print("test dataset size:", X_test.shape)
print("accuracy of train :", clf.score(X_train, Y_train))
print("accuracy of test :", clf.score(X_test, Y_test))

plt.show()
