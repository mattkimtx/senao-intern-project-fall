from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
import os

load_dotenv()

# Create a connection with the MongoDB database
class mongoDB:
     def __init__(self):
          secret = os.environ.get("CONNECTION_STRING")
          self.client = MongoClient(host=secret, directconnection=True)
          self.db = self.client["cloud6_intern"]

     def get_collection(self, collection_name):     
          return self.db[collection_name]
     
     def close(self):
          self.client.close()

# checks to see if the username exists in the database
def user_exists(username, mongo):
     db = mongo
     user_col = db.get_collection('users')
     account = user_col.find_one({"user": username})
     db.close()
     if account == None:
          return False
     else:
          return True
     
# creates the new account
def create_account(username, password):
     db = mongoDB()
     user_col = db.get_collection('users')
     user_col.insert_one({"user": username, "password": password})
     db.close()
     # checks to make sure account was created
     if user_exists(username, db):
          return True
     else:
          return False
     
# Counts failed login attempts
def failed_login(username, timestamp, mongo):
     db = mongo
     # get both collections from the database
     fail_col = db.get_collection('failed_login')
     # get account and update the failed login
     fail_col.insert_one({"user": username, "timestamp": timestamp})
     # compare times

     db.close()

# flaw in design, it uses timezone of the user. what happens when 2+ people with same account log in from different timezones?
def check_failed_login_attempts(username, timestamp, mongo):
     counter = 0
     login_attempt_duration = timedelta(minutes=1)

     db = mongo
     fail_col = db.get_collection('failed_login')
     # a list of failed attempts
     attempts = fail_col.find({"user": username})
     for attempt in attempts:
          # if there have already been too many attempts
          if counter >= 5:
               db.close()
               return False
          # if the timestamp is within 1 minute of the current time, add to counter
          if (timestamp - attempt["timestamp"]) < login_attempt_duration:
               counter += 1
     db.close()
     return True

# Verifies login information
def verify(username, password, timestamp):
     db = mongoDB()
     user_col = db.get_collection('users')
     account = user_col.find_one({"user": username})
     db.close()
     if account == None:
          return 1
     else:
          # if logged in too many times
          if check_failed_login_attempts(username, timestamp, db) == False:
               return 2 # 2 as in 2 many failed login attempts lol
          # successful login
          if account["password"] == password:
               return 0
          # failed to login, will add another failed login to counter
          else:
               failed_login(username, timestamp, db)
               return 1
          
