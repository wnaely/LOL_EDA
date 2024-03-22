import pandas as pd
import numpy as np
df = pd.read_pickle("./0917_game_data.pkl")
df_norm = df.copy(deep=True)
idx = pd.IndexSlice
ids = set()
for id, _, _ in df.index: ids.add(id)
ids = sorted(ids)

features =  ['kda', 'dpd', 'dpm', 'dpg', 'dtpm']
i = 0
for id in ids:
    for feature in features:
        val = df_norm.loc[idx[id, :, feature]].values
        val = np.concatenate(val)
        val_norm = (val - np.min(val)) / (np.max(val) - np.min(val))
        df_norm.loc[idx[id, 100, feature]] = val_norm[0:5]
        df_norm.loc[idx[id, 200, feature]] = val_norm[5:10]
    print(i); i+=1
df_norm.to_pickle("0917_game_data_norm.pkl")