from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Create a connection with the MongoDB database
class mongoDB:
     def __init__(self):
          secret = os.environ.get("CONNECTION_STRING")
          self.client = MongoClient(host=secret, directconnection=True)
          self.db = self.client["cloud6_intern"]
          self.collection = self.db["users"]

def create_account(user, pw):
     try:
          # Create mongoDB class and set a variable equal to the user collection, which creates a connection to the database
          db = mongoDB()
          user_col = db.collection
          # document to add to collection
          new_account = {"user": user, "pw" : pw}

          # check if document already exists
          account = user_col.find_one({"user": user})
          if account:
               return account
          
          db.collection.insert_one(new_account)
          # Return the new account
          return account
     except Exception as e:
          # Handle exceptions (e.g., connection errors)
          raise Http404("No data found")
          # return render(request, 'network/error.html', {'error_message': str(e)})