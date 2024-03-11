from flask import *  
app = Flask(__name__)
@app.route('/jnnce/examfees')  
def examfees():  
   return render_template('examfees.html')  
@app.route('/status',methods = ['POST', 'GET'])  
def res(): 
    if request.method == 'POST': 
      result = request.form     
      return render_template("result.html",result = result)  

@app.route('/jnnce/canteen')  
def canteenform():  
   return render_template('canteen_form.html')  
@app.route('/orderdetail',methods = ['POST', 'GET'])  
def detail():
    if request.method == 'POST':
      result = request.form     
      return render_template("order_detail.html",result = result)     
if __name__ == '__main__':  
   app.run(debug = True)    