from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
collection = db["blueprint"]
bi=['participant_name', 'expected_participant_name', 'investigator_name', 'expected_investigator_name', 'date', 'expected_date', 'relationship', 'expected_relationship']
def add_blueprint(arr,bp_num):
    query={}
    query.update({"metadata": arr})
    query.update({"bp_num": bp_num})
    collection.insert_one(query)
    return ("Added blueprint successfully.")
    
def delete_blueprint(arr):
    collection.delete_one(arr)
    return("Deleted blueprint successfully.")

