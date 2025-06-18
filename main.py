from src.utils import fetch_data
from src.risk_metrics import *
from src.visualisations import *

# GETTING CLOSING PRICE DATA
adj_data = fetch_data(["AAPL","GOOGL","MSFT"],"2023-01-01", "2024-01-01")
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
# plot_var_histogram(returns['AAPL'], var['AAPL'])  # For one stock


