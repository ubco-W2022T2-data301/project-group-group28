import pandas as pd
import numpy as np
def load_data(path):
    return pd.read_csv(path, sep=';')

def load_and_process(path):
    df = (load_data(path)
          .drop(['Population', 'Forest area', 'Military expenditure', 'Beer consumption per capita'], axis=1)
          .apply(lambda x: x.replace(0, np.nan) if x.name != 'Beer consumption per capita' else x, axis=0)
          .dropna()
         )
    return df