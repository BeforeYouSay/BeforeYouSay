from flask import Flask
from flask import render_template
from main import clean_content as library_clean_content
from flask import json
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
from sqlalchemy.dialects.postgresql import JSON, JSONB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+os.environ.get('DATA_DB_HOST')+'/gonano'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class InputLog(db.Model):
    __tablename__ = "input_log"
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ip_address = db.Column(db.Text)
    browser = db.Column(db.Text)
    input = db.Column(db.Text)
    output = db.Column(JSONB)
    is_output_correct = db.Column(db.Boolean, nullable=False, default=None)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/clean_content', methods=['POST'])
def clean_content():
    data = {'cleaned_content': library_clean_content(request.form['content'])}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
