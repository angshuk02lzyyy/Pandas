import pandas as pd
from pandas import json_normalize #normalize to flat json nested data
import json #json module to read json files

# ─── Read from JSON file ──────────────────────────────────────
with open("exercise2.json", "r") as f: # open the JSON file in read mode
    data = json.load(f)              # loads JSON file into Python

# ─── Normalize and use ────────────────────────────────────────
df = json_normalize(data) # normalize the JSON data

print(df.head())                              # view data
print(df["salary"].mean())                    # average salary
print(df[df["department"] == "IT"])           # filter IT department
print(df.sort_values("salary"))               # sort by salary
print(df["address.city"])                     # get cities