import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Comment


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
db = SQLAlchemy(app)


from application import routes
