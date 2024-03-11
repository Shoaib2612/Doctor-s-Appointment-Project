from flask  import Flask,redirect,url_for

app = Flask(__name__)
@app.route('/home/<name>')
def home(name):
    return "hello, "+name+" this is our first flask website..Thank you"
@app.route('/emp/<int:age>')
def emp(age):
    return"Age = %d"%age;  
def about():  
    return "This is about page";  
app.add_url_rule("/about","about",about)
@app.route('/hod')  
def hod():  
    return 'HOD'  
  
@app.route('/principal')  
def principal():  
    return 'Principal'  
  
@app.route('/student')
def student():  
    return 'student' 
 
@app.route('/user/<name>')  
def user(name):  
    if name == 'HOD':  
        return redirect(url_for('hod'))  
    if name == 'Principal':  
        return redirect(url_for('principal'))  
    if name == 'student':  
        return redirect(url_for('student'))   
if __name__=='__main__':
    app.run(debug=True)