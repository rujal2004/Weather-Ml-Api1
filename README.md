## ThermoMatch 
This is a full-stack machine learning project that predicts temperature using a Linear Regression model trained on a Kaggle weather dataset. It compares the model’s output with live data from a real weather API and shows the difference via a clean web interface.
**Live Demo :** https://weather-ml-api1.onrender.com/
## Features
Predicts weather using trained ML model.

Build a custom API using Flask to serve predicted temperature data.

Fetches real-time weather from API(OpenWeatherMap).

Compares predicted and real temperatures, and shows the difference.

Flask API and basic frontend interface.

## Tech Stack
**Frontend:** HTML

**Backend:** Flask(Python)

**Machine Learning:** scikit-learn, pandas

**APIs Used:**

  **Custom Flask API** (to serve predicted temperature)
  
  **OpenWeatherMap API** (for real-time weather)

## Installation
  ### 1. Clone the Repository
        ```bash
      git clone https://github.com/rujal2004/Weather-Ml-Api1.git
      cd Weather-Ml-Api1
  ### 2. Create and Activate Virtual Environment
         python -m venv venv
         venv\Scripts\activate
  ### 3. Install Dependencies
         pip install -r requirements.txt
  ### 4. Run the Application
         python app.py
   

## Future Improvements
  Train the model using more advanced algorithms like **Random Forest** for better   accuracy.
  
  Add chart-based visualization (matplotlib/Plotly).
  
  Include error metrics (MAE, RMSE).
  
  Predict more weather metrics (humidity, wind speed, etc.).

## Author
  Rujal Gupta

 

  
  

