from app import GetwayType
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/payments.db'

db = SQLAlchemy(app)

class GatewayTypeFill:
    def checkGatewayType():

        cnt = GetwayType.query.count()

        if cnt < 3:
            gt1 = GetwayType(name='PremiumPaymentGateway', descripton="Premium Payment Gateway")
            db.session.add(gt1)
            db.session.commit()

            gt2 = GetwayType(name='ExpensivePaymentGateway', descripton="Expensive Payment Gateway")
            db.session.add(gt2)
            db.session.commit()
            
            gt3 = GetwayType(name='CheapPaymentGateway', descripton="Cheap Payment Gateway")
            db.session.add(gt3)
            db.session.commit()

if __name__ == '__main__':
    GatewayTypeFill.checkGatewayType()