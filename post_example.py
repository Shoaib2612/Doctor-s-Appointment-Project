from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['GET','POST'])  
def login(): 
    if request.method=="POST": 
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="abc" and passwrd=="xyz":  
           return render_template("welcome.html",user=uname)

      else:
          return "<h1 style=color:red>Invalid user</h1>"
    else:
        return render_template("login.html") 
 
   
if __name__ == '__main__':  
   app.run(debug = True)  
 
 
