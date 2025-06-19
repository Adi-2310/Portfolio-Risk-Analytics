# 📊 Portfolio Risk Analytics Tool

This project is a complete **risk analysis engine** for financial portfolios, built in Python. It computes key risk metrics, visualizes market relationships, and simulates stress scenarios — all in a structured and extensible codebase.

✅ **Bonus**: An interactive [Streamlit](https://streamlit.io) dashboard (WIP) makes it usable by non-developers, traders, or analysts.

---

## 🚀 Features


- 📈 **Price Fetching**: Historical price data from Yahoo Finance
- 📉 **Daily Returns**: Log-based return calculations
- ⚠️ **Risk Metrics**:
  - Annualized Volatility
  - Value at Risk (VaR 95%)
  - Sharpe Ratio
- 📦 **Portfolio-Level Risk**: Risk aggregated based on custom asset weights
- 🔗 **Correlation Analysis**: Heatmap of asset correlations
- 🔥 **Stress Testing**: Shock scenarios to simulate market crashes
- 🎨 **Visualizations**: Line plots, heatmaps, and VaR histograms
- 🖥 **Streamlit Dashboard** (WIP): Interactive UI to run all features

---

## 📁 Project Structure

``` bash
.
├── src/                      # Core logic: data, metrics, plots
│   ├── utils.py
│   ├── risk_metrics.py
│   ├── portfolio_metrics.py
│   └── visualisations.py
├── main.py                   # CLI/main script for running analysis
├── dashboard.py              # Streamlit dashboard interface
├── outputs/                  # CSV outputs of metrics & returns
├── plots/                    # Saved charts (returns, heatmap, VaR)
├── requirements.txt          # Python dependencies
└── README.md
```
---

## ⚙️ Installation and Setup

    # Clone the repo
    - git clone https://github.com/Adi-2310/Portfolio-Risk-Analytics.git
    - cd portfolio-risk-analytics

    # Set up a virtual environment
    - python3 -m venv .venv
    - source .venv/bin/activate

    # Install dependencies
    - pip install -r requirements.txt

---

## 🧪 Running the scripts

    python main.py

---

## 🌐 Running the dashboard (Coming soon)
    streamlit run dashboard.py

---

## 💼 Why This Project

This is built as a preparatory project for my **Risk Analytics Internship at Morgan Stanley**, this tool replicates core practices in financial risk management, including:
- Risk metric calculation (VaR, Sharpe, Volatility)
- Portfolio-level stress testing
- Interactive dashboarding using Streamlit
This project helped me reinforce concepts in Python, data visualization, and financial analysis.

---

## 🙋‍♂️ Author

**Aditya Nair**  
GitHub: [@Adi-2310](https://github.com/Adi-2310)

