from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir("/content/drive/MyDrive")
os.chdir("Trabajo Fin Grado")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
import pandas as pd
import datetime
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', skiprows= 1, sep='[;,:\s+]', names=range(215))
df.fillna(value=0, inplace=True)
df.head()
# Aplicar la conversión a timestamp a la columna 'fecha'
df[225] = df[2].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y').timestamp())
d_col1 = df.pop(225)
df.insert(1, 225, d_col1)

df = df.drop(df.columns[3], axis=1)
print(df)

#--------------------------------------------------------Etapa 1, 2000 primeros pacientes-------------------------------------------------------------------------------
df.drop(df.index[2000:4079], inplace=True, axis=0)
dfE1a=df.drop(df.iloc[:, 45:225], axis=1)
#print(dfE1a)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------Etapa 1, (2000, 4078] pacientes-------------------------------------------------------------------------------
#df2000 = df.drop(df.index[:2000])
#print(df2000)
#dfE1b=df2000.drop(df.iloc[:, 45:225], axis=1)
#print(dfE1b)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------Etapa 5, 2000 primeros pacientes-------------------------------------------------------------------------------
#df.drop(df.index[2000:4079], inplace=True, axis=0)
#dfaux1=df.drop(df.iloc[:, 0:44], axis=1)#auxiliar para la etapa 5
#dfE5a=dfaux1.drop(df.iloc[:, 70:225], axis=1)#etapa 5
#print(dfE5a)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 5, (2000, 4078] pacientes-------------------------------------------------------------------------------
#df2000 = df.drop(df.index[:2000])
#print(df2000)
#dfaux2=df2000.drop(df.iloc[:, 0:44], axis=1)#auxiliar para la etapa 5
#dfE5b=dfaux2.drop(df.iloc[:, 70:225], axis=1)#etapa 5
#print(dfE5b)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 6--------------------------------------------------------------------------------------------------------
#dfaux3=df.drop(df.iloc[:, 0:70], axis=1)#auxiliar para la etapa 6
#dfE6=dfaux3.drop(df.iloc[:, 96:225], axis=1)#etapa 6
#print(dfE6)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 7--------------------------------------------------------------------------------------------------------
#dfaux4=df.drop(df.iloc[:, 0:96], axis=1)#auxiliar para la etapa 7
#dfE7=dfaux4.drop(df.iloc[:, 122:225], axis=1)#etapa 7
#print(dfE7)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 8--------------------------------------------------------------------------------------------------------
#dfaux5=df.drop(df.iloc[:, 0:122], axis=1)#auxiliar para la etapa 8
#dfE8=dfaux5.drop(df.iloc[:, 148:225], axis=1)#etapa 8
#print(dfE8)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 9--------------------------------------------------------------------------------------------------------
#dfaux6=df.drop(df.iloc[:, 0:148], axis=1)#auxiliar para la etapa 9
#dfE9=dfaux6.drop(df.iloc[:, 174:225], axis=1)#etapa 9
#print(dfE9)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 17--------------------------------------------------------------------------------------------------------
#dfaux7=df.drop(df.iloc[:, 0:174], axis=1)#auxiliar para la etapa 17
#dfE17=dfaux7.drop(df.iloc[:, 186:225], axis=1)#etapa 17
#print(dfE17)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------Etapa 19--------------------------------------------------------------------------------------------------------
dfaux8=df.drop(df.iloc[:, 0:186], axis=1)#auxiliar para la etapa 19
dfE19=dfaux8.drop(df.iloc[:, 190:225], axis=1)#etapa 19
print(dfE19)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

corr_matrix = dfE1a.corr()
print(corr_matrix)

plt.matshow(dfE1a.corr())
plt.show()

f = plt.figure(figsize=(19, 15))
plt.matshow(dfE1a.corr(), fignum=f.number)
plt.xticks(range(dfE1a.select_dtypes(['number']).shape[1]), dfE1a.select_dtypes(['number']).columns, fontsize=14, rotation=45)
plt.yticks(range(dfE1a.select_dtypes(['number']).shape[1]), dfE1a.select_dtypes(['number']).columns, fontsize=14)
cb = plt.colorbar()
plt.title('Correlation Matrix', fontsize=16)