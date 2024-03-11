from flask import *
from cacon import cassandra_connect
app = Flask(__name__)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=="GET":
        return render_template("corona.html")
    else:
        id=int(request.form[ 'id'])
        district=request.form[ 'district']
        active=int(request.form[ 'active'])
        recovered=int(request.form[ 'recovered'])
        deaths=int(request.form[ 'deaths'])
        session=cassandra_connect()
        session.execute('USE corona')
        session.execute(
    """
    INSERT INTO corona (id,district,active,recovered,deaths)
    VALUES(%(id)s, %(district)s, %(active)s, %(recovered)s, %(deaths)s)
    """,
    {'id':id, 'district':district, 'active':active,'recovered':recovered, 'deaths':deaths}
    )
    return "<h2>Inserted..</h2>"

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method=="GET":
        return render_template("coronaup.html")
    else:
        id=int(request.form[ 'id'])
        district=request.form[ 'district']
        active=int(request.form[ 'active'])
        recovered=int(request.form[ 'recovered'])
        deaths=int(request.form[ 'deaths'])
        session=cassandra_connect()
        session.execute('USE corona')
        
        session.execute(
    """
    UPDATE corona set district=%(district)s,active=%(active)s,recovered=%(recovered)s,deaths=%(deaths)s where id=%(id)s
    """,
    {'id':id, 'district':district, 'active':active,'recovered':recovered, 'deaths':deaths}
    )   
    return "Updated Succesfully" 

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method=="GET":
        return render_template("coronadel.html")    
    else:
        id=int(request.form[ 'id'])
        session=cassandra_connect()
        session.execute('USE corona')
        session.execute(
    """
    DELETE from corona where id=%(id)s

    """,
    {'id':id}  
    ) 
    return "Deleted"
@app.route('/display', methods=['GET'])   
def display():
    session=cassandra_connect()
    session.execute('USE corona')
    rows = session.execute('SELECT id,district,active,recovered,deaths FROM corona')
    r=[]
    for corona_row in rows:
        r.append([corona_row.id,corona_row.district,corona_row.active,corona_row.recovered,corona_row.deaths])
    r=tuple(r)
    return render_template('coronadisp.html',r=r) 

@app.route('/threshold', methods=['GET'])   
def threshold():
    session=cassandra_connect()
    session.execute('USE corona')
    rows = session.execute('SELECT id,district,active,recovered,deaths FROM corona')
    r=[]
    for corona_row in rows:
        if (corona_row.active > 35000 or corona_row.recovered < 12000):   
            r.append([corona_row.id,corona_row.district,corona_row.active,corona_row.recovered,corona_row.deaths])
    r=tuple(r)
    return render_template('coronadisp.html',r=r) 


if __name__ == "__main__":
    app.run(debug=True)    
    