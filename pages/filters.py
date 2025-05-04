import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

symbols = ['ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BEL', 'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SHRIRAMFIN', 'SUNPHARMA', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'TRENT', 'ULTRACEMCO', 'WIPRO']

#database credentials
user = "root"
password = "%40Vicky143"
host = "localhost"
database = "stocks"

# create a engine
engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")


stocks=pd.DataFrame()
for symbol in symbols:
    query=f"select * from `{symbol}`"
    df=pd.read_sql(query,engine)
    stocks=pd.concat([stocks,df],axis=0)

# symbols dropdown
selected_symbols=st.multiselect("Symbols",symbols)

# month filter
months=stocks["month"].unique().tolist()
month=st.selectbox("month",months)

st.dataframe(stocks[(stocks["Ticker"].isin(selected_symbols) if len(selected_symbols) else True) & (stocks["month"]==month)])