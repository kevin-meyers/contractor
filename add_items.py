import json
import os

from pymongo import MongoClient


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')                    
client = MongoClient(host=f'{host}')
db = client.Contractor
items = db.items

def add_items(path):
    with open(path) as f:
        for line in f:
            items.insert_one(json.loads(line))


if __name__ == '__main__':
    add_items('data/items.json')
