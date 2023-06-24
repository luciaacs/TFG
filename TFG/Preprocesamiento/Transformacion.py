# Import libraries
'''Main'''
import numpy as np
import pandas as pd
import os, time
import pickle, gzip

'''Data Viz'''
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
import matplotlib as mpl


'''Data Prep and Model Evaluation'''
from sklearn import preprocessing as pp
from scipy.stats import pearsonr
from numpy.testing import assert_array_almost_equal
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import log_loss
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report

'''Algos'''
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb
df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', sep='[;,:\s+]', skiprows=1, names=range(225))
df.head()
df.describe()
df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', skiprows= 1, sep='[;,:\s+]', names=range(225))
df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', skiprows= 1, sep='[;,:\s+]', names=range(225))
df.fillna(value=0, inplace=True)
df.head()
print(dfX.dtypes)
df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', skiprows= 1, sep='[;,:\s+]', names=range(215))
df.fillna(value=0, inplace=True)
df.head()
import datetime
# Aplicar la conversión a timestamp a la columna 'fecha'
df[225] = df[2].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y').timestamp())
d_col1 = df.pop(225)  
df.insert(1, 225, d_col1)
print(df)
