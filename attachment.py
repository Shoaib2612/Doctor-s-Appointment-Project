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
 
@app.route("/")  
def index():  
    msg = Message(subject = "hello", body = "Hi there!", sender = "khansofiakhan03@gmail.com", recipients = ["afeeraarfain3099@gmail.com"])  
    with app.open_resource("img1.jpeg") as fp:  
        msg.attach("img1.jpeg","image/jpeg",fp.read())  
        mail.send(msg)  
    return "sent"  
  
if __name__ == "__main__":  
    app.run(debug = True)  
