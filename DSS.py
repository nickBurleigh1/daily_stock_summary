import json
from bson import json_util
from pymongo import MongoClient

#connection to localhost db market, collection stocks

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#50 moving average between low and high values
def avgRange(lowValue, highValue):
  
  thisList = []
  query = collection.find({"50-Day Simple Moving Average" : {'$lte' : highValue, '$gte' : lowValue}}, { "50-Day Simple Moving Average": 1, "Ticker": 1, "_id": 0 } )
  
  for doc in query:
    outDoc = json.dumps(doc, indent=4, default=json_util.default)
    thisList.append(outDoc)
    print outDoc
  
    
#Search by Industry
def searchByIndustry(industry):
  thisList = []
  query = collection.find({"Industry" : industry}, {"Industry" : 1, "Ticker" : 1, "_id": 0})
  
  for doc in query:
    outDoc = json.dumps(doc, indent=4, default=json_util.default)
    thisList.append(outDoc)
    return thisList

#input sector returns outstanding shares, util aggregation 
def outstandingSharesBySector(sector):
  query = collection.aggregate([{'$match' : {"Sector" : sector}}, {'$group' : {"_id" : "$Industry", "Shares Outstanding" : {'$sum' : 1}}}])
  
  for doc in query:
    outDoc = json.dumps(doc, indent=4, default=json_util.default)
    print outDoc
  return outDoc

#added getallstocksmargin
def getAllStocksMargin():
  thisList = []
  query = collection.find({'$all'}, {"Profit Margin"})
  
  for doc in query:
    outDoc = json.dumps(doc, indent=4, default=json_util.default)
    thisList.append(outDoc)
    return thisList
  
  
#added bubble sort
def bubbleSort(obj_list):
  has_swapped = True  
  total_iteration = 0  
  while(has_swapped):  
    has_swapped = False  
    for i in range(len(obj_list)-1):
          for j in range(0,len(obj_list)-1-i,1):
              if obj_list[j] > obj_list[j+1]:
                  obj_list[j], obj_list[j + 1] = obj_list[j + 1], obj_list[j]
                  has_swapped = True 

  return obj_list[0]
  
#added search by highest profitMargin
def getHighProfitMargin(profitMargin):
  for doc in collection.find({"Profit Margin" : profitMargin}):
      outDoc = json.dumps(doc, indent=4, default=json_util.default)
      print outDoc
      return outDoc


def top5ByIndustry(industry):
  thisList = []
  query = collection.aggregate([{'$match' : {"Industry" : industry}}, {'$sort' : {"P/E" : 1}}, {'$limit' : 5}])
  
  for doc in query:
    outDoc = json.dumps(doc, indent=4, default=json_util.default)
    print outDoc
    return outDoc
    




def get_user_choice():
    print("\n[1] Display 50-Day Simple Moving Average symbols between set range.")
    print("[2] Display Ticker symbols by Industry.")
    print("[3] Display Outstanding Shares by Sector grouped by Industry.")
    print("[4] Return most profitable company.")
    print("[q] Quit.")
    
    choice = ''
    choice = raw_input("Menu: ")
    return choice
  
def title_bar():              
    print("\t**********************************************")
    print("\t***  Daily Stock Summary  ***")
    print("\t**********************************************")  
    
    
    
def menu():
  title_bar()
  choice = ''
  
  
  while choice != 'q':
    
    choice = get_user_choice()
    print choice
    
    if choice == '1':
      lowValue = input("\nEnter the lowest average of the range: ")
      highValue = input("\nEnter the highest average of the range: ")
      print avgRange(lowValue, highValue)
   
    if choice == '2':
      industry = raw_input("\nEnter the industry you wish to view: ")
      print searchByIndustry(industry)
        
    if choice == '3':
      sector = raw_input("\nEnter the sector you wish to view: ")
      outstandingSharesBySector(sector)
       
    if choice == '4':
      objectList[] = getAllStocksMargin()
      top_earnings = bubbleSort(objectlist)
      print("The highest earnings are " + top_earnings)
      
      
    if choice == 'q':
        print("\nExiting Daily Stock Summary")
        
    else:
      print("\nInvalid Choice: Please choose function you wish to perform.\n")
        
