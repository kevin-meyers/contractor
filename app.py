import json
import os

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

if not os.getenv('IS_PROD'):
    from dotenv import load_dotenv
    load_dotenv()


client = MongoClient(
    f'mongodb+srv://{os.getenv("MONGODB_USER")}:{os.getenv("MONGODB_PASSWORD")}@'
    'cluster0-gwjng.mongodb.net/admin?retryWrites=true&w=majority', connect=False
)

db = client.Contractor
items = db.items
cart = db.cart

app = Flask(__name__)


if not items.find_one():
    from add_items import add_items
    add_items()

@app.route('/')
def home():
    return render_template('index.html', items=list(items.find()))

@app.route('/items/<item_id>')
def show_item(item_id):
    item = items.find_one({'_id': ObjectId(item_id)})

    return render_template('item.html', item=item)

@app.route('/cart/<item_id>', methods=['POST'])
def add_item_to_cart(item_id):
    if cart.find_one({'_id': ObjectId(item_id)}):
        cart.update_one(
            {
                {'_id': ObjectId(item_id)},
                {'$inc': {'quantity': int(1)}}
            }
        ) 
    else:
        cart.insert_one({**items.find_one({'_id': ObjectId(item_id)}), **{'quantity': 1}})

    return redirect(url_for('show_cart', items=list(cart.find())))


@app.route('/cart')
def show_cart():
    return str(list(cart.find()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))
