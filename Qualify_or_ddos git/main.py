from flask import Flask, render_template, redirect, url_for, request,session
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["users"]
app=Flask(__name__)

app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
#randomly generated
@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('username')==True:
        return redirect(url_for('login'))

    error = None
    return render_template('home.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():

    row=[]
    error = None
    if request.method == 'POST':
        x=mycol.find({'username':request.form['username'],'password':request.form['password']},{'username':1,'password':1})
        for y in x:
            row.append(y)
        if not row:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    row=[]
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form["cpassword"]:
            error = 'Passwords do not match!'
        x=mycol.find({'username':request.form['username']},{'username':1})
        for y in x:
            row.append(y)
        if row:
            error='username exists!'

        else:
            mycol.insert_one({'name':request.form['name'],'username':request.form['username'],'email':request.form['email'],'dob':request.form['dob'],'password':request.form['password']})
            return redirect(url_for('login'))

    return render_template('register.html', error=error)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('username')
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True)
