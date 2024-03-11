from flask import *  
from flask_mail import *
app = Flask(__name__) 
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'khansofiakhan03@gmail.com'  
app.config['MAIL_PASSWORD'] = 'itistrue'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
mail = Mail(app)   
 
@app.route('/')  
def upload():  
    return render_template("indexform.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        email = request.form["email"]  
        msg = Message(subject = "hello", body = "Hi there!", sender = "khansofiakhan03@gmail.com", recipients = [email])  
        with app.open_resource(f.filename) as fp:  
            msg.attach(f.filename,"image/jpeg",fp.read())  
            mail.send(msg)
        return render_template("fstatus.html", name = f.filename)  
 
if __name__ == "__main__":  
    app.run(debug = True)    