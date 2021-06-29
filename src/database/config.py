from app import app
from flask_pymongo import PyMongo

app.config["MONGO_URI"]="mongodb://localhost/sat"
mongo = PyMongo(app)