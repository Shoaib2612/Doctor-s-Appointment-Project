import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
import requests
 
app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'crops',
#     'host': 'localhost',
#     'port': 27017
# }

DB_URI = "mongodb+srv://flaskmongo:realisrare@cluster0.ddmot.mongodb.net/crops?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI


db = MongoEngine()
db.init_app(app)
 
class Crop(db.Document):
    crop_name = db.StringField()
    soil_type = db.StringField()
    area=db.IntField()
    def to_json(self):
        return {"crop_name": self.crop_name,
                "soil_type": self.soil_type,
                "area":self.area}
 
@app.route('/', methods=['GET'])
def query_records():
    crop_name = request.args.get('crop_name')
    c = Crop.objects(crop_name=crop_name)
    if not c:
        return jsonify('data not found')
    else:
        return jsonify(c.to_json())
 
@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    c = Crop(crop_name=record['crop_name'],
                soil_type=record['soil_type'],
                area=record['area'])
    c.save()
    return jsonify(c.to_json())
 
@app.route('/', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    c = Crop.objects(crop_name=record['crop_name']).first()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        c.update(soil_type=record['soil_type'])
        c.update(area=record['area'])
        return jsonify(c.to_json())
 
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    c = Crop.objects(crop_name=record['crop_name']).first()
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        c.delete()
        return jsonify(c.to_json())

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=="GET":
        return render_template("add.html")
    else:
        x={
        "crop_name":request.form['crop_name'],
        "soil_type":request.form['soil_type'],
        "area":int(request.form['area'])
        }
        x=json.dumps(x)
        response = requests.post(url="http://127.0.0.1:5000/",data=x)
        return response.text

@app.route('/find',methods=['GET','POST'])
def find():
    if request.method=="GET":
        return render_template("find.html")
    else:
        crop_name=request.form['crop_name']
        response = requests.get(url="http://127.0.0.1:5000/",params={"crop_name":crop_name})
        return response.json()
 
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=="GET":
        return render_template("del.html")
    else:
        x={
        "crop_name":request.form['crop_name'],
        
        }
        x=json.dumps(x)
        response = requests.delete(url="http://127.0.0.1:5000/",data=x)
        return response.text


@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=="GET":
        return render_template("update.html")
    else:
        x={
        "crop_name":request.form['crop_name'],
        "soil_type":request.form['soil_type'],
        "area":int(request.form['area'])
        }
        x=json.dumps(x)
        response = requests.put(url="http://127.0.0.1:5000/",data=x)
        return response.text

 
if __name__ == "__main__":
    app.run(debug=True)

