#!/usr/bin/python
import json
from bson import json_util
from milestone1 import insert_document, read_document, update_document, delete_document
import bottle
from bottle import route, run, request, abort, post, get, put
import ast

#partOne
@route('/hello', method='GET')
def greeting():
  name=request.query.name
  greeting = {'hello' : name}
  return greeting

@post('/strings')
def new_greeting():
  newDoc = request.body.getvalue()
  newDoc = ast.literal_eval(newDoc) 
  return newDoc
  
# set up URI paths for REST service

#URI Read

@route('/read', method='GET')
def get_document():
  name=request.query.business_name
  result = read_document(name)  
  return result

#URI Create
@post('/create')
def create_document():
  newDoc = request.body.getvalue()
  newDoc = ast.literal_eval(newDoc) 
  insert_document(newDoc)
  
@route('/update', method='GET')
def modify_document():
  doc_id=request.query.id
  result=request.query.result
  update_document(doc_id, result)
  
@route('/delete', method='GET')
def remove_document():
  doc_id=request.query.id
  delete_document(doc_id)

if __name__ == '__main__':	
	#app.run(debug=True)
	run(host='localhost', port=8080)