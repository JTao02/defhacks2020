import Credentials
from pymongo import MongoClient

client = MongoClient(f"mongodb+srv://Admin:{Credentials.password}@defhacks2020.snfxf.mongodb.net/DefHacks2020?retryWrites=true&w=majority")
db = client["User_data"]
collection = db["User stuff"]

entry = {"name": "Stephen", "Location": "Ottawa"}

collection.insert_one(entry)

