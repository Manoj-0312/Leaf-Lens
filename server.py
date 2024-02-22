from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from MarketPrices import fruit_prices,vegetable_prices

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:YOUR_PASWORD@localhost:5432/Leaf_lens'


db = SQLAlchemy(app)
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

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return jsonify("hello")

@app.route('/fruit')
def get_all_fruits():
    MarketPrices_of_all =   MarketPrices_fruits.query.all()
    item_prices = [{'name':item.name,'prices': {'wholesale_price': item.wholesale_price,
                                                'retail_price': item.retail_price,
                                                'shoping_mall_price': item.shoping_mall_price}} for item in MarketPrices_of_all]
    return jsonify({'Market_prices':item_prices})

@app.route('/vegetables')
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
    app.run(debug=True,port=5050)