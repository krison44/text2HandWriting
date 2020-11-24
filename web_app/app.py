#!/usr/bin/env python
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, Markup, send_file
import argparse
import os
import pickle
import matplotlib
import tensorflow as tf
import generate
 
app = Flask(__name__)


 
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/api/userText', methods = ['POST', 'GET'])
def writeText():
    if request.method == 'POST':
        data = request.get_json()
        text = data['userText']
        print(text)
        parser = argparse.ArgumentParser()
        parser.add_argument('--model', dest='model_path', type=str, default=os.path.join('pretrained', 'model-29'),
                            help='(optional) DL model to use')
        parser.add_argument('--text', dest='text', type=str, help='Text to write')
        parser.add_argument('--text-file', dest='file', type=str, default=None, help='Path to the input text file')
        parser.add_argument('--style', dest='style', type=int, default=0, help='Style of handwriting (1 to 7)')
        parser.add_argument('--bias', dest='bias', type=float, default=0.9,
                            help='Bias in handwriting. More bias is more unclear handwriting (0.00 to 1.00)')
        parser.add_argument('--force', dest='force', action='store_true', default=False)
        parser.add_argument('--color', dest='color_text', type=str, default='0,0,150',
                            help='Color of handwriting in RGB format')
        parser.add_argument('--output', dest='output', type=str, default='./handwritten.pdf',
                            help='Output PDF file path and name')
        args = parser.parse_args()

        if text is not None:
            if len(text) > 50:
                pass
            else:
                print("Text too short!")
                exit()
        else:
            print("Please provide either --text or --text-file in arguments")
            exit()
        matplotlib.use('agg')
        with open(os.path.join('data', 'translation.pkl'), 'rb') as file:
            translation = pickle.load(file)
        rev_translation = {v: k for k, v in translation.items()}
        charset = [rev_translation[i] for i in range(len(rev_translation))]
        charset[0] = ''

        config = tf.compat.v1.ConfigProto(
            device_count={'GPU': 0}
        )

        with tf.compat.v1.Session(config=config) as sess:
            saver = tf.compat.v1.train.import_meta_graph(args.model_path + '.meta')
            saver.restore(sess, args.model_path)

            print("\n\nInitialization Complete!\n\n\n\n")

            color = [int(i) for i in args.color_text.replace(' ', '').split(',')]
            pdf = generate.generate(text.replace('1', 'I'), args, sess, translation, color[:3])
        return jsonify(success=True)
    else:
        return {'test': 'test'}

@app.route('/text', methods = ['POST', 'GET'])
def text():
    return render_template('input.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    return render_template('result.html')

@app.route('/api/url', methods=['GET', 'POST'])
def url():
    if request.method == 'GET':
        return send_file('./pages/page1.png')

# when running app locally
if __name__=='__main__':
      app.run(debug=True)