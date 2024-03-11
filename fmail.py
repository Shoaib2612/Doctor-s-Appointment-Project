from flask import *  
from flask_mail import *  
 
app = Flask(__name__)  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'khansofiakhan03@gmail.com'  
app.config['MAIL_PASSWORD'] = 'itistrue'  
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True  
 
mail = Mail(app)
@app.route('/')  
def index():  
    msg = Message('subject', sender = 'shoaibkhan6993@gmail.com', recipients=['afeeraarfain3099@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    mail.send(msg)  
    return "Mail Sent, Please check the mail id" 
 
if __name__ == '__main__':  
    app.run(debug = True)  
 
