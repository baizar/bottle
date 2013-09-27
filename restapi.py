#!/usr/bin/python
import json
import bottle
from bottle import route, run, request, abort

bigdict = {}
 
@route('/conf/:key', method='PUT')
def put_pair(key):
    value = request.body.read()
    if not value:
        abort(400, 'No data received')
    bigdict[key] = value
    

     
@route('/conf/:key', method='GET')
def get_value(key):
    return bigdict[key]

 
run(host='localhost', port=8000)
