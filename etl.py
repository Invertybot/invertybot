
import pandas as pd
from yahoo_finance import YahooFinance

yf = YahooFinance()


class ETL:
    @classmethod
    def preprocess_data(cls, df):
        df['Ticker'] = df['Symbol/ISIN'].apply(yf.get_ticker)
        total_value = sum(df['Valor en EUR'])
        df['Peso'] = df['Valor en EUR'] / total_value

        return df
