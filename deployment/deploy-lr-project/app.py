
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Age = int(request.form['Age'])
    Sex = request.form['Sex']
    ChestPainType = request.form['ChestPainType']
    RestingBP = int(request.form['RestingBP'])
    Cholesterol = int(request.form['Cholesterol'])
    FastingBS = int(request.form['FastingBS'])
    RestingECG = request.form['RestingECG']
    MaxHR = int(request.form['MaxHR'])
    ExerciseAngina = request.form['ExerciseAngina']
    Oldpeak = int(request.form['Oldpeak'])
    ST_Slope =request.form['ST_Slope']
    
    #final_features = [Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]
    column_names=['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']
    final_features=pd.DataFrame({
    "Age": [Age],
    "Sex": [Sex],
    "ChestPainType": [ChestPainType],
    "RestingBP": [RestingBP],
    "Cholesterol": [Cholesterol],
    "FastingBS": [FastingBS],
    "RestingECG": [RestingECG],
    "MaxHR": [MaxHR],
    "ExerciseAngina": [ExerciseAngina],
    "Oldpeak": [Oldpeak],
    "ST_Slope": [ST_Slope]
})
    prediction= model.predict(final_features) 
    if prediction == [0] :
     return render_template('index.html',prediction_text=f'This person is in good health  ${prediction}')
    else :
     return render_template('index.html',prediction_text=f'This person have heart disease with percentage of   ${prediction}')


if __name__ == '__main__':
	app.run(host='0.0.0.0')
