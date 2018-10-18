
from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json
import pandas as pd
# load the built-in model 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/getdelay', methods=['POST','GET'])
def get_delay():
    result=request.form
    Age=result['Age']
    Experience=result['Experience']
    Income=result['Income']
    CCAvg=result['CCAvg']
    Mortgage=result['Mortgage']
    Family_2=result['Family_2']
    Family_3=result['Family_3']
    Family_4=result['Family_4']
    Education_2=result['Education_2']
    Education_3=result['Education_3']
    CDAccount_1=result['CDAccount_1']
    CCAvg_Income_ratio=result['CCAvg_Income_ratio']
    
    user_input={'Age':Age,'Experience':Experience,'Income':Income,'CCAvg':CCAvg,'Mortgage':Mortgage,'Family_2':Family_2,'Family_3':Family_3,'Family_4':Family_4,'Education_2':Education_2,'Education_3':Education_3,'CDAccount_1':CDAccount_1,'CCAvg_Income_ratio':CCAvg_Income_ratio}
    Log_model = joblib.load('Log.pkl')
    df=pd.DataFrame(data=user_input,index=[0])
    prediction=Log_model.predict(df)
    if prediction ==1:
       return render_template('result.html')
    if prediction ==0:
       return render_template('result2.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)