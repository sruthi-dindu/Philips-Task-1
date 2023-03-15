"""
    This file is to test the created api
"""
#import the required packages
import requests
import json

#import everything from patient and api module
from patient import *
from api import *

#Write a function which will get all the data from the table
def getReq(url):
    try:
        res = requests.get(url)
        return json.dumps(res.json(),indent=4)
    except Exception as ee:
        return f"Message : {ee}"
	
#Write a function which will create a new patient record            
def postReq(url, data):
    try:
        res = requests.post(url, json=data)
        return("New Patient added")
    except Exception as er:
        return f"Message : {er}"

#Write a function which will update the existing patient
def putReq(url, data):
    try:
        res = requests.put(url , json=data)
        return("Patient updated")
    except Exception as er:
        return f"Message : {er}"

#Write a function which will delete the patient
def delReq(url):
    try:
        res = requests.delete(url)
        return("Patient deleted")
    except Exception as er:
        return f"Message : {er}"
    
    
if __name__ == '__main__':
    while True:
        try:
            choice = int(input("1.Fetch all the Patient \n2.Create new Patient \n3.Update Existing Patient \n4.delete Existing Patient \n5.Exit\nEnter Choice : "))
            if choice == 1:
                url_inp = "http://127.0.0.1:1234/patient"
                print(getReq(url_inp))
                
            elif choice == 2:
                url_inp = "http://127.0.0.1:1234/patient/post"
                print("enter the values")
                data_inp = { "name" : input("name : "), "age" : int(input("age : ")), "diagnosis" : input("diagnosis : ")}
                print(postReq(url_inp, data_inp))
                
            elif choice == 3:
                ID = (input("Enter the ID of the patient to be updated : "))
                url_inp = "http://127.0.0.1:1234/patient/update/"+ID                
                print("enter the values")
                data_inp = { "name" : input("name : "), "age" : int(input("age : ")), "diagnosis" : input("diagnosis : ")}
                print(putReq(url_inp, data_inp))

            elif choice == 4:
                ID = (input("Enter the ID of the patient to be deleted : "))
                url_inp = "http://127.0.0.1:1234/patient/delete/"+ID                
                print(delReq(url_inp))

            elif choice == 5:
                exit(0)
        except Exception as e:
            print("Error : ", e)

			
