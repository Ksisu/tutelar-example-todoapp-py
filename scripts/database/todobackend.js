db.getSiblingDB("todoapp");
db.createCollection("todos");
db.users.createIndex({"userid": 1}, {"unique": true});
