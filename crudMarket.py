import json
from bson import json_util
from pymongo import MongoClient
import pprint

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def insert_document(document):
  result = collection.save(document)
  print "Inserting New Document!"
  return result


def read_document(value):
  for doc in collection.find({"business_name" : value}):
    return json.loads(json.dumps(doc, indent=4, default=json_util.default))



def update_document(document_id, mod_value):
  myquery = { "id": document_id }
  newvalues = { "$set": { "result" : mod_value } }
  result = collection.update_one(myquery, newvalues)
  return result


def delete_document(document_id):
  myquery = { "id": document_id }
  result = collection.delete_one(myquery)
  return result
 

def main():
  print "Started"
 
  
main()
