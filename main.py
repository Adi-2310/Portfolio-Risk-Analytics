from src.utils import fetch_data
from src.risk_metrics import *
from src.visualisations import *
from src.portfolio_metrics import calculate_portfolio_metrics,simulate_stress_test
import numpy as np
import pandas as pd


tickers = ["AAPL","GOOGL","MSFT"]
weights = [0.4,0.3,0.3]

# GETTING CLOSING PRICE DATA
adj_data = fetch_data(tickers,"2023-01-01", "2024-01-01")
print(adj_data.head())

print("##############")

# CALCULATING DAILY RETURNS
returns = calculate_daily_returns(adj_data)
print(returns.head())

print("##############")

# CALCULATING VOLATILITY
vol = calculate_annualised_volatility(returns)
var = calculate_var(returns)
sharpe = calculate_sharpe_ratio(returns)

print("Annualized Volatility:\n", vol)
print("Value at Risk (95%):\n", var)
print("Sharpe Ratio:\n", sharpe)

print("##############")

# PLOTTING

plot_returns(returns)
plot_correlation_heatmap(returns)
plot_var_histogram(returns['AAPL'], var['AAPL'])  # For one stock

print("##############")

# PORTFOLIO RETURNS

port_return, port_volatility, sharpe_rat =calculate_portfolio_metrics(returns,weights)

print("Portfolio returns = ",round(port_return,4))
print("Portfolio volatility = ",port_volatility)
print("Sharpe ratio = ",sharpe_rat)  # Sharpe ratio for the portfolio

# STRESS TEST 
print("##############")

ticker_shock = 'AAPL'
shock_value = -0.10

sim_returns, shocked_portfolio_return = simulate_stress_test(returns,weights,ticker_shock,shock_value)
print("Simulated returns", sim_returns)
print("New portfolio return ",shocked_portfolio_return)  # Portfolio return under stress test

latest_actual_return = np.dot(returns.iloc[-1],weights)
print("Latest actual return ",latest_actual_return)  # Latest actual return of the portfolio

# Combine all metrics into one dataframe
summary_df = pd.DataFrame({
    "Annualised volatility" : vol,
    "Value at Risk (95%) ": var,
    "Sharpe Ratio" : sharpe,
})

summary_df.to_csv("outputs/risk_metrics.csv")