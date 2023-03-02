# Import Statements
import os
# print('Installing Packages')
# os.system('pip install -r requirements.txt')

import json
from flask import Flask, render_template, request, jsonify,redirect, url_for
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

'''
This function handles the POST request to the /upload endpoint 
and reads the contents of the uploaded file using Flask's request.files object
'''

@app.route("/upload", methods=['POST'])
def upload_file():
    file = request.files["file"]
    content = file.read()
    content = content.decode('utf-8')
    print(f'Content type = {type(content)}')

    # Call simple algorithm - Harry and Trevor
    
    
    json_returned = {'status':'success','content':content}

    # Writing to a stdout file
    with open('output_file.txt', 'wb') as output_file:
        # Write the contents of the input file to the new file
        output_file.write(content.encode('utf-8'))
    
    print("Flushed output to 'output_file.txt' file")
    return json_returned

# @app.route("/results")
# def results():
#     # retrieve the results from the query parameters
#     results = json.loads(request.args.get('data'))
#     # render the "results.html" template with the results as context
#     return render_template("results.html", results=results)

if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)

    port = config["port"]
    print(f'App running on port {port}')
    app.run(host='localhost', port=port)
    