import pandas as pd
import numpy as np
import scipy

import matplotlib.pyplot as plt
# %matplotlib inline

import seaborn as sns

from sklearn.metrics import r2_score


tables = ['Total','Drywhite','Fortified','Red','Rose','Sparkling','Sweetwhite']
wine_raw = pd.read_csv('wine.csv').iloc[:,1:]
wine = wine_raw[tables]
date_index = pd.date_range(start='1/1/1980', periods=wine.shape[0], freq='M')
wine.index = date_index
wine.head()