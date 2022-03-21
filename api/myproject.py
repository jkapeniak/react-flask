import time
from flask import request
import json
from flask import Flask
from flask_cors import CORS
from course_searcher import search_course 
app = Flask(__name__)
#CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}})
@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

from flask_cors import cross_origin

#@app.route('/api/query',methods=['POST','GET'])
#@cross_origin()
#def get_current_blime():
#    return {'blime': 'time flies'}

@app.route('/api/query', methods = ['POST'])
def get_query_from_react():
    data = request.get_json()
    print("ALI")
    print("dfnjkasnkjd")
    print(data['data']['name'])
    #return data

    list_query = data['data']['name'].split(" ")
    # aList = json.dumps(data['data']['name'])

    print("List query")
    print(list_query)
    mylist = ['cis', 'x', '0.75', 'f']

    # other = search_course(data['data']['name'])
    other = search_course(list_query)

    print("other")
    print(other)
    # other = [{'cc': 'CIS*3750', 'cred': '[0.75]', 'desc': 'System Analysis and Design in Applications', 'off': 'Fall and Winter', 'preqArr': [{'preq': '9.00 credits ', 'type': 'mand'}, {'preq': ' CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2430 or ENGG*1420)', 'type': 'or'}]}, {'cc': 'CIS*3760', 'cred': '[0.75]', 'desc': 'Software Engineering', 'off': 'Fall and Winter', 'preqArr': [{'preq': 'CIS*2750', 'type': 'mand'}, {'preq': ' CIS*3750', 'type': 'mand'}]}]
    return json.dumps(other)


# @app.route('/api/course_q/<uuid>', methods = ['POST','GET'])
# @cross_origin()
# def course_q():
#    content = request.get_json(silent=True)
#    print(content) # Do your processing
#   #  return uuid
#    return "Hello, cross-origin-world!"



@app.route('/api/work')
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


#@app.route('/api/query/<uuid>', methods = ['POST','GET'])
#@cross_origin()
#def get_query_from_react():
 #   content = request.get_json(silent=True)
    # print(content) # Do your processing
  #  return uuid

