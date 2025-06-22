import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import fetch_data
from src.risk_metrics import *
from src.portfolio_metrics import *
from datetime import datetime

st.set_page_config(page_title="Portfolio Risk Dashboard", layout="wide")

# Title
st.title("📊 Portfolio Risk Analytics Dashboard")

# Sidebar: Input
st.sidebar.header("User Input")

tickers = st.sidebar.multiselect(
    "Select Stocks",
    options=["AAPL", "MSFT", "GOOGL", "AMZN", "META"],
    default=["AAPL", "MSFT"]
)

start_date = st.sidebar.date_input("Start Date", datetime(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime(2024, 1, 1))

# Portfolio Weights
st.sidebar.subheader("Portfolio Weights")
weights = {}

if tickers:
    default_weight = round(1.0 / len(tickers), 2)
    for ticker in tickers:
        weights[ticker] = st.sidebar.slider(
            f"{ticker} weight", 0.0, 1.0, default_weight, 0.01
        )
    total_weight = sum(weights.values())
    st.sidebar.markdown(f"**Total Weight:** {total_weight:.2f}")
    if abs(total_weight - 1.0) > 0.01:
        st.sidebar.warning("Weights should sum to 1.0")

# Run Analysis
if st.button("🔍 Run Risk Analysis"):
    try:
        st.subheader("📥 Fetched Adjusted Close Prices")
        data = fetch_data(tickers, start_date, end_date)
        st.dataframe(data.tail())

        # Daily returns
        returns = calculate_daily_returns(data)

        st.subheader("📈 Daily Returns")
        st.line_chart(returns)

        # Risk metrics
        st.subheader("📊 Risk Metrics (Individual)")
        vol = calculate_annualised_volatility(returns)
        var = calculate_var(returns)
        sharpe = calculate_sharpe_ratio(returns)

        st.write("**Annualized Volatility:**")
        st.dataframe(vol)

        st.write("**Value at Risk (95%):**")
        st.dataframe(var)

        st.write("**Sharpe Ratio:**")
        st.dataframe(sharpe)

        # Portfolio metrics
        st.subheader("📦 Portfolio Risk Metrics")
        portfolio_vol, portfolio_var, portfolio_sharpe = calculate_portfolio_metrics(returns, weights)

        st.metric("Volatility", f"{portfolio_vol:.2%}")
        st.metric("Value at Risk (95%)", f"{portfolio_var:.2%}")
        st.metric("Sharpe Ratio", f"{portfolio_sharpe:.2f}")

        # Correlation Heatmap
        st.subheader("🔗 Correlation Heatmap")

        # width = st.slider("Heatmap width", 5, 20,10)
        # height = st.slider("Heatmap height", 5, 20,8)

        fig, ax = plt.subplots(figsize=(6,4))
        sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        # Stress testing (optional toggle)
        st.subheader("⚠️ Stress Test")
        st.info("Apply a hypothetical -5% market shock to all assets.")
        shocked_returns = returns - 0.05
        shocked_vol, shocked_var, shocked_sharpe = calculate_portfolio_metrics(shocked_returns, weights)

        st.write("**Post-Stress Portfolio Metrics:**")
        st.metric("Volatility", f"{shocked_vol:.2%}")
        st.metric("VaR (95%)", f"{shocked_var:.2%}")
        st.metric("Sharpe Ratio", f"{shocked_sharpe:.2f}")

    except Exception as e:
        st.error(f"Something went wrong {e}")




# # --- Sidebar Inputs ---
# st.sidebar.header("Portfolio Configuration")
# tickers = st.sidebar.text_input("Enter tickers (comma-separated):", "AAPL,GOOGL,MSFT").split(",")
# start = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
# end = st.sidebar.date_input("End Date", pd.to_datetime("2024-01-01"))

# weights = st.sidebar.text_input("Portfolio Weights (comma):", "0.33,0.33,0.34")
# weights = [w for w in weights]

# ## - Fetch and display data
# st.title("📊Portfolio Risk Analytics Dashboard")
# st.subheader("Historial Price data")

# data = fetch_data(tickers,start,end)
# st.write(data.tail())

# # --- Calculate Metrics ---
# returns = calculate_daily_returns(data)
# vol = calculate_annualised_volatility(returns)
# var = calculate_var(returns)
# sharpe = calculate_sharpe_ratio(returns)

# # --- Display Metrics ---
# st.subheader("📉 Risk Metrics")
# st.write("**Annualized Volatility**")
# st.dataframe(vol)
# st.write("**Value at Risk (95%)**")
# st.dataframe(var)
# st.write("**Sharpe Ratio**")
# st.dataframe(sharpe)

# # --- Portfolio Metrics ---
# port_vol, port_ret, port_sharpe = calculate_portfolio_metrics(returns, weights)
# st.subheader("📦 Portfolio-Level Metrics")
# st.markdown(f"**Annualized Volatility:** `{port_vol:.4f}`")
# st.markdown(f"**Expected Annual Return:** `{port_ret:.4f}`")
# st.markdown(f"**Sharpe Ratio:** `{port_sharpe:.4f}`")





