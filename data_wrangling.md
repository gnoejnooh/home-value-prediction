# Data Wrangling
With the data provided by Kaggle for Zillow Prize Competition, we are to explore the real estate data to predict the log-error between Zillow's home value prediction algorithm and the actual sale price, given all the features of a home.

## Attributes
In the data files, properties_2016.csv and properties_2017.csv, there is full list of real estate properties in three counties (Los Angeles, Orange and Ventura, California). It contains the following attributes.

#### Id
| Parcel |
|---|
| Parcel Id `parcelid` |

#### Code
| Census Tract and Block | Federal Information Processing Standard |
|---|---|
| Census Tract and Block Id (String) `rawcensustractandblock` | FIPS County Code `fips` |
| Census Tract and Block Id (Integer) `censustractandblock` | |

#### Land Features
| Location | Type |
|---|---|
| Longitude `longitude` | Land Type `propertylandusetypeid` |
| Latitude `latitude` | Zoning Type `propertyzoningdesc` |
| County `regionidcounty` | County Land User Code `propertycountylandusecode` |
| City `regionidcity` | |
| Zipcode `regionidzip` | |
| Neighborhood `regionidneighborhood` | |

#### Building Features
| Architecture | Structure | Style |
|---|---|---|
| Building Quality Type Id `buildingqualitytypeid` | Construction Material `typeconstructiontypeid` | Architectural Style Type Id `architecturalstyletypeid` |
| Building Class Type Id `buildingclasstypeid` | Unit `unitcnt` | |
| Number of Stories `numberofstories` | | |
| Story Type `storytypeid` | | |
| Year Built `yearbuilt` | | |

#### Living Area Features
| Room | Bathroom | Fireplace
|---|---|---|
| Bedroom  `bedroomcnt` | Bathroom (User) `bathroomcnt` | Fireplace Exist `fireplaceflag` |
| Room `roomcnt` | Bathroom (Zillow) `calculatedbathnbr` | Fireplace `fireplacecnt` |
| | 3/4 Bathroom `threequarterbathnbr` | |
| | Full Bathroom `fullbathcnt` | |

#### Amenity Features
| Pool | Heating/Cooling | Garage |
|---|---|---|
| Deck Type Id `decktypeid` | Air Conditioning Type Id `airconditioningtypeid` | Garage `garagecarcnt` |
| Hot Tub/Spa Exist `hashottuborspa` | Heating System Type `heatingorsystemtypeid` | |
| Pool Type (Spa or Hot Tub) `pooltypeid10` | | |
| Pool Type (Pool with Spa/Hot Tub) `pooltype2` | | |
| Pool Type (Pool without Hot Tub) `pooltypeid7` | | |
| Pool `poolcnt` | | |

#### Square Footage
| Living Area | Amenity | Land |
|---|---|---|
| Finished Basement Sqft `basementsqft` | Garage Sqft `garagetotalsqft` | Lot Size Sqft `lotsizesquarefeet` | |
| Finished 1st Floor Living Area Sqft `finishedfloor1squarefeet` | Pool Sqft `poolsizesum` | |
| Total Finished Sqft (Zillow) `calculatedfinishedsquarefeet` | Patio in Yard Sqft `yardbuildingsqft17` | |
| Total Finished Sqft (User) `finishedsquarefeet50` | Storage Building Sqft `yardbuildingsqft26` | |
| Base Finished and Unfinished Area `finishedsquarefeet6` | | |
| Finished Living Area `finishedsquarefeet12` | | |
| Perimeter Living Area `finishedsquarefeet13` | | |
| Total Area `finishedsquarefeet15` | | |

#### Tax Assessment
| Tax | Detail | Delinquency |
|---|---|---|
| Total `taxvaluedollarcnt` | Built Structure `structuretaxvaluedollarcnt` | Past Due as of 2015 `taxdelinquencyflag` |
| Total by Assessment Year `taxamount` | Land `landtaxvaluedollarcnt` | Year the tax was due `taxdelinquencyyear` |
| Assessment Year `assessmentyear` | | |

The data files, train_2016.csv and train_2017.csv, has the transaction date from 1/1/2016 to 9/15/2017 along with the log-error data.

| Parcel Id | Log Error | Transaction Date |
| --- | --- | --- |
| `parcelid` | `logerror` | `transactiondate` |

## Cleaning Data
The data needs to be cleaned for analysis. The following steps was considered during the process.
1. Redundant columns to be removed. There are three pairs of columns defined identically in the data dictionary.
2. Columns with a considerably few data can be ignored under the circumstance (i.e. a column contains 1624 entries out of 2985217 rows).
