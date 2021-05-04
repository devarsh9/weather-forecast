import pandas as pd
import numpy as np
import pickle
from flask import Flask, jsonify, request ,render_template
# from flask_cors import CORS, cross_origin

#import libraries

#Initialize the flask App
app = Flask(__name__)
# CORS(app)
maxT = pickle.load(open('forecast_model_maxT.pkl', 'rb'))
minT = pickle.load(open('forecast_model_minT.pkl', 'rb'))

print("working")

#default page of our web-app
@app.route('/')
def home():
    print("working good")
    return "<h1>HIIIII</h1>"

@app.route('/predict',methods=['GET'])
def home1():
    maxT = pickle.load(open('forecast_model_maxT.pkl', 'rb'))
    minT = pickle.load(open('forecast_model_minT.pkl', 'rb'))
    d={}
    d['Query'] = str(request.args['Query'])
    print("working good")
    future_max = maxT.make_future_dataframe(periods=365)
    forecast = maxT.predict(future_max)
    df1 = pd.DataFrame(forecast)
    df2 = df1[['ds','yhat']]
    df2['ds'] = df2['ds'].astype(str)
    
    future_min = minT.make_future_dataframe(periods=365)
    forecast_m = minT.predict(future_min)
    df1_m = pd.DataFrame(forecast_m)
    df2_m = df1_m[['ds','yhat']]
    df2_m['ds'] = df2_m['ds'].astype(str)
    for i in range(len(df2)):
     if(d['Query'] == df2['ds'][i]):
        print("Min Temperature : " + str(df2_m['yhat'][i]))
        print("Max Temperature : " + str(df2['yhat'][i]))
        dict={}
        dict['Max_temp']=str(df2['yhat'][i])
        dict['Min_temp']=str(df2_m['yhat'][i])

    return jsonify(dict)

#     return render_template('index.html',prediction_text='Hello')
@app.route('/hi')
def home12():
    print("working good")
    return "HIIII"
@app.route('/trial',methods=['GET'])
def trial():
    d={}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)

if __name__ == "__main__":
    app.run()
