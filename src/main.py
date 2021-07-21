from flask import Flask, jsonify, request, make_response
from flask.helpers import make_response
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from password import db_pass

app = Flask(__name__)
api = Api(app)

db_name = 'user_db'
app.config["MONGODB_HOST"] = "mongodb+srv://admin:{}@cluster0.o4tig.mongodb.net/{}?retryWrites=true&w=majority".format(db_pass, db_name)

db = MongoEngine(app)

class Interest(db.EmbeddedDocument):
    # _id = db.IntField()
    name = db.StringField()
    priority = db.StringField()

class users(db.Document):
    # _id = db.IntField()
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    age = db.IntField()
    interest = db.EmbeddedDocumentListField(Interest)

    def to_json(self):
        return({
            "_id": self._id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "age": self.age,
            "interest": self.interest
        })

@app.route("/user", methods=["GET", "POST"])
def CRUser():
    # READ all users
    if request.method == "GET":
        data = users.objects()
        return make_response(jsonify(data), 201)
    # CREATE new user
    elif request.method == "POST":
        body = request.get_json()
        data = users(**body).save()
        return make_response(jsonify(data), 201)

@app.route("/user/<id>", methods=["GET", "PUT", "DELETE"])
def RUDUser(id:str):
    # READ user with id
    if request.method == "GET":
        data = users.objects(id=id)
        return make_response(jsonify(data), 201)

    # UPDATE user with id
    elif request.method == "PUT":
        body = request.get_json()
        data = users.objects(id=id)
        if data:
            data.update(**body)
            return make_response(jsonify(data), 201)
        else:
            return make_response(jsonify({"error":"User with id =" + id + "not found"}), 404)
    
    # DELETE user with id
    elif request.method == "DELETE":
        data = users.objects(id=id)
        if data:
            data.delete()
            return make_response(jsonify({"message":"User with id =" + id + "was deleted"}), 201)
        else:
            return make_response(jsonify({"error":"User with id =" + id + "not found"}), 404)

if __name__ == '__main__':
    app.run(debug=True)