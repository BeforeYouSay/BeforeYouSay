from flask import Flask
from flask import render_template
from main import clean_content as library_clean_content
from flask import json
from flask import request
app = Flask(__name__)

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
