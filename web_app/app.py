#!/usr/bin/env python
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, Markup, send_file
import pickle
 
app = Flask(__name__)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/text', methods = ['POST', 'GET'])
def writeText():
    return render_template('input.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    return render_template('result.html')

@app.route('/api/images', methods=['GET', 'POST'])
def images():
     if request.method == 'GET':
        filename = request.args.get('filename')
        print(filename)
        return send_file('images/'+filename, mimetype='image/gif') 

# when running app locally
if __name__=='__main__':
      app.run(debug=True)