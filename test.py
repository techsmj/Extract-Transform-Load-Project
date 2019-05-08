import pymongo


# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.food_db1
#collection = db.food_collection
collection2 = db.food_collection


#food = list(db.collection2.find())
print(list(collection2.find()))
