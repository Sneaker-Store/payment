import datetime
import logging
import sys
import psycopg2
from psycopg2 import OperationalError
from flask import Flask, request, render_template, make_response
from flask_mongoengine import MongoEngine
from httplib2 import Response
import os   

from pip import main

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

def get_db_connection():
    conn = psycopg2.connect(
            dbname="paymentdb",
            user=os.environ['pay'],
            password=os.environ['payment'])

    return conn


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/payments", methods=['POST'])
def payments():

    # headers = {'token': request.headers['token'], 'email': request.headers['email']}
    # r = requests.get('http://localhost:5000/auth', headers=headers)
    
    # if r.status_code != 200:
    #     return make_response(
    #         "Not authenticated", r.status_code
    # )
    
    if request.method == 'POST':
        body = request.get_json(force=True)
        insert_form = "INSERT INTO payment (username, data, ammount) VALUES ({}, {}, {});".format(body['username'], \
            'NOW()', body['ammount'])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(insert_form)
        conn.commit()
        cur.close()
        conn.close()

        res = Response("Transaction complete!")
        res.status = 200

    return res

if __name__ == '__main__':
    app.run(debug=True)