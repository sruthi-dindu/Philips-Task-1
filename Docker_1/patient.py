"""
    This file will contains the basic operation like connecting to the sql and working on that
    It will have all the CRUD operations

"""

#importing required libraries
from settings import *
import json


#starting the Database
db = SQLAlchemy(app)

#createa class which inherit the properties of sqlalchemy
#This is a patient details table
#This table will have 4 columns
#ID(Primary Key), Name, Age, Diagnosis

class Patient(db.Model):
    #Create a table
    __tablename__ = 'patient'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    age = db.Column(db.Integer, nullable=False)
    diagnosis = db.Column(db.String(80), nullable=False)

    #write some code to convert our output to JSON format
    def json(self):
        return {'id' : self.id, 'name' : self.name, 'age' : self.age, 'diagnosis' : self.diagnosis}


    #write functions to do CRUD operatons
    #Write a function which will add new patient record
    def add_patient(_name, _age, _diagnosis):
        # function to add patients to database
        new_patient = Patient(name=_name, age=_age, diagnosis=_diagnosis)
        db.session.add(new_patient)  # add new patient to database session
        db.session.commit()  # commit changes to session

    #Write a function to fetch all the patients
    def get_all_patients():
        return [Patient.json(pat) for pat in Patient.query.all()]

    #Write a function to get the patient details based on id
    def get_patient(_id):
        return [Patient.json(Patient.query.filter_by(id=_id).first())]

    '''#Write a function to get the patient details based on name
    def get_patient(_name):
        return [Patient.json(Patient.query.filter_by(name=_name).first())]'''

    #Write a function to update any record
    def update_patient(_id, _name, _age , _diagnosis):
        patient_to_update = Patient.query.filter_by(id=_id).first()
        patient_to_update.name = _name
        patient_to_update.age = _age
        patient_to_update.diagnosis = _diagnosis
        db.session.commit()

    #Write a function to delete any record
    def delete_patient(_id):
        Patient.query.filter_by(id=_id).delete()
        db.session.commit()
        

