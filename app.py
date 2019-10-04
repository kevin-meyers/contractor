from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'
