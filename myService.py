#!/usr/bin/python
import json
from bson import json_util
from crudMarket import create_document, read_document, update_document, delete_document
import bottle
from bottle import route, run, request, abort, post, get, put
import ast


  
# set up URI paths for REST service

#URI Read

@route('/stocks/api/v1.0/getStock', method='GET')
def get_document():
  ticker=request.query.ticker
  result = read_document(ticker)  
  return result

#URI Create
@post('/stocks/api/v1.0/createStock/')
def insert_document_document():
  newDoc = request.body.getvalue()
  newDoc = ast.literal_eval(newDoc) 
  create_document(newDoc)
  
@route('/stocks/api/v1.0/updateStock', method='GET')          #<-------------------
def modify_document():
  ticker=request.query.ticker
  target_field=request.query.target_field
  mod_value=request.query.mod_value
  update_document(ticker, target_field, mod_value)
  
@route('/stocks/api/v1.0/deleteStock', method='GET')
def remove_document():
  ticker=request.query.ticker
  delete_document(ticker
                 
                 
                 )

if __name__ == '__main__':	
	#app.run(debug=True)
	run(host='localhost', port=8080)