import numpy as np
import pandas as pd

# Load dataset
train = pd.read_csv('data/train_2016_v2.csv', parse_dates=['transactiondate'])
prop = pd.read_csv('data/properties_2016.csv', low_memory=False)

# Check the dimension of each data
print("DIMENSION\n---------")
print("Training Size: " + str(train.shape))
print("Property Size: " + str(prop.shape))


# Merge train with prop
df = train.merge(prop, how='left', on='parcelid')
#df = prop
del train, prop
print("\nMERGED\n------")
print(df.head(2).transpose())


# Type check
for c, dtype in zip(df.columns, df.dtypes):
    if dtype == np.int64:
        df[c] = df[c].astype(np.int32)
    if dtype == np.float64:
        df[c] = df[c].astype(np.float32)


# Find redundant columns
dropcols = []
print("\nDROP COLUMNS\n------------")

def drop_identical(col1, col2):
    print(col1 + " vs " + col2 + "\n" + str(df[[col1, col2]].corr()) + "\n")
    cond = bool(df[col1].isnull().sum() > df[col2].isnull().sum())
    dropcols.append(col1 if cond else col2)

# Column pairs that are defined identically in data dictionary
drop_identical('rawcensustractandblock', 'censustractandblock')
drop_identical('finishedfloor1squarefeet', 'finishedsquarefeet50')
drop_identical('calculatedfinishedsquarefeet', 'finishedsquarefeet12')
drop_identical('bathroomcnt', 'calculatedbathnbr')
drop_identical('hashottuborspa', 'pooltypeid10')

# Remaining bathroom columns are redundant (full and 3/4 bathroom count)
# bathroomcnt = fullbathcnt + threequarterbathnbr
dropcols.extend(['fullbathcnt', 'threequarterbathnbr'])

def drop_few(col):
    print("Examine " + col + ":")
    print(str(df[df[col].isnull() == False][col].value_counts()) + "\n")
    dropcols.append(col)

# Check the null entry on every columns
# Remove sqft information - Total sqft information can be acquired from calculatedfinishedsquarefeet
missing = (df.isnull().sum() / df.shape[0] * 100)
print("\nMISSING VALUES\n--------------")
print("Columns with missing values over 90%:\n" + str(missing[missing > 90].sort_values(ascending=False)) + "\n")
dropcols.extend(['finishedsquarefeet6', 'finishedsquarefeet13', 'finishedsquarefeet15', 'basementsqft'])

# storytypeid only contains 16 values (all 7.0 representing basement) which does not correspond with numberofstories
print("Check the value of storytypeid:\n" + str(df[df['storytypeid'].isnull() == False][['storytypeid', 'numberofstories']].head()) + "\n")
dropcols.append('storytypeid')

# The column contains only a few value to be valuable
drop_few('architecturalstyletypeid')
drop_few('buildingclasstypeid')
drop_few('typeconstructiontypeid')

# Compare fireplaceflag with fireplacecnt
print("Compare fireplaceflag with fireplacecnt:\n" + str(df[df['fireplacecnt'].isnull() == False][['fireplaceflag', 'fireplacecnt']].head()) + "\n")
# Replace fireplaceflag
df['fireplaceflag'] = np.nan
df.loc[df['fireplacecnt'] > 0, 'fireplaceflag'] = 1.0

# decktypeid has only one type - Change it to be deckflag
print("Deck type:\n" + str(df['decktypeid'].value_counts()) + "\n")
df.loc[df['decktypeid'].isnull() == False, 'deckflag'] = 1.0
#df.rename(columns={'decktypeid':'deckflag'}, inplace=True)
dropcols.append('decktypeid')

# Drop accumulated columns
print("Columns to drop:\n" + str(dropcols) + "\n")
df = df.drop(columns=dropcols)


# Add proportional values
# living area proportions = Calculated total finished living area of the home / Area of the lot in square feet
df['living_area_prop'] = df['calculatedfinishedsquarefeet'].divide(df['lotsizesquarefeet'])
# tax value ratio = total tax assessed value of the parcel / total property tax assessed in a year
df['value_ratio'] = df['taxvaluedollarcnt'].divide(df['taxamount'])
# tax value proportions = assessed value of the built structure on the parcel / assessed value of the land
df['value_prop'] = df['structuretaxvaluedollarcnt'].divide(df['landtaxvaluedollarcnt'])


# Convert categorical values
df['airconditioningtypeid'] = df['airconditioningtypeid'].astype('category')
df['buildingqualitytypeid'] = df['buildingqualitytypeid'].astype('category')
df['fips'] = df['fips'].astype('category')
df['heatingorsystemtypeid'] = df['heatingorsystemtypeid'].astype('category')
df['propertycountylandusecode'] = df['propertycountylandusecode'].astype('category')
df['propertylandusetypeid'] = df['propertylandusetypeid'].astype('category')


# Print info
print(df.info())


# Export the merged data
df.to_csv('data/merged_2016.csv', index=False)
