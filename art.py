from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pymysql
app = Flask(__name__,static_folder="static", static_url_path="")

@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/submit', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':

      req = request.form
      print(req)

      name = req['name']
      email = req['email']
      technique = req['technique']
      size = req['size']
      notes = req['notes']

      if request.files:
         reference = request.files["image"]
         print(reference)
      else:
         pass

      return render_template('result.html', result=req)
   return render_template('homepage.html')


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)