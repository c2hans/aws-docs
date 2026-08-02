---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/forecast-forecast-entity.html
---

# forecast
<a name="forecast-forecast-entity"></a>

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| forecast | snapshot\_date, product\_id, site\_id, region\_id, product\_group\_id, forecast\_start\_dttm, forecast\_end\_dttm |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| snapshot\_date | timestamp | Yes | Date up to when data was captured to generate forecasts. |
| creation\_date | timestamp | No | Date when a forecast was created. |
| company\_id2 | string | No | Company ID. |
| product\_id2 | string | Yes1 | Product or product group level for the forecast. |
| site\_id2 | string | Yes1 | Site ID that the forecast is generated for . |
| source | string | No | Source of the data. |
| region\_id2 | string | Yes1 | Geographical region ID. |
| product\_group\_id2 | string | Yes1 | Product group ID. |
| reg\_agg\_type | string | No | Type of regional aggregation. |
| mean | double | No | Mean value of forecast. |
| p10 | double | No | P10 quantile of forecast. |
| p20 | double | No | P20 quantile of forecast. |
| p30 | double | No | P30 quantile of forecast. |
| p40 | double | No | P40 quantile of forecast. |
| p50 | double | No | P50 quantile of forecast. |
| p60 | double | No | P60 quantile of forecast. |
| p70 | double | No | P70 quantile of forecast. |
| p80 | double | No | P80 quantile of forecast. |
| p90 | double | No | P90 quantile of forecast. |
| forecast\_start\_dttm | timestamp | Yes | Forecast start date and time. |
| forecast\_end\_dttm | timestamp | Yes | Forecast end date and time. |
| default\_price | double | No | Default MSRP of the product that is forecast. |
| forecast\_price | double | No | Price at which the ASIN was forecast to be sold. |
| num\_causals | int | No | Number of casuals applied to forecast. |
| causal\_start | timestamp | No | Start date of causal. |
| causal\_end | timestamp | No | End date of causal. |
| user\_override | double | No | User override of forecast quantity. |
| user\_id | string | No | ID of the user that overrode the forecast. |
| act\_qty | double | No | Actual order quantity sold in the forecast period. |
| channel\_id | string | No | Unique identifier for a specific channel. Corresponds to channel\_id in the outbound\_order\_line dataset. |
| tpartner\_id 2 | string | No | Tpartner ID. |
| user\_override\_p10 | double | No | Override value for the P10 quantile of forecast. |
| user\_override\_p20 | double | No | Override value for the P20 quantile of forecast. |
| user\_override\_p30 | double | No | Override value for the P30 quantile of forecast. |
| user\_override\_p40 | double | No | Override value for the P40 quantile of forecast. |
| user\_override\_p50 | double | No | Override value for the P50 quantile of forecast. |
| user\_override\_p60 | double | No | Override value for the P60 quantile of forecast. |
| user\_override\_p70 | double | No | Override value for the P70 quantile of forecast. |
| user\_override\_p80 | double | No | Override value for the P80 quantile of forecast. |
| user\_override\_p90 | double | No | Override value for the P90 quantile of forecast. |
| postal\_code | string | No | Trading partner's postal code. |
| tpartner\_type | string | No | Trading partner type. |
| quantity\_uom | string | No | Quantity unit of measure. |
| demand\_plan\_id | string | No | Demand plan ID. |
| plan\_sequence\_id | string | No | Unique identifier or sequence number assigned to each individual demand plan or demand plan version. |
| plan\_type | string | No | Type of forecast or plan. |
| plan\_window\_start | timestamp | No | If plan corresponds to a planning bucket or window in application, this field stores the start of the planning window. |
| plan\_window\_end | timestamp | No | If plan corresponds to a planning bucket or window in application, this field stores the end of the planning window.  |
| ship\_to\_site\_id | string | No | Site to which an order is shipped. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system.  |
| status | string | No | Status defining whether the plan generated in demand planning was created, saved, or published.  |
| plan\_name | string | No | Represents the name of the demand plan associated with the forecast |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| product\_id | Product | product | id |
| region\_id | Organization | geography | id |
| product\_group\_id | Product | product\_hierarchy | id |
| site\_id | Network | site | id |
| tpartner\_id | Organization | trading\_partner | id |
| ship\_to\_site\_id | Outbound | outbound\_order\_line | ship\_to\_site\_id |
