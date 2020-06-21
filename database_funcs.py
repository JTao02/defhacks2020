from pymongo import MongoClient

client = MongoClient("mongodb+srv://test_user:test123@defhacks2020.snfxf.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["Data"]
collection = db["API"]


def getQueueETA(address):
    lookUp = client["Data"]["API"]
    a = lookUp.find_one({"address": address})
    if not a:
        return None
    else:
        return a[address]

def updateDatabase(query:dict):
    address = query["address"]
    queue = query[address][0]
    ETA = query[address][1]
    stats = [queue, ETA]

    lookUp = client["Data"]["API"]
    a = lookUp.find_one({"address": address})
    if not a:
        entry = {
            "address": address,
            address  : stats
        }
        collection.insert_one(entry)
    else:
        collection.update_one(
            {"address": address},
            { '$set': {address: stats}, }
        )
