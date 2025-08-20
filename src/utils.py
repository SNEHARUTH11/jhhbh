import matplotlib.pyplot as plt
import seaborn as sns

def plot_corr(df):
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=False, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
