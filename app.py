from flask import Flask, request,render_template, jsonify
import  pickle
import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)
import requests
from datetime import datetime

API_KEY = "a641892d56a4a927c1e0628d3305b09b"


with open('temp_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('city_encoder.pkl', 'rb') as f:
    city_encoder = pickle.load(f)

    
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods = ['GET','POST'])
def predict():
   if request.form:
     city_name = request.form.get('city_name')
     now = datetime.now()
     dayofyear = now.timetuple().tm_yday
     month = now.month
     hour = now.hour

   else:
        data = request.get_json()
        city_name = data.get('city_name')
        dayofyear = data.get('DayofYear')
        month = data.get('month')
        hour = data.get('Hour')
   
   city_encoded = city_encoder.transform([city_name])[0]
   
   input_df = pd.DataFrame([{
        'DayofYear': dayofyear,
        'month': month,
        'Hour': hour,
        'city_name_encoded': city_encoded
    }])
   prediction = model.predict(input_df)[0]
   '''if request.form:
       return f"<h2>Predicted Temperature: {prediction:.2f} °C</h2>"
   else:
       return jsonify({
       'predicted_temp': prediction[0]
   })'''
   
   url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
   response = requests.get(url)
   if response.status_code == 200:
        real_temp=  response.json()['main']['temp']
   else:
        print("Real API Error:", response.json())
        return None
   
   difference = round(abs(real_temp - prediction))
 
   return render_template('result.html',
                           city=city_name,
                           predicted=prediction,
                           real=real_temp,difference=difference)
if __name__ == '__main__':
    app.run(debug=True)