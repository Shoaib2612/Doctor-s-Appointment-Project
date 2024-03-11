from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'khansofiakhan03@gmail.com'  
app.config['MAIL_PASSWORD'] = 'itistrue'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
users = [{'name':'Afeera','email':'afeeraarfain3099@gmail.com'},
{'name':'Syeda','email':'syedaafeera105@gmail.com'}]  
  
mail = Mail(app)  
 
@app.route("/")  
def index():  
    with mail.connect() as con:  
        for user in users:  
            message = "hello %s" %user['name']  
            msgs = Message(recipients=[user['email']],body = message, subject = 'hello', sender = 'shoaibkhan6993@gmail.com')  
            con.send(msgs)  
    return " Message Sent"  
if __name__ == "__main__":  
    app.run(debug = True)
