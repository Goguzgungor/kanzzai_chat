from flask import abort
from pymongo import MongoClient

class DBService:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_data(self, wallet_address):
        data = self.collection.find_one({"wallet_address": wallet_address})
        if data:
            return data
        else:
            abort(404, description="Wallet address not found")