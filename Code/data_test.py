import pandas as pd

df = pd.read_pickle("top_data_only.pkl")

print(df.head())
print(len(df))