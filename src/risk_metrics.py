
def calculate_daily_returns(price_df):
    return price_df.pct_change().dropna()

def calculate_annualised_volatility(returns):
    return returns.std()*(252**0.5)

def calculate_var(returns, confidence_level=0.95):
    return returns.quantile(1 - confidence_level)

def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate / 252
    return (excess_returns.mean() * 252) / (excess_returns.std() * (252 ** 0.5))
