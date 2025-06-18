import matplotlib.pyplot as plt
import seaborn as sns


def plot_returns(returns_df):
    returns_df.plot(figsize=(12,6))
    plt.title('Daily returns')
    plt.xlabel('Date')
    plt.ylabel('Return')
    plt.grid(True)
    plt.show()


def plot_correlation_heatmap(returns_df):
    corr = returns_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()


def plot_var_histogram(returns_series, var_value):
    plt.figure(figsize=(8, 5))
    sns.histplot(returns_series, bins=50, kde=True)
    plt.axvline(var_value, color='red', linestyle='--', label=f'VaR (95%): {var_value:.2%}')
    plt.title("Return Distribution with VaR")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()
