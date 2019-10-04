import json
import os

from flask import Flask, render_template, request
from pymongo import MongoClient

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=host)
db = client.Contractor
items = db.items

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html', items=items.find())

@app.route('/items/<item_id>')
def show_item(item_id):
    item = item


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
