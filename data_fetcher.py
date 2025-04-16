import yfinance as yf
from datetime import date, timedelta
import pandas as pd

def fetch_stock_data(ticker, days_back=720, end_date=None):
    """Fetch stock data from Yahoo Finance"""
    end_date = end_date or date.today()
    start_date = end_date - timedelta(days=days_back)
    
    try:
        data = yf.download(
            ticker, 
            start=start_date, 
            end=end_date, 
            progress=False, 
            repair=True
        )
        # Flatten MultiIndex columns if needed
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = ['_'.join(col).strip() for col in data.columns.values]
        return data
    except Exception as e:
        print(f"Download failed: {e}")
        return None