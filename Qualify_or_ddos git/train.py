import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Defining the DataSet preprocessing Function
def dataset(area):
    data = pd.read_csv("C:\\datafiles\\crop_production.csv")
    del data["District_Name"]
    # del data["Crop_Year"]
    X = data[["Area","Crop_Year"]]
    y = data["Production"]
    X = X.dropna()
    y = y.dropna()
    X = X[:242361]
    X.shape
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
    # Instantiating the Classifier
    clf =  GradientBoostingRegressor()
    # Fitting the model
    clf.fit(X_train,y_train)
    # Predicting the results
    z=clf.predict([[area,2000]])
    print(z)
    return(z)