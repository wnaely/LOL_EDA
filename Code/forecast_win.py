import pandas as pd
import numpy as np

df = pd.read_pickle("./0917_game_data_norm.pkl")
idx = pd.IndexSlice

position = ['TOP', 'MID', 'JUG', 'SPT', 'ADC']
features = ['kda', 'dpd', 'dpg', 'dpm', 'dtpm']

ids = set()
for id, _, _ in df.index: ids.add(id)
ids = sorted(ids)
match_data = []

for id in ids:
    blue_data = df.loc[idx[id, 100, features]].values
    blue_data = list(np.concatenate(blue_data))
    red_data  = df.loc[idx[id, 200, features]].values
    red_data  = list(np.concatenate(red_data))
    blue_win = df.loc[idx[id, 100, 'win']].values
    win  = blue_win[0]
    blue_sum = sum(blue_data)
    red_sum = sum(red_data)
    forecast = 0
    if blue_sum > red_sum : forecast = 1
    acc = 0
    if win == forecast: acc =1
    match_info = {
        "id" : id,
        "blue" : blue_data,
        "red" : red_data,
        "win" : win,
        "forecast" : forecast,
        "acc": acc
    }
    print(id, win, forecast, acc)
    match_data.append(match_info)

acc_sum = 0
for match in match_data:
    acc_sum += match["acc"]

print(acc_sum, len(ids), acc_sum / len(ids))

#for match in match_data:
    #print(match["id"], match["win"], match["forecast"])