---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/data.html
---

# Data for forecasting freight demand
<a name="data"></a>

High-quality data is essential for any ML model to make a meaningful prediction and forecast. For demand forecasts, the dataset consists of any relevant data that could affect the ultimate demand. This data can come from various sources. You can classify this data into two categories, internal and external data.

## Internal data
<a name="internal-data"></a>

Internal data is organic, business-generated data. This data is usually stored in a data warehouse, such as [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html).

You can directly generate or extract target output values from tables in the data warehouse that contain historical volumes for products of interest. For shipping companies, outputs or target values can be in units of full container loads for ocean shipping or total weight for air cargo.

You can also generate various historical business metrics. These can be used as features in the machine learning model when forecasting demand. Example features include historical price, cost, capacity, and inventory.

## External data
<a name="external-data"></a>

External data sources can be used as additional features to improve the forecast accuracy. Examples of external data sources include weather data, macro-economic data, industry data, and market data. These factors can have direct or indirect impact to the logistics and transportation industry, therefore affecting demand. For example, market freight rate provides a benchmark of the global freight market, which ultimately affects company-specific demand. Macro-economic data, such as import and export data for major economies, could also be used as a measure of market activity. To incorporate these external data sources, you can use various APIs to ingest data. For example, the St. Louis Fed provides the [Federal Reserve Economic Data (FRED) API](https://fred.stlouisfed.org/docs/api/fred/) to access macro-economic data, and the National Oceanic and Atmospheric Administration (NOAA) provides the [Climate Data Online (CDO) API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) to access worldwide weather data.
