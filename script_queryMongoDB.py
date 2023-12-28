from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient(host=f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}/{mongo_db_name}?authSource=cloud6_intern', directconnection=True)

# test database connection
print(client.list_database_names())
all_db = client.list_database_names()

for db in all_db:
     database = client.db # not just the name but includes all of the collection info
     
