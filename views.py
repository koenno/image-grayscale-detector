import os
from flask import Flask,request
from flask.json import jsonify
import datetime
from grayscale import detect_grayscale

app = Flask(__name__)

@app.route("/detect-grayscale", methods=[ "POST"])
def predict():
    file = request.files["file"]

    filename = str(datetime.datetime.now())+".jpg"

    input_path = os.path.join("/tmp/", filename)

    file.save(input_path)
    
    result = detect_grayscale(input_path)

    os.remove(input_path)

    return jsonify(result)
