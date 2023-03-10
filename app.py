import os
import requests
from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from dotenv import load_dotenv
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)
mail = Mail(app)

if app.config["DEBUG"] == True:
    app.config.from_object('config.DevConfig')
else:
    app.config.from_object('config.ProdConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Faq(db.Model):
    __tablename__ = 'faq'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150))
    answer = db.Column(db.String(100))
    timestamp = db.Column(db.String(100))

    def __init__(self, question, answer, timestamp):
        self.question = question
        self.answer = answer
        self.timestamp = timestamp

with app.app_context():
    db.create_all()

#index route
@app.route('/')
def index():
    data = Faq.query.all()
    return render_template('index.html', data=data)

#add faq
@app.route('/add-faq', methods=['GET', 'POST'])
def addfaq():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')
        timestamp = datetime.utcnow()
        
        data = Faq(question, answer, timestamp)
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add-faq.html')

if __name__ == '__main__':
    app.run()