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

if __name__ == "__main__":
    from os import path
    import os
    extra_dirs = ['templates','static']
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)

    app.run(host='0.0.0.0', extra_files=extra_files)
