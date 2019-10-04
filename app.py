import json

from flask import Flask, render_template, request
from pymongo import MongoClient

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=f'{host}')
db = client.Contractor
items = db.items

app = Flask(__name__)


with open('data/items.json') as f:
    ITEMS_LIST = [json.loads(line) for line in f]


@app.route('/')
def home():
    return render_template('base.html', items=ITEMS_LIST)

@app.route('/items/<item_id>')
def show_item(item_id):
    item = item
