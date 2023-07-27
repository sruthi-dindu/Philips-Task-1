from pymongo import MongoClient
from bson.binary import Binary

client = MongoClient("mongodb://localhost:27017/")
db = client["consent_forms"]
cf_database = db["Consentform"]


def add_consentform(arr,link,bi):
    #bi = ['participant_name', 'investigator_name','date', 'relationship']
    with open(link, 'rb') as image_file:
        image_data = image_file.read()
    query={}
    for i in range(len(arr)):
        query.update({bi[i]: arr[i]})
    print(query)
    query.update({'image': Binary(image_data)})
    cf_database.insert_one(query)
    return ("Added consent form successfully.")
    

    

