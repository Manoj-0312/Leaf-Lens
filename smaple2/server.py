from flask_sqlalchemy import SQLAlchemy
from MarketPrices import fruit_prices,vegetable_prices
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from datetime import datetime
from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, ARRAY
from flask_login import UserMixin,login_user,login_required,logout_user,current_user,LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
import requests
from MarketPrices import fruit_prices,vegetable_prices
from fertlizer import transformed_data
import tensorflow as tf
import os
import numpy as np
from PIL import Image
from io import BytesIO


model = tf.keras.models.load_model("M:/Documents/Plant_disease_model/models/version_1/") 





def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((128,128))  # Assuming input size of the model is 224x224
    img_array = np.array(image).astype('uint8')
    img_array = np.expand_dims(img_array,0)
    return img_array


classes = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:manoj4897@localhost:5432/Leaf_lens'
db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = 'uploads'



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(200), nullable=False)

    


class MarketPrices_fruits(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),primary_key=True,nullable=False)
    img_url = db.Column(db.String(800),nullable=False)
    wholesale_price = db.Column(db.Integer,nullable=False)
    retail_price = db.Column(db.Integer,nullable=False)
    shoping_mall_price = db.Column(db.Integer,nullable=False)

class MarketPrices_vegs(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),primary_key=True,nullable=False)
    img_url = db.Column(db.String(800),nullable=False)
    wholesale_price = db.Column(db.Integer,nullable=False)
    retail_price = db.Column(db.Integer,nullable=False)
    shoping_mall_price = db.Column(db.Integer,nullable=False)

class fruit(db.Model):
    Fruit=db.Column(db.String(100),nullable=False)
    disease = db.Column(db.String(1000),nullable=False)
    fruit_id = db.Column(db.Integer, primary_key=True)

class fertilizer_table(db.Model):
    fertilizer_name = Column(String, primary_key=True)
    diseases = Column(ARRAY(String))
    image_urls = Column(String)
    function = Column(String)
    application = Column(String)

class ContactUs(db.Model):
    Name=db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    Phno=db.Column(db.Numeric,nullable=False)
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Message=db.Column(db.String(10000),nullable=False)



with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = "bangalore"

    url = "https://api.openweathermap.org/data/2.5/forecast/"


    params = {
        'q': city,
        'appid': '13129000fa3d9c6f1cef8e8524284c07'
    }
    

    response = requests.get(url, params=params)
    weather_details = response.json()
    if response.status_code == 200:
        print("Received data from API:")
    else:
        print("Failed to retrieve data from API. Status code:", response.status_code)
    weather_data = [[]]

    for i in range(0,40):
        weather_data[0].append(dict(date=weather_details["list"][i]["dt_txt"],
                             temparatures=round(weather_details["list"][i]["main"]["temp"]-273.15,1),
                             todays_forecast=weather_details["list"][i]["weather"][0]["main"],
                             description=weather_details["list"][i]["weather"][0]["description"],
                             humidity = weather_details["list"][i]["main"]["humidity"],
                             wind_speed = weather_details["list"][i]["wind"]["speed"]
                             
                             ))
    weather_data.append(params["q"].capitalize())
    return render_template('index.html',weather = weather_data)

@app.route('/about_us')
def about_us():
    
    return render_template('about_us.html')



@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('predict.html', prediction="No file uploaded")

        file = request.files['image']
        if file.filename == '':
            return render_template('predict.html', prediction="No selected file")

        if file:
            # Save the uploaded file to a secure location
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Preprocess the uploaded image
            processed_image = preprocess_image(file_path)

            # Make predictions using the preprocessed image
            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction[0])
            predicted_class = classes[predicted_class]

            return render_template('predict.html', prediction=predicted_class)

    return render_template('predict.html', prediction="ERROR")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        user=User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                # login_user(user,remember=True)
                return redirect(url_for('home'))
            else:
                error_msg="please check your password it is incorrect"
                return render_template('login.html',error_msg=error_msg)
        else:
            error_msg="username is incorrect"
            return render_template('login.html',error_msg=error_msg)

    return render_template('login.html',error_msg="")

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
        return redirect(url_for('contactus'))
    return render_template('contactus.html')

@app.route("/products")
def products():
    fertilizers = fertilizer_table.query.all()
    transformed_data = {}
    for fertilizer in fertilizers:
        transformed_data[fertilizer.fertilizer_name] = {
            'Disease': fertilizer.diseases,
            'Image_URLs': fertilizer.image_urls,
            'Function': fertilizer.function,
            'Application': fertilizer.application
        }
    return render_template('fertilizer.html', transformed_data=transformed_data)
@app.route('/more')
def more():
    fruits_data = MarketPrices_fruits.query.all()
    
    vegs_data = MarketPrices_vegs.query.all()
    
    return render_template('market.html', fruits_data=fruits_data, vegs_data=vegs_data)


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








@app.route('/get_fruit')
def get_all_fruits():
    MarketPrices_of_all =   MarketPrices_fruits.query.all()
    item_prices = [{'name':item.name,'prices': {'wholesale_price': item.wholesale_price,
                                                'retail_price': item.retail_price,
                                                'shoping_mall_price': item.shoping_mall_price}} for item in MarketPrices_of_all]
    return jsonify({'Market_prices':item_prices})

@app.route('/get_vegetables')
def get_all_vegetables():
    MarketPrices_of_all =   MarketPrices_vegs.query.all()
    item_prices = [{'name':item.name,'prices': {'wholesale_price': item.wholesale_price,
                                                'retail_price': item.retail_price,
                                                'shoping_mall_price': item.shoping_mall_price}} for item in MarketPrices_of_all]
    return jsonify({'Market_prices':item_prices})

@app.route("/add_fruits")
def add_prices_fruits():
    fruit_names = list(fruit_prices.keys())
    for i in range(len(fruit_names)):
        name = fruit_names[i]
        img_url = fruit_prices[fruit_names[i]]['url']
        wholesale_price = fruit_prices[fruit_names[i]]['Wholesale_Price']
        retail_price = fruit_prices[fruit_names[i]]['Retail_Price'][0]
        shoping_mall_price = fruit_prices[fruit_names[i]]['Shopping_Mall_Price'][0]
        new_fruit = MarketPrices_fruits(name=name,img_url=img_url,wholesale_price=wholesale_price,retail_price=retail_price,shoping_mall_price=shoping_mall_price)
        db.session.add(new_fruit)
        db.session.commit()

    return jsonify({'message':"done"})

@app.route("/add_vegs")
def add_prices_vegs():
    vegs_name = list(vegetable_prices.keys())
    for i in range(len(vegs_name)):
        name = vegs_name[i]
        img_url = vegetable_prices[vegs_name[i]]['url']
        wholesale_price = vegetable_prices[vegs_name[i]]['Wholesale_Price']
        retail_price = vegetable_prices[vegs_name[i]]['Retail_Price'][0]
        shoping_mall_price = vegetable_prices[vegs_name[i]]['Shopping_Mall_Price'][0]
        new_fruit = MarketPrices_vegs(name=name,img_url=img_url,wholesale_price=wholesale_price,retail_price=retail_price,shoping_mall_price=shoping_mall_price)
        db.session.add(new_fruit)
        db.session.commit()

    return jsonify({'message':"done"})

if __name__=='__main__':
    app.run(debug=True)