import os
import pymongo
import pandas as pd
from secret import generate_user_hash
from datetime import datetime
from settings import MONGO_USER, MONGO_PASS

class Holding():
    def __init__(self, isin, product, ticker, quantity, weight, value):
        self.isin = isin
        self.product = product
        self.ticker = ticker
        self.quantity = quantity
        self.weight = weight
        self.value = value

    def to_dict(self):
        h = {
            "isin": self.isin,
            "product": self.product,
            "ticker": self.ticker,
            "quantity": self.quantity,
            "weight": self.weight,
            "value": self.value
        }
        return h


class MongoManager():
    def __init__(self):
        mongo_user = MONGO_USER
        mongo_pass = MONGO_PASS
        dbname = 'invertybot'

        mongo_uri = f"mongodb://{mongo_user}:{mongo_pass}@cluster0-shard-00-00.payae.mongodb.net:27017,cluster0-shard-00-01.payae.mongodb.net:27017,cluster0-shard-00-02.payae.mongodb.net:27017/{dbname}?ssl=true&replicaSet=atlas-xfm6uc-shard-0&authSource=admin&retryWrites=true&w=majority"
        client = pymongo.MongoClient(mongo_uri)
        self.db = client[dbname]
        self.acounts = self.db.get_collection('accounts')

    def insert_account(self, user_id, df):
        user_hash = generate_user_hash(user_id)

        month = datetime.now().month
        year = datetime.now().year

        holdings = []
        for row in df.iloc:
            h = Holding(
                isin=row['Symbol/ISIN'],
                product=row['Producto'],
                ticker=row['Ticker'],
                quantity=row['Cantidad'],
                weight=row['Peso'],
                value=row['Valor en EUR'],
            )
            holdings.append(h.to_dict())
            print(h.to_dict())

        positions = {
            "user_hash": user_hash,
            "month": month,
            "year": year,
            "holdings": holdings
        }

        self.acounts.update({
            'user_hash': user_hash,
            'month': month,
            'year': year
        }, {
            '$set': positions
        }, upsert=True)

    def get_global_portfolio(self, month, year):
        accounts = list(self.acounts.find({"month": month, "year": year}))
        return accounts



if __name__ == "__main__":
    MongoManager()
    MongoManager().acounts.find({})
    accounts = list(MongoManager().acounts.find({"month": 1, "year": 2021}))

    holdings = {}
    for account in accounts:
        print(account)
        for holding in account['holdings']:
            print(holding["ticker"], holding["value"])
            if holdings.get(holding["ticker"]) is None:
                holdings[holding["ticker"]] = holding["value"]
            else:
                holdings[holding["ticker"]] += holding["value"]

    print(holdings)
    total_value = sum(holdings.values())
    for k in holdings.keys():
        holdings[k] = holdings[k] / total_value
    print(holdings)

    holdings = {}
    for account in accounts:
        print(account)
        for holding in account['holdings']:
            print(holding["ticker"], holding["weight"])
            if holdings.get(holding["ticker"]) is None:
                holdings[holding["ticker"]] = holding["weight"] / len(accounts)
            else:
                holdings[holding["ticker"]] += holding["weight"] / len(accounts)
    print(holdings)