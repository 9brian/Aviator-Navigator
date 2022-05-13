# export FLASK_APP=project.py
# export FLASK_DEBUG=1
# flask run
"""
Name: Brian Palomar
Teammates: Nick Mederos, Vicente Valencia & team number 7327 
CST205-01_SP22: Multimedia Design & Progmng
"""
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Home Page
@app.route('/')
def home():
  return render_template('index.html')

# Page 2
@app.route('/about')
def page2func():
  return render_template('page2.html')
