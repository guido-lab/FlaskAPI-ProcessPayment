from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
import json, os, datetime
from flask_migrate import Migrate
from models import GetwayType, Payments
from serializer import PaymentsSerializer

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/payments.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/payment', methods=['GET'])
def query_records():
    name = Payments.query.all()
    post_schema = PaymentsSerializer()
    posts_schema = PaymentsSerializer(many=True)
    
    return {"data": posts_schema.dump(name)} 


@app.route('/addpayment', methods=['POST'])
def addpost():

    try:
        credit_card_number = request.form['credit_card_number']
        card_holder = request.form['card_holder']
        expiration_date = request.form['expiration_date']
        security_code = request.form['security_code']
        amount = request.form['amount']

        if len(credit_card_number) != 16:
            return json.dumps({'error': "Not a valid card number"}), 400, {'ContentType':'application/json'}

        if datetime.datetime.fromisoformat(expiration_date) < datetime.datetime.now():
            return json.dumps({'success': "Not a valid Expiration Date"}), 400, {'ContentType':'application/json'}

        if amount.isnumeric():
            if int(amount) > 0 and int(amount) <= 20:
                getway_tp = GetwayType.query.filter_by(name='CheapPaymentGateway').first()

            elif int(amount) >= 21 and int(amount) <= 400:
                getway_tp = GetwayType.query.filter_by(name='ExpensivePaymentGateway').first()

            elif int(amount) > 400:
                getway_tp = GetwayType.query.filter_by(name='PremiumPaymentGateway').first()

            else:
                return json.dumps({'success': "Not a valid amount"}), 400, {'ContentType':'application/json'}

        else:
            return json.dumps({'success': "Not a valid amount"}), 400, {'ContentType':'application/json'}

        payment = Payments(credit_card_number = credit_card_number, 
                        card_holder = card_holder, 
                        expiration_date = datetime.datetime.fromisoformat(expiration_date), 
                        security_code = security_code, 
                        amount = int(amount),
                        deleted = False,
                        create_date = datetime.datetime.now(),
                        getway_type_id = getway_tp.id)

        db.session.add(payment)
        db.session.commit()

        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    except Exception as e:
        return json.dumps({}), 400, {'ContentType':'application/json'}



if __name__ == '__main__':
    app.run(debug=True)