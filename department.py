from flask import *  
app = Flask(__name__)
@app.route('/jnnce/depts')  
def departments():  
   return render_template('dept.html') 
@app.route('/cs')  
def cs():  
    return '<h1 style=color:blue>Welcome to Computer science Department<h1>'

@app.route('/cv') 
def cv():  
    return '<h1 style=color:blue>Welcome to Civil  Department<h1>'  
@app.route('/ee')     
def ee():  
    return '<h1 style=color:blue>Welcome to Electronics and Electrical Department<h1>' 
@app.route('/ec')      
def ec():  
    return '<h1 style=color:blue>Welcome to Electronics and Communication Department<h1>'  
@app.route('/ise')     
def ise():  
    return '<h1 style=color:blue>Welcome to Information Science Department<h1>'
@app.route('/m')       
def m():  
    return '<h1 style=color:blue>Welcome to Mechanical Department<h1>'                                
if __name__ == '__main__':  
   app.run(debug = True)    