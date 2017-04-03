#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'keypair/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif', 'xls', 'xlsx', 'pdf', 'p'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['POST'])
def connect():
    return 'success'


@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['dataset']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'hello, ' + request.form.get('name', 'little apple') + '. success'
    else:
        return 'hello, ' + request.form.get('name', 'little apple') + '. failed'


if __name__ == '__main__':
    # get key hosted in 6000
    app.run(host='127.0.0.1', port=6000, debug=True)
