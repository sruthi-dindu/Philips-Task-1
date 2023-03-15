"""
    This file will have the rest api methods whic will tell about the route
    Simply it tells about which url is used for which process
"""


from patient import * #import everything from patient module

#get all the patients
@app.route('/patient', methods=['GET'])
def get_patients():
    return jsonify({'Patients': Patient.get_all_patients()})

#get movie by id
@app.route('/patient/<int:id>', methods=['GET'])
def get_patient_by_id(id):
    return_value = Patient.get_patient(id)
    return jsonify(return_value)

#add new patient
@app.route('/patient/post', methods=['POST'])
def add_patient():
    request_data = request.get_json()  # getting data from client
    Patient.add_patient(request_data["name"], request_data["age"],request_data["diagnosis"])
    response = Response("Patient added", 201, mimetype='application/json')
    return response

#Update the existing patient
@app.route('/patient/update/<int:id>', methods=['PUT'])
def update_patient(id):
    request_data = request.get_json()
    Patient.update_patient(id, request_data["name"], request_data["age"],request_data["diagnosis"])
    response = Response("Patient Updated", status=200, mimetype='application/json')
    return response

#Delete the existing patient
@app.route('/patient/delete/<int:id>', methods=['DELETE'])
def delete_patient(id):
    Patient.delete_patient(id)
    response = Response("Patient Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)

#http://127.0.0.1:1234/patient
