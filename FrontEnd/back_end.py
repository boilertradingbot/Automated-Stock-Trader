# Import Statements
import os
import sys
import time
from trendFollowing import *

import json
from flask import Flask, render_template, request, jsonify,redirect, url_for, send_file
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

'''
This function handles the POST request to the /upload endpoint 
and reads the contents of the uploaded file using Flask's request.files object
'''
# @app.route("/select",methods=['GET','POST'])
# def display():
#     return send_file('static/res.html')

@app.route("/", methods=["GET", "POST"])
def home():
    return send_file('static/display.html')

@app.route("/upload", methods=['POST'])
def upload_file():
    print("Recieved")
    selected_strings = request.form.getlist('strings[]')
    if len(selected_strings) == 0:
        return {'status': 'failure'}

    print(f'Selected Strings: {selected_strings}')

    # Call simple algorithm - Read jsons
    start_time = time.time()

    print("Shifting Directories")
    # os.chdir('../Backend')
    JsonList = main_trendFollowing(selected_strings)
    json_returned = {'status':'success', 'JsonList': JsonList}
    # os.chdir('../FrontEnd')
    # Writing to a stdout file
    # with open('output_file.txt', 'wb') as output_file:
    #     # Write the contents of the input file to the new file
    #     output_file.write(content.encode('utf-8'))

    # print("Flushed output to 'output_file.txt' file")
    return json_returned


'''@app.route("/upload", methods=['POST'])
def upload_file():
    selected_strings = request.form.getlist('strings[]')
    if len(selected_strings) == 0:
        return {'status': 'failure'}

    print(f'Selected Strings: {selected_strings}')

    JsonList = []

    for json_obj in runAlgorithm(selected_strings):
        JsonList = [json.dumps(json_obj)]
        print(JsonList)
        #yield json.dumps(JsonList)
    json_returned = {'status':'success', 'JsonList': JsonList}
    return json_returned'''

'''@app.route("/upload", methods=['POST'])
def upload_file():
    selected_strings = request.form.getlist('strings[]')
    if len(selected_strings) == 0:
        return {'status': 'failure'}

    print(f'Selected Strings: {selected_strings}')

    def generate_json():
        for json_obj in runAlgorithm(selected_strings):
            yield json.dumps(json_obj)
            #yield "\n"
    return Response(generate_json(), mimetype='text/json')'''

'''@app.route("/upload", methods=['POST'])
def upload_file():
    selected_strings = request.form.getlist('strings[]')
    if len(selected_strings) == 0:
        return {'status': 'failure'}

    print(f'Selected Strings: {selected_strings}')

    JsonList = []

    algorithm = runAlgorithm(selected_strings)

    try:
        while True:
            json_obj = next(algorithm)
            JsonList.append(json_obj)
            print(JsonList)
            return json.dumps(json_obj)
    except StopIteration:
        pass

    json_returned = {'status':'success', 'JsonList': JsonList}
    return json.dumps(json_returned)'''

'''@app.route("/upload", methods=['POST'])
def upload_file():
    selected_strings = request.form.getlist('strings[]')
    if len(selected_strings) == 0:
        return {'status': 'failure'}
    def generate_response():
        for stockJson in runAlgorithm(selected_strings):
            print(stockJson)
            yield stockJson
            time.sleep(5)
    
    return Response(generate_response(), mimetype='application/json')'''


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)

    port = config["port"]
    print(f'App running on port {port}')
    app.run(host='0.0.0.0', port=port)
    