"""
Course: CST205-01_SP22: Multimedia Design & Programming
Title: The Aviator Navigator
Abstract:
Date: May 19, 2022

Team number: 7327 
Teammates: Brian Palomar, Nick Mederos, Vicente Valencia

Brian implemented the api into flask
Nick worked on styling 
Vince debugged and researched workarounds
We all helped setup the basic flask formatting

Link: https://github.com/9brian/CST-205-Project-7327 
"""

# importing Flask and other modules
from flask import Flask, request, render_template 
from flask_bootstrap import Bootstrap5 
import requests, json
from pprint import pprint

# Flask constructor
app = Flask(__name__)
bootstrap = Bootstrap5(app) 

# Helps create url
location = 'marina'

# Function to search user wanted location in api
def api_search(location):
  
  url = f'https://weatherdbi.herokuapp.com/data/weather/{location}'
  endpoint = url
  payload = {
    # 'region' : 'Marina, CA'
  }

  # Requests acess to info
  r = requests.get(endpoint, params=payload)
  # Data variable
  data = r.json()

  # Makes region global
  global region
  # Assigns variables with api data
  region = data['region']
  weatherNow = data['currentConditions']

  # Initalizes empty array
  val_arr = []

  # Appends weather values into array
  for key, value in weatherNow.items():
    if(key != 'iconURL'):
      if(key == 'temp'):    
        val_arr.append(value)
      elif(key == 'wind'):
        val_arr.append(value)
      else:
        val_arr.append(value)
    
  # Variable globalization
  global dot
  global temp_cel
  global temp_far
  global precip
  global humid
  global wind_km
  global wind_mile
  global comment

  # Assigns variables to data wanted
  dot = val_arr[0]
  temp_cel = val_arr[1]['c']
  temp_far = val_arr[1]['f']
  precip = val_arr[2]
  humid = val_arr[3]
  wind_km = val_arr[4]['km']
  wind_mile = val_arr[4]['mile']
  comment = val_arr[5]
  
  # Returning wanted data
  return region, dot, temp_cel, temp_far, precip, humid, wind_km, wind_mile, comment


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])  
def home():
  return render_template("form.html")

# Page 2
@app.route('/how-it-works')
def page2func():
  return render_template('page2.html')

# Page 3
@app.route('/experience', methods = ["GET","POST"])
def page3func():
  if request.method == "POST":
    city_name = request.form.get("cityname")
    # state_name = request.form.get("statename") 
    location = city_name

    api_search(location)

    return render_template('page4.html', cn=city_name, location=location,
    region=region, dot=dot, cel=temp_cel, far=temp_far, precip=precip, 
    humid=humid, wind_km=wind_km, wind_mile=wind_mile,
    comment=comment)
  return render_template('page3.html')

# Page 4
@app.route('/results', methods = ["GET", "POST"])
def page4func():
  return render_template('page4.html', region=region,
  dot=dot, cel=temp_cel, far=temp_far, precip=precip, 
  humid=humid, wind_km=wind_km, wind_mile=wind_mile,
  comment=comment)

# Helps app run
if __name__=='__main__':
  app.run()
