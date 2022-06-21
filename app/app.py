from datetime import date, datetime
from flask import Flask, request, render_template, jsonify
from flask_mongoengine import MongoEngine
from httplib2 import Response
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
# app.config['MONGO_URI'] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' \
#                                        + os.environ['MONGODB_PASSWORD'] \
#                                        + '@' + os.environ['MONGODB_HOSTNAME'] \
#                                        + ':27017/' + os.environ['MONGODB_DATABASE']

with open("/tmp/secret", 'r') as f:
    secret = f.read()

app.config['MONGO_URI'] = secret

db = MongoEngine(app)


class Payment(db.Document):
    username = db.StringField(required=True)
    date = db.DateTimeField()
    products = db.DictField()
    ammount = db.FloatField()


@app.route("/")
def home():
    return "Payments API"


@app.route("/payments", methods=['POST', 'GET'])
def payments():
    if request.method == 'POST':
        body = request.get_json(force=True)
        body["date"] = datetime.today()
        payment = Payment(**body).save()

        data = {'message':'Payment is processing'}
        resp = jsonify(data, 200)
    return resp


@app.route("/paymentConfirmation", methods=['GET', 'POST'])
def paymentConfirmation():
    if request.method == 'POST':
        res = Response("Payment confirmed")
        res.status = 200
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
