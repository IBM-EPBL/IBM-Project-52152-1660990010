from site import USER_BASE
from flask import Flask, render_template, url_for, request, redirect
import sqlite3 as sql

 
app=Flask(__name__)
app.secret_key ='kaviya'



@app.route('/')
def home():
    con =sql.connect('user_base.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select *from user')

    users= cur.fetchall()
    con.close()
    return render_template('Index.html',users=users)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/Signin')
def signin():
    return render_template('Signin.html')

@app.route('/Signup')
def singup():
    return render_template('Signup.html')
@app.route('/user/<id>')
def user_page(id):
    with sql.connect('user_base.db') as con:
        con.row_factory=sql.Row
        cur =con.cursor()
        cur.execute(f'SELECT * FROM user WHERE email="{id}"')
        user = cur.fetchall()
    return render_template("user_info.html", user=user[0])

@app.route('/accessbackend', methods=['POST','GET'])
def accessbackend():
    if request.method == "POST":
        try:
            firstname=request.form['firstname']
            lastname=request.form['lastname']
            e_mail= request.form['email']
            phone=request.form['phone']
            password=request.form['password']
            dob=request.form['dob']
            with sql.connect('user_base.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO user (firsname,lastname,email,phone,pasword,dod) VALUES(?,?,?,?,?)',
                            (str(firstname),str(lastname),str(e_mail),str(phone),str(password),str(dob)))
                con.commit()
                msg='you are Resgistered!'
        except:
            con.rollback()
            msg='some error'
        finally:
            print(msg)
            return redirect(url_for('home'))
    else:
        try:
            tue=request.args.get('email')
            tue=request.args.get('password')
            print(tue,tuple)
            with sql.connect('user_base.db') as con:
                con.row_factory=sql.row
                cur=con.cursor()
                cur.execute(f'SELECT password FROM user WHER email="{tue}"')
                user= cur.fetchall()
        except:
            print('error')
            con.rollback()
        finally:
            if len(user) >0:
                if tuple == user[0][0]:
                    return redirect(url_for("user_page",id=tue))
                print(user[0][0])
            return redirect(url_for(signin))
from site import USER_BASE
from flask import Flask, render_template, url_for, request, redirect
import sqlite3 as sql

 
app=Flask(__name__)
app.secret_key ='kaviya'



@app.route('/')
def home():
    con =sql.connect('user_base.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select *from user')

    users= cur.fetchall()
    con.close()
    return render_template('Index.html',users=users)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/Signin')
def signin():
    return render_template('Signin.html')

@app.route('/Signup')
def singup():
    return render_template('Signup.html')
@app.route('/user/<id>')
def user_page(id):
    with sql.connect('user_base.db') as con:
        con.row_factory=sql.Row
        cur =con.cursor()
        cur.execute(f'SELECT * FROM user WHERE email="{id}"')
        user = cur.fetchall()
    return render_template("user_info.html", user=user[0])

@app.route('/accessbackend', methods=['POST','GET'])
def accessbackend():
    if request.method == "POST":
        try:
            firstname=request.form['firstname']
            lastname=request.form['lastname']
            e_mail= request.form['email']
            phone=request.form['phone']
            password=request.form['password']
            dob=request.form['dob']
            with sql.connect('user_base.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO user (firsname,lastname,email,phone,pasword,dod) VALUES(?,?,?,?,?)',
                            (str(firstname),str(lastname),str(e_mail),str(phone),str(password),str(dob)))
                con.commit()
                msg='you are Resgistered!'
        except:
            con.rollback()
            msg='some error'
        finally:
            print(msg)
            return redirect(url_for('home'))
    else:
        try:
            tue=request.args.get('email')
            tue=request.args.get('password')
            print(tue,tuple)
            with sql.connect('user_base.db') as con:
                con.row_factory=sql.row
                cur=con.cursor()
                cur.execute(f'SELECT password FROM user WHER email="{tue}"')
                user= cur.fetchall()
        except:
            print('error')
            con.rollback()
        finally:
            if len(user) >0:
                if tuple == user[0][0]:
                    return redirect(url_for("user_page",id=tue))
                print(user[0][0])
            return redirect(url_for(signin))
