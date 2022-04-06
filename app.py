from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from httplib2 import Response
from importlib_metadata import method_cache
from flask_bootstrap import Bootstrap
import os

from pip import main

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'SECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.path.join(basedir, 'payments.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db=SQLAlchemy(app)


# o que vou guardar
class Payment(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    username = db.Column(db.String)
    products = db.Column(db.String) 
    ammount = db.Column(db.Float)
    
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/payments", methods=['GET', 'POST'])
def payments():
    if request.method == 'GET':
        trans = Payment.query.all()
        res = Response("Payment Information")
        res.status = 200
        
        
    if request.method == 'POST':
        trans = Payment()
        db.session.add(trans)
        db.session.commit()
        res = Response("Transaction complete!")
        res.status = 200
        return res
    return res

if __name__ == '__main__':
    app.run(debug=True)