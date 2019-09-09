from flask import Flask, request, jsonify, render_template, redirect
import os
import json
import pusher
from datetime import datetime
from database import db_session
from models import Site_Infos

app = Flask(__name__)


@app.route('/')
def index():
    sites_infos = Site_Infos.query.all()
    return render_template('index.html', sites_infos=sites_infos)


#tell Flask to close the connection to the database as soon as an operation is complete
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# run Flask app
if __name__ == "__main__":
    app.run()
