from flask import *  
from cacon import cassandra_connect
app = Flask(__name__, static_folder="static")  

# <----------------admin login------------->

@app.route('/login',methods = ['GET','POST'])  
def login(): 
    if request.method=="POST": 
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="admin" and passwrd=="afeera123":  
           return render_template("welcome.html")

      else:
          return "<h1 style=color:red>Invalid user name or password</h1>"
    else:
        return render_template("login.html") 



#<---------------user login------------------->

@app.route('/userlogin',methods = ['GET','POST'])  
def userlogin(): 
    if request.method=="POST": 
      uname=request.form['username']  
      password=request.form['pass']
      session=cassandra_connect()
      session.execute('USE "Student" ')
      rows = session.execute('SELECT username,password FROM user')
      for user_row in rows:
            flag=0
            # print(user_row.username,user_row.password,uname,password)
            if (uname==user_row.username and password==user_row.password):
                flag=1  
                return render_template("welcomeuser.html")

      if flag==0: 
         return "<h1 style=color:red>Invalid user name or password</h1>"
    else:
        return render_template("userlogin.html")   

# <-----------user registration------------>

@app.route('/register',methods = ['GET','POST'])  
def register():  
    if request.method=="GET":
        return render_template("regform.html")
    else:
        username=request.form[ 'username']
        password=request.form[ 'password']
        session=cassandra_connect()
        session.execute('USE "Student"')
        session.execute(
    """
    INSERT INTO user (username,password)
    VALUES(%(username)s, %(password)s)
    """,
    {'username':username, 'password':password}
    )
    return render_template("msg.html")      


@app.route('/spc',methods=['GET']) 
def spc():
     if request.method=="GET": 
        return render_template("spc.html")

@app.route('/patpro',methods=['GET']) 
def patpro():
     if request.method=="GET": 
        return render_template("patpro.html")
@app.route('/home') 
def home():
        return render_template("homepage.html")
@app.route('/bc') 
def bc():
        return render_template("welcomeuser.html")


@app.route('/back',methods=['GET']) 
def back():
     if request.method=="GET": 
        return render_template("welcome.html")
  

#  <------------------manage doctors------------------->

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method=="GET":
        return render_template("add_doctor.html")
    else:
        doc_id=int(request.form[ 'doc_id'])
        spc=request.form[ 'spc']
        doc_name=request.form['doc_name']
        fee=int(request.form[ 'fee'])
        session=cassandra_connect()
        session.execute('use "Student" ')
        session.execute(
    """
    INSERT INTO doc (doc_id,specialization,doctor_name,fee)
    VALUES( %(doc_id)s,%(specialization)s,%(doctor_name)s,%(fee)s)
    """,
    {'doc_id':doc_id,'specialization':spc,'doctor_name':doc_name,'fee':fee}
    )
    return "<h2 style=color:blue>Data inserted..</h2>"



@app.route('/upd', methods=['GET','POST'])
def upd():
    if request.method=="GET":
        return render_template("doc_up.html")
    else:
        doc_id=int(request.form[ 'doc_id'])
        spc=request.form[ 'spc']
        doc_name=request.form['doc_name']
        fee=int(request.form[ 'fee'])
        session=cassandra_connect()
        session.execute('use "Student" ')
        session.execute(
    """
    UPDATE doc set specialization=%(specialization)s,doctor_name=%(doctor_name)s,fee=%(fee)s where doc_id=%(doc_id)s
    """,
     {'doc_id':doc_id,'specialization':spc,'doctor_name':doc_name,'fee':fee}
    )   
    return "<h2 style=color:blue>Updated Succesfully</h2>" 

@app.route('/del', methods=['GET','POST'])
def dele():
    if request.method=="GET":
        return render_template("docdel.html")    
    else:
        doc_id=int(request.form[ 'doc_id'])
        session=cassandra_connect()
        session.execute('USE "Student" ')
        session.execute(
    """
    DELETE from doc where doc_id=%(doc_id)s

    """,
    {'doc_id':doc_id}  
    ) 
    return "<h2 style=color:blue>Deleted</h2>"

@app.route('/disp', methods=['GET'])   
def disp():
    session=cassandra_connect()
    session.execute('USE "Student" ')
    rows = session.execute('SELECT doc_id,specialization,doctor_name,fee FROM doc')
    r=[]
    for doc_row in rows:
        r.append([doc_row.doc_id,doc_row.specialization,doc_row.doctor_name,doc_row.fee])
    r=tuple(r)
    return render_template('docdisp.html',r=r)   


#<--------------------patient profile----------------->

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method=="GET":
        return render_template("patientpro.html")
    else:
        name=request.form['name']
        email=request.form['email']
        gender=request.form['gender']
        age=int(request.form['age'])
        address=request.form['address']
        number=int(request.form[ 'number'])
        state=request.form[ 'state']
        city=request.form[ 'city']
        session=cassandra_connect()
        session.execute('USE "Student"')
        session.execute(
    """
    INSERT INTO patient (name,email,gender,age,address,number,state,city)
    VALUES(%(name)s, %(email)s,%(gender)s,%(age)s,%(address)s,%(number)s,%(state)s,%(city)s)
    """,
    {'name':name, 'email':email,'gender':gender,'age':age,'address':address,'number':number,'state':state,'city':city}
    )
    return "<h2 style=color:blue>Data inserted..</h2>"

