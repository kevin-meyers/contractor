import json
import os

from pymongo import MongoClient

client = MongoClient('mongodb+srv://Kevin:hoiiaATXovVdCW54@cluster0-gwjng.mongodb.net/admin?retryWrites=true&w=majority') 
db = client.Contractor
items = db.items

def add_items(path='data/items.json'):
    with open(path) as f:
        for line in f:
            items.insert_one(json.loads(line))
