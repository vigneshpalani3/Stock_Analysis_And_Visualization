import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# database credentials
user = "root"
password = "%40Vicky143"
host = "localhost"
database = "stocks"

# create a engine
engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# Header
st.title("Stock analysis")
st.header("Home")

# dropdown menu
option=st.selectbox("Select an option", ("Top 10 gainers and losers","Red & Green stocks count,average price and average volume","Top 10 most volatile stocks","Top 5 performing stocks over the year","Sector wise performance","stock price correlation","monthly gainers and loosers"))
symbols = ['ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BEL', 'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SHRIRAMFIN', 'SUNPHARMA', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'TRENT', 'ULTRACEMCO', 'WIPRO']

st.write('')

def cut_symbol(symbol):
    return symbol.split(': ')[1]

def show_gainers_loosers():
    # 1. Top 10 gainers and losers by yearly returns
    query = "SELECT * FROM yearly_returns ORDER BY yearly_returns DESC"
    df=pd.read_sql(query,engine)
    st.subheader("Top 10 gainers")
    st.dataframe(df.head(10))
    # bar chart of top 10 gainers
    st.bar_chart(df.head(10).set_index('symbol')["yearly_returns"])

    st.subheader("Top 10 losers")
    st.dataframe(df.tail(10))
    # bar chart of top 10 losers
    st.bar_chart(df.tail(10).set_index('symbol')["yearly_returns"])
def calc_statistics():
    # 2.Red & Green stocks count,average price and average volume
    query = "SELECT * FROM yearly_returns ORDER BY yearly_returns DESC"
    df=pd.read_sql(query,engine)
    st.write("Green and Red stocks count")
    st.table({
        "Green stocks":df[df["yearly_returns"]>0].shape[0],
        "Red stocks":df[df["yearly_returns"]<=0].shape[0],
        })
    
    # average price and volume
    values_df=pd.DataFrame()
    for symbol in symbols:
        query = f"select round(avg(close),2) as average_price,round(avg(volume),2) as average_volume from `{symbol}`"
        df=pd.read_sql(query,engine)
        values_df=pd.concat([values_df,df],axis=0)
    
    st.write("Average price and volume")
    st.dataframe(np.round(values_df.mean(),2))

def calc_volatility():
    # 3.Top 10 most volatile stocks
    volatility=[]
    for symbol in symbols:
        query=f"SELECT daily_returns FROM `{symbol}`"
        df=pd.read_sql(query,engine)
        volatility.append({"symbol":symbol,"volatility":df.std()[0]})
    volatility_df=pd.DataFrame(volatility).sort_values(by="volatility",ascending=False).head(10)
    st.write('')
    st.bar_chart(volatility_df.set_index("symbol"))

def yearly_performance():
    # 4.Top 5 performing stocks over the year
    yearly_perf_df=pd.DataFrame()
    top_5=None
    for symbol in symbols:
        query=f"select ticker as symbol,cumulative_returns from `{symbol}` order by date desc limit 1;"
        df=pd.read_sql(query,engine)
        yearly_perf_df=pd.concat([yearly_perf_df,df],ignore_index=True,axis=0)
    top_5=yearly_perf_df.sort_values(by="cumulative_returns",ascending=False).head(5)

    # plots for best performing stocks

    # fig,(ax1,ax2,ax3,ax4,ax5,ax6)=plt.subplots(3,2,figsize=(6,6))
    for symbol in top_5["symbol"]:
        df=pd.read_sql(f"select cumulative_returns from `{symbol}`",engine)
        st.subheader(symbol)
        st.line_chart(df)

def sector_wise_performance():
    # show the performence of the sectors
    df=pd.read_sql("select symbol,round(yearly_returns,3) as yearly_returns from yearly_returns",engine)
    sectors_df=pd.read_csv('Sector_data.csv')
    sectors_df["Symbol"]=sectors_df["Symbol"].apply(cut_symbol)
    # merge both yearly returns and sectors dataframe 
    merged_df=pd.merge(sectors_df,df,left_on="Symbol",right_on="symbol",how="inner")
    merged_df.drop('Symbol',axis=1,inplace=True)
    sector_perf=merged_df.groupby("sector")['yearly_returns'].mean()
    st.bar_chart(sector_perf)

def stocks_correlation():
    #show the correlation between stocks
    price_df=pd.DataFrame()
    for symbol in symbols:
        query=f'select close from `{symbol}`'
        df=pd.read_sql(query,engine)
        price_df[symbol]=df
    price_df=price_df.pct_change()
    
    # Correlation
    corr=price_df.corr()
   
    # heatplot
    fig,ax=plt.subplots()
    sns.heatmap(corr,ax=ax)
    st.pyplot(fig)

def monthly_performance():
    monthly_returns=[]
    for symbol in symbols:
        query=f"select date,month,close from `{symbol}` order by date"
        df=pd.read_sql(query,engine)
        grouped = df.groupby('month')

        for month,group in grouped:
            first=group["close"].iloc[0]
            last=group["close"].iloc[-1]
            returns=((last-first)/first)*100
            monthly_returns.append({"symbol":symbol,"month":month,"monthly_returns":returns})
    returns_df=pd.DataFrame(monthly_returns)

    months=returns_df["month"].unique()


    for i,month in enumerate(months):
        month_wise_df=returns_df[returns_df["month"]==month]
        month_wise_df=month_wise_df.sort_values(by="monthly_returns",ascending=False)
        top5=month_wise_df.head(5)
        bottom5=month_wise_df.tail(5)
        conc=pd.concat([top5,bottom5])

        fig,ax=plt.subplots()
        sns.barplot(data=conc,x="symbol",y="monthly_returns",ax=ax,palette=['red' if x<=0 else 'green' for x in conc["monthly_returns"]])
        plt.tight_layout()
        ax.set_title(month)
        ax.tick_params(axis="x",rotation=45,labelsize=7)
        st.pyplot(fig)

if option == "Top 10 gainers and losers":
    show_gainers_loosers()

elif option=="Red & Green stocks count,average price and average volume":
    calc_statistics()

elif option=="Top 10 most volatile stocks":
    calc_volatility()

elif option=="Top 5 performing stocks over the year":
    yearly_performance()

elif option=="Sector wise performance":
    sector_wise_performance()

elif option=="stock price correlation":
    stocks_correlation()

elif option=="monthly gainers and loosers":
    monthly_performance()