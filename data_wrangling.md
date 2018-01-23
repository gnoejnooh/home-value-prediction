# Data Wrangling
With the data provided by Kaggle for Zillow Prize Competition, we are to explore the real estate data to predict the log-error between Zillow's home value prediction algorithm and the actual sale price, given all the features of a home.

## Attributes
In the data files, properties_2016.csv and properties_2017.csv, there is full list of real estate properties in three counties (Los Angeles, Orange and Ventura, California). It contains the following attributes.

Id/Code | Features | Measurement | Count | Location | Tax Assessment
--- | --- | --- | --- | --- | ---
FIPS County Code `fips` | Air Conditioning Type Id `airconditioningtypeid` | Finished Basement Sqft `basementsqft` | Bathroom (User) `bathroomcnt` | Latitude `latitude` | Total `taxvaluedollarcnt`
Parcel Id `parcelid` | Architectural Style Type Id `architecturalstyletypeid` | Finished 1st Floor Living Area Sqft `finishedfloor1squarefeet` | Bedroom  `bedroomcnt` | Longitude `longitude` | Built Structure `structuretaxvaluedollarcnt`
County Land User Code `propertycountylandusecode` | Building Quality Type Id `buildingqualitytypeid` | Total Finished Sqft (Zillow) `calculatedfinishedsquarefeet` | Bathroom (Zillow) `calculatedbathnbr` | County `regionidcounty` | Land `landtaxvaluedollarcnt`
Census Tract and Block Id (String) `rawcensustractandblock` | Building Class Type Id `buildingclasstypeid` | Base Finished and Unfinished Area `finishedsquarefeet6` | 3/4 Bathroom `threequarterbathnbr` | City `regionidcity` | Total by Assessment Year `taxamount`
Census Tract and Block Id (Integer) `censustractandblock` | Deck Type Id `decktypeid` | Finished Living Area `finishedsquarefeet12` | Fireplace `fireplacecnt` | Zipcode `regionidzip` | Assessment Year `assessmentyear`
| Fireplace Exist `fireplaceflag` | Perimeter Living Area `finishedsquarefeet13` | Full Bathroom `fullbathcnt` | Neighborhood `regionidneighborhood` | Past Due as of 2015 `taxdelinquencyflag`
| Hot Tub/Spa Exist `hashottuborspa` | Total Area `finishedsquarefeet15` | Garage `garagecarcnt` || Year the tax was due `taxdelinquencyyear`
| Heating System Type `heatingorsystemtypeid` | Total Finished Sqft (User) `finishedsquarefeet50` | Pool `poolcnt` |
| Number of Stories `numberofstories` | Garage Sqft `garagetotalsqft` | Room `roomcnt` |
| Pool Type (Spa or Hot Tub) `pooltypeid10` | Lot Size Sqft `lotsizesquarefeet` | Unit `unitcnt` |
| Pool Type (Pool with Spa/Hot Tub) `pooltype2` | Pool Sqft `poolsizesum` ||
| Pool Type (Pool without Hot Tub) `pooltypeid7` | Patio in Yard Sqft `yardbuildingsqft17` | |
| Land Type `propertylandusetypeid` | Storage Building Sqft `yardbuildingsqft26` ||
| Zoning Type `propertyzoningdesc` |||
| Story Type `storytypeid` |||
| Construction Material `typeconstructiontypeid` |||
| Year Built `yearbuilt` |||

The data files, train_2016.csv and train_2017.csv, has the transaction date from 1/1/2016 to 9/15/2017 along with the logerror data.

Percel Id | Log Error | Transaction Date
--- | --- | ---
`parcelid` | `logerror` | `transactiondate`

## Cleaning Data
The data needs to be cleaned for analysis. The following steps was considered during the process.
1. Redundant columns to be removed.
2. Columns with a considerably few data can be ignored under the circumstance (i.e. a column contains 1624 entries out of 2985217 rows).
