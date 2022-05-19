import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import pickle

model_data = pd.read_csv("data/processed/Well_3_modeldata.csv", index_col=[0])

X = model_data[["DT","GR","RHOB", "RLLD_log"]]
Y = model_data["NPHI"]

model_pipeline = Pipeline(steps = [
    ("scaler", StandardScaler()),
    ("poly_transform", PolynomialFeatures(degree = 2)),
    ("regression", LinearRegression())])

model_pipeline.fit(X, Y)


filename = "new_model"
with open(filename, 'wb') as archivo_salida:
    pickle.dump(model_pipeline, archivo_salida)