
"""
Created on Thu Nov 17 15:13:35 2022

@author: MuthuMurali
"""

from flask import Flask,render_template,request,url_for,redirect
import ibm_db2
import mail
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')      # register - regsitration page

# admin credentials
@app.route('/register')
def register():
    return render_template('register.html')
  
@app.route('/adminregister')
def adminregister():
    return render_template('adminregister.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/adminlogin')
def adminlogin():
  return render_template('adminlogin.html')   # admin log in page

@app.route('/adminreg')
def adminreg():
  return render_template('adminreg.html')  # admin sign up page
@app.route('/donor')
def donor():
  return render_template('donor.html')
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/recipregistration')
def recipregistration():
  return render_template('recipregistration.html')   ## recipient signup page uh
@app.route('/success')
def success():
  return render_template('success.html')
@app.route('/success2')
def success2():
  return render_template('success2.html')
@app.route('/recipientlogin')
def recipientlogin():
  return render_template('reclogin.html')  
@app.route('/recipient')
def recipient():
  return render_template('recipient.html')
@app.route('/donregistration')
def donregistration():
  return render_template('donregistration.html')   ## donar signup page uh


@app.route('/donarlogin')
def donarlogin():
  return render_template('donlogin.html') 

if __name__ == "__main__":
    app.run(host='0.0.0.0')