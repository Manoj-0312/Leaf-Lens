from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,login_required,logout_user,current_user,LoginManager
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from fruitVegetable import fruit_dataset,vegetable_dataset

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hmmm@localhost/leaflens'
app.config['SECRET_KEY'] = 'jfhudnfsdussud'

db=SQLAlchemy(app)
migrate = Migrate(app, db) 
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(200), nullable=False)

class ContactUs(db.Model):
    Name=db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    Phno=db.Column(db.Numeric,nullable=False)
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Message=db.Column(db.String(10000),nullable=False)

class fruit(db.Model):
    Fruit=db.Column(db.String(100),nullable=False)
    disease = db.Column(db.String(1000),nullable=False)
    fruit_id = db.Column(db.Integer, primary_key=True)

class Fertilizer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fruit_disease_id = db.Column(db.Integer, db.ForeignKey('fruit.fruit_id'), nullable=False)
    fruit_disease = db.relationship('fruit', backref=db.backref('fertilizers', lazy=True))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        user=User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user,remember=True)
                return redirect(url_for('index'))
            else:
                error_msg="please check your password it is incorrect"
                return render_template('login_register.html',error_msg=error_msg)
        else:
            error_msg="username is incorrect"
            return render_template('login_register.html',error_msg=error_msg)

    return render_template('login_register.html')

@app.route('/contactus',methods=['GET', 'POST'])
def contactus():
    if request.method=='POST':
        Name=request.form['Name']
        Email=request.form['Email']
        Phno=request.form['Phone Number']
        Message=request.form['Message']

        data=ContactUs(Name=Name,email=Email,Phno=Phno,Message=Message)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('contact_us.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        error_msg="NONE"
        username = request.form['username']
        email=request.form['email']
        password = request.form['Password']

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            db.session.rollback()
            error_msg ="Username already exists. Please choose a different username."
            return render_template('sign_up.html',error_msg=error_msg)
        
        new_user = User(username=username, password=generate_password_hash(password),email=email)
        db.session.add(new_user)
        db.session.commit() 
        return redirect(url_for('login'))

    return render_template('sign_up.html')

if __name__=='__main__':
    app.run(debug=True)
