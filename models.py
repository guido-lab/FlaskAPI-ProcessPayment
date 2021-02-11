from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os, datetime
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/payments.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class GetwayType(db.Model):
    __tablename__ = 'getwaytype'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descripton = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    payments = relationship("Payments") # havinvg a relation with Payments table

class Payments(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    credit_card_number = db.Column(db.String(50), nullable=False)
    card_holder = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    security_code = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Numeric(10,2), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    getway_type_id = Column(Integer, ForeignKey('getwaytype.id'))

