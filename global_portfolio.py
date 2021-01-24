
from mongo_manager import MongoManager


class GlobalPortfolio:
    def __init__(self):
        self.mongo = MongoManager()
        self.accounts = None

    def compute_global_holdings(self, mode, month, year):
        self.accounts = self.mongo.get_global_portfolio(month, year)

        if mode == 'porcentaje':
            holdings = self.__compute_global_holdings_porcentaje()
        elif mode == 'value':
            holdings = self.__compute_global_holdings_value()

        return holdings

    def __compute_global_holdings_porcentaje(self):
        holdings = {}
        for account in self.accounts:
            print(account)
            for holding in account['holdings']:
                print(holding["ticker"], holding["weight"])
                if holdings.get(holding["ticker"]) is None:
                    holdings[holding["ticker"]] = holding["weight"] / len(self.accounts)
                else:
                    holdings[holding["ticker"]] += holding["weight"] / len(self.accounts)

        return holdings

    def __compute_global_holdings_value(self):
        holdings = {}
        for account in self.accounts:
            print(account)
            for holding in account['holdings']:
                print(holding["ticker"], holding["value"])
                if holdings.get(holding["ticker"]) is None:
                    holdings[holding["ticker"]] = holding["value"]
                else:
                    holdings[holding["ticker"]] += holding["value"]

        total_value = sum(holdings.values())
        for k in holdings.keys():
            holdings[k] = holdings[k] / total_value

        return holdings