@app.route('/updprofile', methods=['GET','POST'])
def updprofile():
    if request.method=="GET":
        return render_template("uppatientpro.html")
    else:
        name=request.form['name']
        email=request.form['email']
        gender=request.form['gender']
        age=int(request.form['age'])
        address=request.form['address']
        number=int(request.form[ 'number'])
        state=request.form[ 'state']
        city=request.form[ 'city']
        session=cassandra_connect()
        session.execute('USE "Student"')
        session.execute(
    """
    UPDATE patient set  email=%(email)s,gender=%(gender)s,age=%(age)s,address=%(address)s,number=%(number)s,state=%(state)s,city=%(city)s where name=%(name)s
    """,
    {'name':name, 'email':email,'gender':gender,'age':age,'address':address,'number':number,'state':state,'city':city}
    )
    return "<h2 style=color:blue>Updated Successfully:)</h2>"

@app.route('/viewpro', methods=['GET','POST'])   
def viewpro():
    if request.method=="GET":
        return render_template("askname.html")
    else:
        name=request.form['name']
        session=cassandra_connect()
        session.execute('USE "Student" ')
        rows = session.execute(
            """
            SELECT * FROM patient WHERE name=%(name)s
            """,
            {'name':name}
            )
        r=[]
        for patient_row in rows:
            r.append([patient_row.name,patient_row.email,patient_row.gender,patient_row.age,patient_row.address,patient_row.number,patient_row.state,patient_row.city])
        r=tuple(r)
        return render_template('prodisp.html',r=r)  

@app.route('/doclist', methods=['GET','POST'])   
def doclist():
        session=cassandra_connect()
        session.execute('USE "Student" ')
        rows = session.execute('SELECT doc_id,specialization,doctor_name,fee FROM doc')
        r=[]
        for doc_row in rows:
            r.append([doc_row.doc_id,doc_row.specialization,doc_row.doctor_name,doc_row.fee])
        r=tuple(r)
        return render_template('docdetails.html',r=r)  


# <--------------------Appointment history------------------>

@app.route('/appoint', methods=['GET','POST'])
def appoint():
    if request.method=="GET":
        return render_template("appoint.html")
    else:
        patient_name=request.form['patient_name']
        doctor_name=request.form['doctor_name']
        specialization=request.form['specialization']
        date=request.form['date']
        time=request.form[ 'time']
        session=cassandra_connect()
        session.execute('USE "Student"')
        session.execute(
    """
    INSERT INTO appoint (patient_name,doctor_name,specialization,date,time)
    VALUES(%(patient_name)s, %(doctor_name)s,%(specialization)s,%(date)s,%(time)s)
    """,
    {'patient_name':patient_name, 'doctor_name':doctor_name,'specialization':specialization,'date':date,'time':time}
    )
    return render_template('msgshow.html')


@app.route('/appointup', methods=['GET','POST'])
def appointup():
    if request.method=="GET":
        return render_template("appointup.html")
    else:
        patient_name=request.form['patient_name']
        doctor_name=request.form['doctor_name']
        specialization=request.form['specialization']
        date=request.form['date']
        time=request.form[ 'time']
        session=cassandra_connect()
        session.execute('USE "Student"')
        session.execute(
    """
    UPDATE appoint set doctor_name=%(doctor_name)s,specialization=%(specialization)s,date=%(date)s,time=%(time)s where patient_name=%(patient_name)s
    """,
   {'patient_name':patient_name, 'doctor_name':doctor_name,'specialization':specialization,'date':date,'time':time}
    )
    return "<h2 style=color:blue>Updated Successfully:)</h2>"

@app.route('/viewappoint', methods=['GET','POST'])   
def viewappoint():
    if request.method=="GET":
        return render_template("askpname.html")
    else:
        patient_name=request.form['patient_name']
        session=cassandra_connect()
        session.execute('USE "Student" ')
        rows = session.execute(
            """
            SELECT * FROM appoint WHERE patient_name=%(patient_name)s
            """,
            {'patient_name':patient_name}
            )
        r=[]
        for appoint_row in rows:
            r.append([appoint_row.patient_name,appoint_row.doctor_name,appoint_row.specialization,appoint_row.date,appoint_row.time])
        r=tuple(r)
        return render_template('appointdisp.html',r=r)  

@app.route('/cancel', methods=['GET','POST'])
def cancel():
    if request.method=="GET":
        return render_template("appointdel.html")    
    else:
        patient_name=request.form['patient_name']
        session=cassandra_connect()
        session.execute('USE "Student" ')
        session.execute(
    """
    DELETE from appoint where patient_name=%(patient_name)s

    """,
    {'patient_name':patient_name} 
    ) 
    return "<h2 style=color:blue>Appointment Cancelled</h2>"

@app.route('/viewallapp', methods=['GET'])   
def viewallapp():
    session=cassandra_connect()
    session.execute('USE "Student" ')
    rows = session.execute('SELECT patient_name,doctor_name,specialization,date,time FROM appoint')
    r=[]
    for appoint_row in rows:
            r.append([appoint_row.patient_name,appoint_row.doctor_name,appoint_row.specialization,appoint_row.date,appoint_row.time])
    r=tuple(r)
    return render_template('dispallappoint.html',r=r)   


@app.route('/madoc',methods=['GET']) 
def madoc():
     if request.method=="GET": 
        return render_template("managedoc.html")

@app.route('/appointdetails',methods=['GET']) 
def appointdetails():
     if request.method=="GET": 
        return render_template("manageappoint.html")



if __name__ == '__main__':  
   app.run(debug = True)  
 