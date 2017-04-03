#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif', 'xls', 'xlsx', 'pdf'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['POST'])
def connect():
    return 'success'


if __name__ == '__main__':
    # get connection hosted in 4000
    app.run(host='127.0.0.1', port=4000, debug=True)
