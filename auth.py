from flask import *  
app = Flask(__name__)  
 
 
 
@app.route('/login')  
def login():  
    return render_template("alogin.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        return redirect(url_for("success"))  
    else:  
        abort(404)  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True) 