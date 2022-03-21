import time
from flask import Flask

from flask_cros import CORS
CORS(app, resources={r'/*':{'origins': '*'}})
@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

from flask_cros import cross_origin


@app.route('/api/query',methods=['POST','GET'])
@cross_origin()
def get_current_blime():
    return {'blime': 'time flies'}
