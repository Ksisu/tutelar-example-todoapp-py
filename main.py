from flask import Flask, request, jsonify
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient
import os
import jwt

version = os.getenv("VERSION", "DEV")
jwt_secret = os.getenv("TOKEN", "secret")
mongo_uri = os.getenv("DB_URI", "mongodb://localhost/todoapp")

mongo_client = MongoClient(mongo_uri)
database = mongo_client.get_default_database()
todo_collection = database.todos

app = Flask(__name__)
CORS(app)


def db_list(user_id):
    doc = todo_collection.find_one({"userId": user_id})
    if doc is None:
        return []
    else:
        return doc['todos']


def db_remove(user_id, idx):
    todo_collection.update_one({"userId": user_id}, {"$unset": {"todos." + idx: 1}})
    todo_collection.update_one({"userId": user_id}, {"$pull": {"todos": None}})


def db_update(user_id, idx, data):
    todo_collection.update_one({"userId": user_id}, {"$set": {"todos." + idx: data}})


def db_add(user_id, data):
    res = todo_collection.update_one({"userId": user_id}, {"$push": {"todos": data}})
    if res.matched_count is 0:
        todo_collection.insert_one({"userId": user_id, "todos": [data]})


def decode_token(auth_token):
    payload = jwt.decode(auth_token, jwt_secret)
    return payload['id']


def get_todo_from_request():
    data = request.get_json()
    return {"title": data['title'], "done": data['done']}


def authenticate():
    return decode_token(request.headers.get('Authorization').split()[1])


@app.route("/api/healthCheck")
def health_check():
    return jsonify({"success": True, "version": version})


@app.route("/api/todo")
def list_todo():
    try:
        userid = authenticate()
        return jsonify(db_list(userid))
    except:
        return "UNAUTHORIZED\n", 401


@app.route("/api/todo", methods=['POST'])
def create_todo():
    try:
        userid = authenticate()
        item = get_todo_from_request()
        db_add(userid, item)
        return jsonify({})
    except:
        return "UNAUTHORIZED\n", 401


@app.route("/api/todo/<idx>", methods=['POST'])
def update_todo(idx):
    try:
        userid = authenticate()
        item = get_todo_from_request()
        db_update(userid, idx, item)
        return jsonify({})
    except:
        return "UNAUTHORIZED\n", 401


@app.route("/api/todo/<idx>/delete", methods=['POST'])
def delete_todo(idx):
    try:
        userid = authenticate()
        db_remove(userid, idx)
        return jsonify({})
    except:
        return "UNAUTHORIZED\n", 401


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
