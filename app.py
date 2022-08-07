# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:03:03 2022

"""
import webbrowser as wb
from flask import Flask, render_template, jsonify, request
from pred_test import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/sentanalysis')
def sentanalysis():
   input_text = request.args.get('input_text', '0', type=str)
   
   if len(input_text) == 0 or input_text=='':
      return jsonify({"error_input":"..    No tweet supplied"})
   else:
       with warnings.catch_warnings():           
           warnings.simplefilter("ignore")
           res = predict(input_text)
           return jsonify({'result':res})


if __name__ == "__main__":
    #wb.open_new_tab('http://localhost:1000/search')
    app.run(debug=True)
    
    #app.run(host='0.0.0.0')
