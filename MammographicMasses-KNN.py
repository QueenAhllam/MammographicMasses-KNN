import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , classification_report

data =pd.read_csv("mammographic_masses.data",)

data.columns = ["BIRADS", "Age" , "Shape", "Margin" , "Density", "Severity"]


data.BIRADS = pd.to_numeric(data.BIRADS , errors="coerce" ) # type: ignore
data.Age = pd.to_numeric(data.Age, errors= "coerce")
data.Shape = pd.to_numeric(data.Shape , errors="coerce")
data.Margin = pd.to_numeric(data.Margin , errors= "coerce")
data.Density = pd.to_numeric(data.Density , errors="coerce" )

data = data.dropna().reset_index(drop=True)

y= data["Severity"]
x=data.drop("Severity", axis=1)
# print(y.shape)
# print(x.shape)

#knn
X_train, X_test, y_train, y_test = tts(x, y, shuffle=True, test_size=0.15, random_state=42)
# model = KNeighborsClassifier(n_neighbors= 5, p=2, weights="uniform")
model = KNeighborsClassifier(n_neighbors= 5, p=2, weights="distance")

model.fit(X_train, y_train)
y_hat = model.predict(X_test)
# # print(y_test, y_hat)

# print(accuracy_score(y_test, y_hat))

# print(classification_report(y_test, y_hat))


for k in range (3,30,2):
    model = KNeighborsClassifier(n_neighbors=k , p=2, weights="distance").fit(X_train, y_train)
    y_hat = model.predict(X_test)
    print(f"acc k = {k} : {accuracy_score(y_test,y_hat)}")


Did you like it? Be sure to share your thoughts with me!
👑 I can send you more code  privately if you'd like. And don't forget where you are  —  you’re on Queen Ahllam’s page! 💖✨
