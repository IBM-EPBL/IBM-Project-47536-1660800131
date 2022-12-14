# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:13:35 2022

@author: MuthuMurali
"""

from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')      # index - home page

# admin credentials

@app.route('/login')
def login():
  return render_template('login.html')   # admin log in page

@app.route('/adminreg')
def adminreg():
  return render_template('adminreg.html')  # admin sign up page


@app.route('/recipregistration')
def recipregistration():
  return render_template('recipregistration.html')   ## recipient signup page uh

@app.route('/recipientlogin')
def recipientlogin():
  return render_template('reclogin.html')  

@app.route('/donregistration')
def donregistration():
  return render_template('donregistration.html')   ## donar signup page uh


@app.route('/donarlogin')
def donarlogin():
  return render_template('donlogin.html') 

if __name__ == "__main__":
    app.run(debug=True)