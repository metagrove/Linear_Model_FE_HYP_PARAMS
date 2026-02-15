import pickle
from flask import Flask, request,jsonify,render_template
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

#import ridge regress and standard scaler
ridge_model = pickle.load(open("Models/ridge.pkl","rb"))
scaler = pickle.load(open("Models/scaler.pkl","rb"))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict_data',methods=["GET","POST"])
def predict_data():
    if request.method == "POST":
        try:
            # get form values
            Temperature = float(request.form.get("Temperature"))
            RH = float(request.form.get("RH"))
            WS = float(request.form.get("WS"))
            RAIN = float(request.form.get("RAIN"))
            FFMC = float(request.form.get("FFMC"))
            DMC = float(request.form.get("DMC"))
            ISI = float(request.form.get("ISI"))
            CLASS = float(request.form.get("CLASS"))
            REGION = float(request.form.get("REGION"))

            # make input array
            data = [[Temperature, RH, WS, RAIN, FFMC, DMC, ISI, CLASS, REGION]]

            scaled_data = scaler.transform(data)

            # prediction
            prediction = ridge_model.predict(scaled_data)

            # send result to HTML
            return render_template("home.html", result=prediction)

        except Exception as e:
            return f"Error: {e}"

    else:
        return render_template("home.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)