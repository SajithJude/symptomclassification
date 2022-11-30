from flask import Flask, request, jsonify
import pickle
import pandas as pd

# inisiasi model
app = Flask(__name__)

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model


# Memangil Model Klasifikasi
model_diabetes = open_model("model_logreg.pkl") # Pandas dataframe

# fungsi untuk inference diabetic berupa dataframe
def inference_diabetes(data, model):
    """
    input : list with length : 4 --> [1, 2, 3, 4]/pandas data frame
    output : predicted class (idx, label)
    """
    LABEL = ["Not Diabetes", "Diabetes"]
    columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    data = pd.DataFrame([data], columns=columns)
    res = model.predict(data)
    return res[0], LABEL[res[0]]


# halaman home
@app.route("/")
def homepage():
    return "<h1> Deployment Model Backend! </h1>"

# halaman inference diabetes/data yang dioper ke backend
@app.route('/diabetes_prediction', methods=['POST'])
def diabetes_predict():
    """
    content = 
    {
        'Pregnancies' : xx,
        'Glucose' : xx,
        'BloodPressure' : xx,
        'SkinThickness' : xx,
        'Insulin' : xx,
        'BMI': xx,
        'DiabetesPedigreeFunction' :xx,
        'Age': xx
    }
    """
    content = request.json
    newdata = [
        content['Pregnancies'], #harus berurutan sesuai kolom pada bagian fungsi diatas
        content['Glucose'],
        content['BloodPressure'],
        content['SkinThickness'],
        content['Insulin'], #semua nama kolom harus sesui dengan isi pkl nya
        content['BMI'],
        content['DiabetesPedigreeFunction'],
        content['Age']
               ]
    res_idx, res_label = inference_diabetes(newdata, model_diabetes)
    result = {
        'label_idx': str(res_idx),
        'label_name': res_label
    }
    response = jsonify(success=True,
                       result=result)
    return response, 200

# run app di local
# jika deploy di heroku, comment baris dibawah ini
# app.run(debug=True)
