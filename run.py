from flask import Flask, render_template, url_for, request, send_from_directory,redirect, abort, flash, jsonify

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
# START APP
if __name__ == '__main__':
    app.run(port = 3001, debug=True)
