import requests


class YahooFinance():
    def __init__(self):
        self.api_url = "https://query2.finance.yahoo.com/v1/finance/search"

    def get_ticker(self, isin):
        r = requests.get(f"{self.api_url}?q={isin}")
        try:
            if type(isin) is float:
                ticker = 'EUR (cash)'
            else:
                ticker = r.json()['quotes'][0]['symbol']
        except Exception as e:
            print(e)
            ticker = isin
        return ticker
