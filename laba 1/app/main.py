from flask import Flask, jsonify, request
from datetime import date 

application = Flask(__name__)

class PhoneNumber:
    def __init__(self, type_code: int, country_prefix: int, provider: int, digits: int):
        self.type_code = type_code
        self.country_prefix = country_prefix
        self.provider = provider
        self.digits = digits

    def serialize(self):
        return {
            "TypeID": self.type_code,
            "CountryCode": self.country_prefix,
            "Operator": self.provider,
            "Number": self.digits
        }
    
class Person:
    def __init__(self, uid: int, nickname: str, first_name: str, last_name: str, 
                 mobile: PhoneNumber, mail: str, birth_date: date):
        self.uid = uid
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.mail = mail
        self.birth_date = birth_date
    
    def to_dict(self):
        return {
            "ID": self.uid,
            "Username": self.nickname,
            "GivenName": self.first_name,
            "FamilyName": self.last_name,
            "Phone": self.mobile.serialize(),
            "Email": self.mail,
            "Birthday": self.birth_date
        }
    
class ContactGroup:
    def __init__(self, gid: id, name: str, details: str, members_count: int):
        self.gid = gid
        self.name = name
        self.details = details
        self.members_count = members_count

    def as_json(self):
        return {
            "ID": self.gid,
            "Title": self.name,
            "Description": self.details,
            "Contacts": self.members_count
        }
    
@application.route("/api/v1/contact", methods=["POST"])
def add_contact():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/contact", methods=["GET"])
def fetch_contact():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/contact", methods=["PUT"])
def modify_contact():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/contact", methods=["DELETE"])
def remove_contact():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/group", methods=["POST"])
def make_group():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/group", methods=["GET"])
def retrieve_group():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/group", methods=["PUT"])
def change_group():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())

@application.route("/api/v1/group", methods=["DELETE"])
def erase_group():
    sample_data = Person(1, "Linga", "Nguli", "Guliguli", 
                        PhoneNumber(1, 4, 6, 9), "Vatalin", "2052-01-19")
    return jsonify(sample_data.to_dict())


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=6080)