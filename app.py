import pymongo

client = pymongo.MongoClient('mongodb+srv://Eli:CXtvUDJNR2BZJLi@cluster0.1xtkxye.mongodb.net/')

# Create a database
db = client["inventory"]

# Create a collection
collection = db["myCollection"]


def connect(name, picture, amount):
    # Connect to MongoDB

    d = {"name": name, 'picture': picture, 'amount': amount}
    collection.insert_one(d)


def show():
    data = collection.find()
    return data


print(show())
