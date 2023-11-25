import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database
db = client["myDatabase"]

# Create a collection
collection = db["myCollection"]

d = {"name": 'eli', 'age': 20}
collection.insert_one(d)
