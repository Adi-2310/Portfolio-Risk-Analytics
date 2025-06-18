import yfinance as yf

def fetch_data(tickers, start_date, end_date):

    df = yf.download(tickers,start=start_date, end= end_date)
    
    # if isinstance(tickers,list) and len(tickers)>1:
    #     adj_close = df.xs('Adj Close',axis=1,level=0)
    
    # else:
    #     adj_close = df[['Adj Close']]
    #     adj_close.columns = [tickers]
    adj_close = df['Close']
    return adj_close.dropna()




