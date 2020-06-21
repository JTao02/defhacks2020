from pymongo import MongoClient

client = MongoClient("mongodb+srv://test_user:test123@defhacks2020.snfxf.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["Data"]
collection = db["User_stuff"]

entry = {"name": "Stephen", "Location": "Ottawa"}

collection.insert_one(entry)

