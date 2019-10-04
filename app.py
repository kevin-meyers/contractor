import os

from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

host = (
    f'mongodb+srv://{os.getenv("MONGODB_USER")}:{os.getenv("MONGODB_PASSWORD")}@'
    'cluster0-gwjng.mongodb.net/admin?retryWrites=true&w=majority'
)

client = MongoClient(host=host)

db = client.Contractor
items = db.items

print(items.find_one())
@app.route('/')
def test():
    return items.find_one()['name']
