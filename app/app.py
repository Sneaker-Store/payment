from datetime import date, datetime
import requests
from flask import Flask, request, render_template, make_response
from flask_mongoengine import MongoEngine
from httplib2 import Response
import os   

from pip import main

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.config['MONGO_URI'] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' \
                                       + os.environ['MONGODB_PASSWORD'] \
                                       + '@' + os.environ['MONGODB_HOSTNAME'] \
                                       + ':27017/' + os.environ['MONGODB_DATABASE']
#app.config['MONGO_URI'] = "mongodb://localhost:27017/payment"

db = MongoEngine(app)

class Payment(db.Document):
    username = db.StringField(required=True)
    date = db.DateTimeField()
    products = db.DictField()
    ammount = db.FloatField()



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/payments", methods=['GET', 'POST'])
def payments():

    headers = {'token': request.headers['token'], 'email': request.headers['email']}
    r = requests.get('http://localhost:5000/auth', headers=headers)
    if r.status_code != 200:
        return make_response(
            "Not authenticated", r.status_code
    )

    # if request.method == 'GET':
    #     global ammount
    #     ammount = request.get_json(force=True)
    #     print(ammount)
    #     #ammount = ammount["ammount"]

    #     res = Response("Payment Information")
    #     res.status = 200
        
    
    if request.method == 'POST':
        body = request.get_json(force=True)
        body["date"] = datetime.today()
        payment = Payment(**body).save()

        res = Response("Transaction complete!")
        res.status = 200


    return res

if __name__ == '__main__':
    app.run(debug=True)