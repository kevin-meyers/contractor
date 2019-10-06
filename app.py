import json
import os

from flask import Flask, render_template, request
from pymongo import MongoClient

if not os.getenv('IS_PROD'):
    from dotenv import load_dotenv
    load_dotenv()


client = MongoClient(
    f'mongodb+srv://{os.getenv("MONGODB_USER")}:{os.getenv("MONGODB_PASSWORD")}@'
    'cluster0-gwjng.mongodb.net/admin?retryWrites=true&w=majority'
)

db = client.Contractor
items = db.items

app = Flask(__name__)


if not items.find_one():
    from add_items import add_items
    add_items()

@app.route('/')
def home():
    print(str(list(items.find())))
    return render_template('base.html', items=list(items.find()))

@app.route('/items/<item_id>')
def show_item(item_id):
    item = item


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))
