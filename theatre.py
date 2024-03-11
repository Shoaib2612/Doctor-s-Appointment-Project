from flask import *
from cacon import cassandra_connect
app = Flask(__name__)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=="GET":
        return render_template("theatre.html")
    else:
        tid=int(request.form[ 'tid'])
        nos=int(request.form[ 'nos'])
        seats=request.form[ 'seats']
        year=int(request.form[ 'year'])
        session=cassandra_connect()
        session.execute('USE "Movie"')
        session.execute(
    """
    INSERT INTO theatre (tid,nos,seats_type,year)
    VALUES(%(tid)s, %(nos)s, %(seats_type)s, %(year)s)
    """,
    {'tid':tid, 'nos':nos, 'seats_type':seats,'year':year}
    )
    return "inserted.."


@app.route('/update', methods=['GET','POST'])
def update():
    if request.method=="GET":
        return render_template("theatreup.html")
    else:
        tid=int(request.form[ 'tid'])
        nos=int(request.form[ 'nos'])
        seats=request.form[ 'seats']
        year=int(request.form[ 'year'])
        session=cassandra_connect()
        session.execute('USE "Movie"')
        session.execute(
    """
    UPDATE theatre set nos=%(nos)s,seats_type=%(seats_type)s,year=%(year)s where tid=%(tid)s
    """,
    {'tid':tid, 'nos':nos, 'seats_type':seats,'year':year}
    )   
    return "Updated Succesfully" 

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method=="GET":
        return render_template("theatredel.html")    
    else:
        tid=int(request.form[ 'tid'])
        session=cassandra_connect()
        session.execute('USE "Movie"')
        session.execute(
    """
    DELETE from theatre where tid=%(tid)s

    """,
    {'tid':tid}  
    ) 
    return "Deleted"

@app.route('/display', methods=['GET'])   
def display():
    session=cassandra_connect()
    session.execute('USE "Movie"')
    rows = session.execute('SELECT tid,nos,seats_type,year FROM theatre')
    r=[]
    for theatre_row in rows:
        r.append([theatre_row.tid,theatre_row.nos,theatre_row.seats_type,theatre_row.year])
    r=tuple(r)
    return render_template('disp.html',r=r) 

if __name__ == "__main__":
    app.run(debug=True)    
    