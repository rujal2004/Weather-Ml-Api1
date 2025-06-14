import gdown
import zipfile
import os


url = "https://drive.google.com/uc?id=1jZlFxPBWil60vfv7nQgLNZJtcYEtYKTW" 
output = 'weather.zip'

print("Downloading dataset")
gdown.download(url, output, quiet=False)

print("Extracting dataset")
  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import zipfile
import os

import pickle
print("Starting the model training")
with zipfile.ZipFile(output, 'r') as zip:
    zip.extractall('weather_data')
print("Extracted the weather data from zip file.")

df = pd.read_csv("weather_data/weather_data.csv")
print(df.head())
df['dt_txt'] = pd.to_datetime(df['dt_txt'])
df['DayofYear']  = df['dt_txt'].dt.dayofyear
df['month']=df['dt_txt'].dt.month
df['Hour'] = df['dt_txt'].dt.hour

le = LabelEncoder()
df['city_name_encoded'] = le.fit_transform(df['city_name'])

with open('city_encoder.pkl', 'wb') as f:
     pickle.dump(le, f)

feature_cols = ['DayofYear', 'month', 'Hour', 'city_name_encoded']

X = df[feature_cols]
y = df['temp']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mean = mean_squared_error(y_test, y_pred)
print(mean)
with open('temp_model.pkl', 'wb') as f:
    pickle.dump(model, f)