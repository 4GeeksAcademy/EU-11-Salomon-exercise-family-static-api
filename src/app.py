"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, abort
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    if not members:
        return errormessage, 400
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(response_body), 200  # Status code 200 for success

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member():
    member = jackson_family.get_member()
    if not member:
        return errormessage, 400
    response_body = {
        "id": self._generateId(),
        "first_name": String,
        "age": Int,
        "lucky_numbers": List
    }
    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def add_member():
    addmember = jackson_family.add_member()
    if not addmember:
        return errormessage, 400
    response_body = {
        first_name: String,
        age: Int,
        lucky_numbers: [],
        id:  Int *optional
    }
    return jsonify(), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member():
    deletemember = jackson_family.delete_member()
    if not deletemember:
        return errormessage, 400
    response_body = {
        done: True
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
