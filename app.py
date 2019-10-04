import json
import os

from flask import Flask, render_template, request
from pymongo import MongoClient


client = MongoClient("mongodb+srv://Kevin:hoiiaATXovVdCW54@cluster0-gwjng.mongodb.net/admin?retryWrites=true&w=majority")
db = client.Contractor
items = db.items

app = Flask(__name__)

if not items.find_one():
    from add_items import add_items
    add_items()

@app.route('/')
def home():
    return render_template('base.html', items=items.find())

@app.route('/items/<item_id>')
def show_item(item_id):
    item = item


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
  
