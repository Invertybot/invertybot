import os
import pymongo
import pandas as pd
from secret import generate_user_hash

class MongoManager():
    def __init__(self):
        mongo_user = os.environ['MONGO_USER']
        mongo_pass = os.environ['MONGO_PASS']
        dbname = 'invertybot'

        mongo_uri = f'mongodb://{mongo_user}:{mongo_pass}@cluster0-shard-00-00.payae.mongodb.net:27017,cluster0-shard-00-01.payae.mongodb.net:27017,cluster0-shard-00-02.payae.mongodb.net:27017/{dbname}?ssl=true&replicaSet=atlas-xfm6uc-shard-0&authSource=admin&retryWrites=true&w=majority'
        client = pymongo.MongoClient(mongo_uri)
        self.db = client[dbname]
        self.acounts = self.db.get_collection('accounts')

    def insert_account(self, user_id, df):
        user_hash = generate_user_hash(user_id)



