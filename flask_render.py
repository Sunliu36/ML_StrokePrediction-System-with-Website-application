import joblib

import numpy as np
import pandas as pd
from flask import Flask, request, render_template,url_for,redirect
import json as js
app = Flask(__name__)
app.static_folder = 'static'
app.debug = True
answer=""
@app.route("/")
def formPage():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    global answer
    if request.method == 'POST':
        # id=request.form.get('id')
        gender=request.form.get('gender')
        age=request.form.get('age')
        have_hypertension=request.form.get('hypertension')
        have_heartdisease=request.form.get('heart_disease')
        have_married=request.form.get('ever_married')
        work_type=request.form.get('work_type')
        Residence_type=request.form.get('Residence_type')
        avg_glucose_level=request.form.get('avg_glucose_level')
        bmi=request.form.get('bmi')
        smoking_status=request.form.get('smoking_status')
        smoking_status_Unknown = 0
        print(gender,age,have_hypertension,have_heartdisease,have_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status)
        if gender=='Female':
            gender_Female=1
            gedner_Male=0
        elif gender=='Male':
            gedner_Male=1
            gender_Female=0
        if have_married==0:
            married_yes=0
            married_no=1
        else:
            married_no=0
            married_yes=1
        if work_type=='Govt_job':
            Govt_job=1
            never_worked=0
            private=0
            self_employ=0
            children=0
        elif(work_type=='Never_worked'):
            Govt_job=0
            never_worked=1
            private=0
            self_employ=0
            children=0
        elif(work_type=='Private'):
            Govt_job=0
            never_worked=0
            private=1
            self_employ=0
            children=0
        elif(work_type=='Self-employed'):
            Govt_job=0
            never_worked=0
            private=0
            self_employ=1
            children=0
        elif(work_type=='children'):
            Govt_job=0
            never_worked=0
            private=0
            self_employ=0
            children=1
        if Residence_type=='Urban':
            resident_type_urban=1
            resident_type_rural=0
        elif Residence_type=='Rural':
            resident_type_urban=0
            resident_type_rural=1
        if smoking_status=='smokes':
            smoking_status_smoke=1
            smoking_status_never=0
            smoking_status_former=0
        elif smoking_status=='never smoked':
            smoking_status_smoke=0
            smoking_status_never=1
            smoking_status_former=0
        elif smoking_status=='formerly smoked':
            smoking_status_smoke=0
            smoking_status_never=0
            smoking_status_former=1
        
        model = joblib.load('model/EasyEnsembleClassifier')
        print('error')
        X = pd.Series(
            {
                'age':age,
                'hypertension':have_hypertension,
                'heart_disease':have_heartdisease,
                'avg_glucose_level':avg_glucose_level,
                'bmi':bmi,
                'gender_Female':gender_Female,
                'gender_Male':gedner_Male,
                'ever_married_No':married_no,
                'ever_married_Yes':married_yes,
                'work_type_Govt_job':Govt_job, 
                'work_type_Never_worked':never_worked,
                'work_type_Private':private,
                'work_type_Self-employed':self_employ,
                'work_type_children':children,
                'Residence_type_Rural':resident_type_rural,
                'Residence_type_Urban':resident_type_urban,
                'smoking_status_Unknown':smoking_status_Unknown,
                'smoking_status_formerly smoked':smoking_status_former,
                'smoking_status_never smoked':smoking_status_never,
                'smoking_status_smokes':smoking_status_smoke
            }
        )
        print(X)
        print('erro2')
        pred = model.predict([X])[0]
        prod_prob = model.predict([X])[0]
        print('ddd')
        print(pred)
        if pred:# stroke
            prediction = '您很有可能中風，請至醫院進行健康檢查'
        else:
            prediction = 'No stroke'
        # prediction = model.predict([[
        #     age,
        #     have_hypertension,
        #     have_heartdisease,
        #     avg_glucose_level,
        #     bmi, 
        #     gender_Female,
        #     gedner_Male,
        #     married_no,
        #     married_yes,
        #     Govt_job,
        #     never_worked,
            
        # ]])
        answer=prediction
        print(prediction)
        return answer

if __name__ == "__main__":
    app.run()
    