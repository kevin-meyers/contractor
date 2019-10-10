import json
import os

from pymongo import MongoClient

if not os.getenv('IS_PROD'):
    from dotenv import load_dotenv
    load_dotenv()

client = MongoClient(
    f'mongodb+srv://{os.getenv("MONGODB_USER")}:{os.getenv("MONGODB_PASSWORD")}@'
    'cluster0-gwjng.mongodb.net/admin?retryWrites=true&w=majority', connect=False
)
db = client.Contractor
items = db.items

def add_items(path='data/items.json'):
    with open(path) as f:
        for line in f:
            items.insert_one(json.loads(line))

def drop_items():
    items.drop()


if __name__ == '__main__':
    drop_items()
    add_items()
