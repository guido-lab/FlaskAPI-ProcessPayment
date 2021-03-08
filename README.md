# FlaskAPI-ProcessPayment

## Coding exercise:
Write a Flask Web API with only 1 method called “ProcessPayment” that receives a request like this
- CreditCardNumber (mandatory, string, it should be a valid credit card number)
- CardHolder: (mandatory, string)
- ExpirationDate (mandatory, DateTime, it cannot be in the past)
- SecurityCode (optional, string, 3 digits)
- Amount (mandatoy decimal, positive amount)

The response of this method should be 1 of the followings based on
- Payment is processed: 200 OK
- The request is invalid: 400 bad request
- Any error: 500 internal server error

The payment could be processed using different payment providers (external services) called:
- PremiumPaymentGateway
- ExpensivePaymentGateway
- CheapPaymentGateway.

The payment gateway that should be used to process each payment follows the next set of
business rules:

a) If the amount to be paid is less than £20, use CheapPaymentGateway.

b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
Otherwise, retry only once with CheapPaymentGateway.

c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
in case payment does not get processed.

Recommendations:
- The classes should be written in such way that they are easy to test.
- Write as many tests as you think is enough to be certain about your solution works -
Use SOLID principles.
- Decouple the logic the prediction logic from the API as much as possible

## SETUP

1- The following command creates a new virtual environment named venv in the current directory

```bash
$ python -m venv env
```

2- Activate virtual environment:

```bash
(Mac/Linux) $ source env/bin/activate
```

```bash
(Windows) $ source env/Scripts/activate
```
3- Installing requirements:


```bash
$ pip install -r requirements.txt
```

4- Running code

```bash
$ python app.py
```

The file checkGatewayType.py it's for checking if there is records on Payment-Type table 
If there are not, for filling it with demo records just needed to execute 

```bash
$ python checkGatewayType.py
```
The app will be running on localhost port 5000 (http://127.0.0.1:5000)

The endpoint "/addpayment" is accepting the POST request with all data required

POST: http://127.0.0.1:5000/addpayment

GET: http://127.0.0.1:5000/payment 

Example:

payload='credit_card_number=1234567890123456&card_holder=Joe&expiration_date=2021-09-09%2011%3A30%3A21&security_code=000&amount=2'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

