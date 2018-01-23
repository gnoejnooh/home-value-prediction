import numpy as np
import pandas as pd

# Load dataset
train = pd.read_csv('data/train_2016_v2.csv', parse_dates=['transactiondate'])
prop = pd.read_csv('data/properties_2016.csv', low_memory=False)

# Check the dimension of each data
print("DIMENSION\n---------")
print("Training Size: " + str(train.shape))
print("Property Size: " + str(prop.shape))

# Type check
for c, dtype in zip(prop.columns, prop.dtypes):
    if dtype == np.int64:
        prop[c] = prop[c].astype(np.int32)
    if dtype == np.float64:
        prop[c] = prop[c].astype(np.float32)


# Merge train with prop
df = train.merge(prop, how='left', on='parcelid')
del train, prop
print("\nMERGED\n------")
print(df.head(2).transpose())


# Find redundant columns
dropcols = []
print("\nDROP COLUMNS\n-----------")

# Two census data are defined identically in data dictionary
print("rawcensustractandblock vs censustractandblock\n" + str(df[['rawcensustractandblock', 'censustractandblock']].corr()))
cond = bool(df['rawcensustractandblock'].isnull().sum() > df['censustractandblock'].isnull().sum())
dropcols.append('rawcensustractandblock' if cond else 'censustractandblock')

# Two bathroom count data are defined identically
print("bathroomcnt vs calculatedbathnbr\n" + str(df[['bathroomcnt', 'calculatedbathnbr']].corr()))
cond = bool(df['bathroomcnt'].isnull().sum() > df['calculatedbathnbr'].isnull().sum())
dropcols.append('bathroomcnt' if cond else 'calculatedbathnbr')
# Remaining bathroomcnt includes fullbathcnt and threequarterbathnbr
dropcols.extend(['fullbathcnt', 'threequarterbathnbr'])

print(dropcols)
