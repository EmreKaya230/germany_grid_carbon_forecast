#compute carbon intensity
#for example: when there is high level wind and sun, CI low(cleaner)
#carbon intensity is target variable of the project.

import pandas as pc

def compute_ci(gen_hourly, ef):
    numerator = (gen_hourly * ef).sum(axis=1)
    denominator = gen_hourly.sum(axis=1)
    return numerator/denominator