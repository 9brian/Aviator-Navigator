# importing Flask and other modules
from flask import Flask, request, render_template 
from flask_bootstrap import Bootstrap5 

# Flask constructor
app = Flask(__name__)
bootstrap = Bootstrap5(app)  
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def home():
    return render_template("form.html")


# Page 2
@app.route('/how-it-works', methods = ["GET", "POST"])
def page2func():
  return render_template('page2.html')


@app.route('/experience', methods = ["GET", "POST"])
def page3func():
  if request.method == "POST":
    # getting input with name = fname in HTML form
    city_name = request.form.get("cityname")
    # getting input with name = lname in HTML form 
    state_name = request.form.get("statename") 
    return render_template('page4.html', cn=city_name, sn=state_name)
  return render_template('page3.html')


@app.route('/e', methods = ["GET", "POST"])
def page4func():
   
   return render_template('page4.html')

  
if __name__=='__main__':
   app.run()