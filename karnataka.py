import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
import requests
 
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'corona',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Karnataka(db.Document):
    ID=db.IntField()
    district = db.StringField()
    active = db.IntField()
    recovered=db.IntField()
    containment_zones=db.IntField()
    death=db.IntField()
    lockdown = db.StringField()
    def to_json(self):
        return {"ID": self.ID,
                "district": self.district,
                "active": self.active,
                "recovered":self.recovered,
                "containment_zones":self.containment_zones,
                "death":self.death,
                "lockdown":self.lockdown}

@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    k = Karnataka(ID=record['ID'],
                district=record['district'],
                active=record['active'],
                recovered=record['recovered'],
                containment_zones=record['containment_zones'],
                death=record['death'],
                lockdown=record['lockdown'])
    k.save()
    return jsonify(k.to_json())

@app.route('/', methods=['GET'])
def query_records():
    ID = int(request.args.get('id'))
    k = Karnataka.objects(ID=ID).first()
    if not k:
        return jsonify('data not found')
    else:
        return jsonify(k.to_json())

@app.route('/listall',methods=['GET'])
def list_all():
    if request.method=="GET":
        k = Karnataka.objects.all()
        string = str()
        for i in range(1,len(k)+1):
            id =i
            response = requests.get(url="http://127.0.0.1:5000/",params={"id":id})
            string = string[:]+'<tr>'
            for j in response.json().values():
                string = string[:]+'<td>'+str(j)+'</td>'
            string = string[:]+'</tr>'
        heading = '<tr><th>ID</th><th>Active</th><th>Containment_Zones</th><th>Deaths</th><th>District</th><th>Lockdown</th><th>Recovered</th></tr>'
        return '<table>'+heading+string+'</table>'




@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=="GET":
        return render_template("post.html")
    else:
        x={
        "ID":int(request.form['ID']),
        "district":request.form['district'],
        "active":int(request.form['active']),
        "recovered":int(request.form['recovered']),
        "containment_zones":int(request.form['containment_zones']),
        "death":int(request.form['death']),
        "lockdown":request.form['lockdown']
        }
        x=json.dumps(x)
        response = requests.post(url="http://127.0.0.1:5000/",data=x)
        return response.text 

@app.route('/', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    k = Karnataka.objects(ID=record['ID']).first()
    if not k:
        return jsonify( 'data not found')
    else:
        k.update(district=record['district'])
        k.update(active=record['active'])
        k.update(recovered=record['recovered'])
        k.update(containment_zones=record['containment_zones'])
        k.update(death=record['death'])
        k.update(lockdown=record['lockdown'])
        return jsonify(k.to_json())

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=="GET":
        return render_template("updatedata.html")
    else:
        x={
        "ID":int(request.form['ID']),
        "district":request.form['district'],
        "active":int(request.form['active']),
        "recovered":int(request.form['recovered']),
        "containment_zones":int(request.form['containment_zones']),
        "death":int(request.form['death']),
        "lockdown":request.form['lockdown']
        }
        x=json.dumps(x)
        response = requests.put(url="http://127.0.0.1:5000/",data=x)
        return response.text

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    k = Karnataka.objects(ID=record['ID']).first()
    if not k:
        return jsonify('data not found')
    else:
        k.delete()
        return jsonify(k.to_json())

@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=="GET":
        return render_template("deldata.html")
    else:
        x={
        "ID":request.form['ID'],
        
        }
        x=json.dumps(x)
        response = requests.delete(url="http://127.0.0.1:5000/",data=x)
        return response.text
    
@app.route('/check',methods=['GET', 'POST'])
def check():
    if request.method=="GET":
        return render_template("check.html")
    else:
        active=int(request.form['active'])
        recovered=int(request.form['recovered'])
        k = Karnataka.objects.all()
        string1 = str()
        string2 = str()
        for i in range(1,len(k)+1):
            id=i
            response = requests.get(url="http://127.0.0.1:5000/",params={"id":id})


            if response.json()['active'] > active:
                    string1 = string1[:]+'<tr>'
                    for j in response.json().values():
                        string1 = string1[:]+'<td>'+str(j)+'</td>'
                    string1 = string1[:]+'</tr>'  

            if response.json()['recovered'] < recovered:
                    string2 = string2[:]+'<tr>'
                    for j in response.json().values():
                        string2 = string2[:]+'<td>'+str(j)+'</td>'
                    string2 = string2[:]+'</tr>' 
        heading = '<tr><th>ID</th><th>Active</th><th>Containment_Zones</th><th>Deaths</th><th>District</th><th>Lockdown</th><th>Recovered</th></tr>'
        if string1=='':
            string1 = 'No records found'
        else:
            string1 = heading+string1[:]
        if string2=='':
            string2 = 'No records found'
        else:
            string2 = heading+string2[:]
        return '<b>List of active cases exceeding threshold </b><table>'+string1+'</table><br><br><br><br><b>List of recovered cases below threshold</b><table>'+string2+'</table><br><br><br><br>'
if __name__ == "__main__":
    app.run(debug=True)        