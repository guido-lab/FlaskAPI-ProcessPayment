from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # new
import os
from models import GetwayType, Payments

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/payments.db'
db = SQLAlchemy(app)
ma = Marshmallow(app) # new

class GetwayTypeSerializer(ma.Schema):
    class Meta:
        fields = ("id", "name", "descripton")
        model = GetwayType

class PaymentsSerializer(ma.Schema):
    class Meta:
        fields = ("id", "credit_card_number", "card_holder", "expiration_date", "security_code", "amount", "getway_type_id")
        model = Payments
