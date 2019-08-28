from flask import Flask
import requests
import openaq
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask import render_template
from .models import DB, Record

api = openaq.OpenAQ()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')

    def root():
        status, body = api.measurements(x='', parameter = '')
        #model
 
        return render_template("root.html",)

    @app.route('/refresh', methods = ['POST', 'GET'])
    def refresh():
        DB.drop_all()
        DB.create_all()
        status, body = api.measurements(x='', parameter = '')

        #refresh scraping?

        return render_template('refresh.html',)
 
    @app.route('/dashboard', methods=['GET'])
    def dashboard():
        
        return render_template("dashboard.html",)

    return app
