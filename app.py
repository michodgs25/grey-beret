import os
from flask import (
    Flask, render_template, redirect, requests, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/weather")
def get_weather():
    """Define domain pathway to homepage.
    Args:
    get index: define opening page of the platform.
    Returns:
    the weather.html document.
    """
    return render_template("weather.html")
