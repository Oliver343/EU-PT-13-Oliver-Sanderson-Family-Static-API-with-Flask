"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

class Member:
  def __init__(self, first_name, age, lucky_numbers, id=None):
    self.first_name = first_name
    self.age = age
    self.lucky_numbers = lucky_numbers
    self.id = id or None

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

john_jackson = Member("John", 33, [7, 13, 22])
jackson_family.add_member(john_jackson)

jane_jackson = Member("Jane", 35, [10, 14, 3])
jackson_family.add_member(jane_jackson)

jimmy_jackson = Member("Jimmy", 5, [1])
jackson_family.add_member(jimmy_jackson)





# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET', 'DELETE'])
def handle_get_member(id):
    if request.method == "GET":
        member_old = jackson_family.get_member(int(id))
        # member = {"name": member_old[0]["first_name"] + " " + member_old[0]["last_name"], "id": member_old[0]["id"], "age": member_old[0]["age"], "lucky_numbers": member_old[0]["lucky_numbers"]}
        response_body = {
            "member": member_old
        }
    if request.method == "DELETE":
        jackson_family.delete_member(int(id))
        response_body = {
            "done": True
        }
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def handle_new_member():
    recieved_data = request.get_json()
    print(recieved_data["id"])
    if 'id' in recieved_data:
        id_to_use = recieved_data["id"]
    else:
        id_to_use = None
    new_member = Member(recieved_data["first_name"], recieved_data["age"], recieved_data["lucky_numbers"], id_to_use)
    jackson_family.add_member(new_member)
    response_body = {
        "message": "Member added"
    }
    return jsonify(response_body), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
