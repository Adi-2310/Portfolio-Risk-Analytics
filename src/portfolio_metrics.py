import numpy as np
import pandas as pd

def calculate_portfolio_metrics(returns_df, weights, risk_free_rate=0.0):
    weights = np.array(weights)
    mean_returns = returns_df.mean()
    cov_matrix = returns_df.cov()

    port_return = np.dot(mean_returns,weights) * 252
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))

    sharpe_ratio = (port_return - risk_free_rate) / port_volatility

    return port_return, port_volatility, sharpe_ratio



def simulate_stress_test(returns_df, weights, ticker_to_shock, shock_percent):

    ''' Simulate a 1 day shock '''

    simulated_returns = returns_df.iloc[-1].copy()

    simulated_returns[ticker_to_shock] += shock_percent

    weights = np.array(weights)
    new_portfolio_return = np.dot(simulated_returns,weights)

    return simulated_returns, new_portfolio_return
