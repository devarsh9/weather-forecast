# -*- coding: utf-8 -*-
"""Prophet_TimeSeries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZMwPn3nMyZIWcdmHYZKw_J0cvtsZA2Ll
"""

import pandas as pd
from fbprophet import Prophet


Data = pd.read_csv("C:/Users/udit/Desktop/SGP_PROPHET/ahmedabad.csv") 

print(Data.head())

"""## ***Calulating Maximum Temperature prediction of a day***"""

df = Data[['date_time','tempC']]
print(df.head())

df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], format='%m/%d/%Y')

df = df.rename(columns = {"date_time": "ds", "tempC": "y"})




# instantiate model
m = Prophet(daily_seasonality=True)
# fit model to data
m.fit(df)

# make a forecast dataframe 
future = m.make_future_dataframe(periods = 365)
# make a forecast
forecast = m.predict(future)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

df1 = pd.DataFrame(forecast)
df2 = df1[['ds','yhat']]
df2['ds'] = df2['ds'].astype(str)


# date = input("The data you want to forecast for : ")
# for i in range(len(df2)):
#     if(date == df2['ds'][i]):
#         print(df2['yhat'][i])

"""## ***Now Calculating Minimum Temperature Prediction of a day***"""

df_min = Data[['date_time','mintempC']]
df_min[df_min.columns[0]] = pd.to_datetime(df_min[df_min.columns[0]], format='%m/%d/%Y')
df_min = df_min.rename(columns = {"date_time": "ds", "mintempC": "y"})

print(df_min.head())


# instantiate model
min = Prophet(daily_seasonality=True)
# min = Prophet()
# fit model to data
min.fit(df_min)

# make a forecast dataframe 
future = min.make_future_dataframe(periods = 365)
# make a forecast
forecast_min = min.predict(future)

print(forecast_min[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

df1_min = pd.DataFrame(forecast_min)
df2_min = df1_min[['ds','yhat']]
df2_min['ds'] = df2_min['ds'].astype(str)

import pickle
pickle.dump(m, open('forecast_model_maxT.pkl','wb'))
pickle.dump(min, open('forecast_model_minT.pkl','wb'))
# with open('forecast_model_maxT.pkl', 'wb') as fout:
#     pickle.dump(m, fout)
# with open('forecast_model_minT.pkl', 'wb') as fout_min:
#     pickle.dump(min,fout_min)
# date = input("The data you want to forecast for : ")
# for i in range(len(df2_min)):
#     if(date == df2_min['ds'][i]):
#         print(df2_min['yhat'][i])

"""## ***Predicting Both***"""

date = input("The data you want to forecast for : ")
for i in range(len(df2)):
    if(date == df2['ds'][i]):
        print("Min Temperature : " + str(df2_min['yhat'][i]))
        print("Max Temperature : " + str(df2['yhat'][i]))




# fig1 = m.plot(forecast)
# fig2 = min.plot(forecast_min)

# fig3 = m.plot_components(forecast)

# fig4 = min.plot_components(forecast_min)