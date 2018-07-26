#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:24:00 2018

@author: devang
"""
from flask import Flask
import main # Main Python Script

app = Flask(__name__)

@app.route('/home/devang/Desktop/hackathon dataset/guide dataset')
def my_script():
    main.some_func()



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)