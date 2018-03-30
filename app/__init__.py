# coding:utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:shuju4KU@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "320552885fda447f9c62e929dc362dea"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprit
from app.admin import admin as admin_blueprit

app.register_blueprint(home_blueprit)
app.register_blueprint(admin_blueprit, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
