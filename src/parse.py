import json 
import pandas as pd

path = "/Users/emrekaya/germany_grid_carbon_forecast/data/raw/sample_public_power_2023-04-01_03.json"

def load_power(path):
    with open(path) as f:
        data = json.load(f)
        
    cols = {}
    for source in data["production_types"]:
        cols[source["name"]] = source["data"]
    df = pd.DataFrame(cols)
            
    df.index = pd.to_datetime(data["unix_seconds"], unit="s", utc=True)
    return df

def load_power2()
    path = "/Users/emrekaya/germany_grid_carbon_forecast/data/raw/sample_public_power_2023-04-01_03.json"

path2 = "data/raw/sample_public_power_2023-04-14_17.json"
def load_power(path2):
    with open(path2) as f:
        data = json.load(f)
        
    cols = {}
    for source in data["production_types"]:
        cols[source["name"]] = source["data"]
    df2= pd.DataFrame(cols)
            
    df2.index = pd.to_datetime(data["unix_seconds"], unit="s", utc=True)
    return df2


