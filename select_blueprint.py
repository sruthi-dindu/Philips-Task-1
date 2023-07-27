from pymongo import MongoClient
from bson.binary import Binary

client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
cf_database = db["blueprint"]


def select_blueprint(bp_num):
    query = { 'bp_num': { '$eq': bp_num } }
    function = list(cf_database.find(query))
    for i in function:
        # Function name stored in a variable
        function_name = i['function']
        return function_name

        

