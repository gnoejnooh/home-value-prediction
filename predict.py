from sklearn.linear_model import Lasso
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/merged_2016.csv')

# Drop non-numerical columns and fill NaN values with median
X_train = df.drop(['logerror', 'parcelid', 'transactiondate', 'hashottuborspa',\
'propertycountylandusecode', 'propertyzoningdesc',\
'taxdelinquencyflag'], axis=1)
X_train.fillna(X_train.median(), inplace=True)

y_train = df['logerror'].abs().values

print(X_train.shape, y_train.shape)

lasso = Lasso(alpha=0.1, normalize=True)
lasso.fit(X_train, y_train)

lasso_coef = lasso.coef_

plt.plot(range(len(X_train.columns)), lasso_coef)
plt.xticks(range(len(X_train.columns)), X_train.columns.values, rotation=60)
plt.margins(0.02)
plt.show()
