---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/forecast-supp-timeseries-entity.html
---

# supplementary\_time\_series
<a name="forecast-supp-timeseries-entity"></a>

**Note**
If you cannot locate the supplementary\_time\_series data entity, your instance might be using an older data model version. You can contact AWS Support to upgrade your data model version or create a new data connection.

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| forecast\_supplementary\_time\_series | id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Unique identifier with each supplementary data entry. |
| product\_id 2 | string | No | Unique identifier for a specific product. Corresponds to product\_id in the outbound\_order\_line dataset. |
| product\_group\_id | string | No | Product hierarchy or grouping. |
| order\_date  | timestamp | Yes1 | The timestamp indicating the date and time when the date for the respective time-series was recorded. |
| channel\_id | string | No | Unique identifier for a specific product. Corresponds to product\_id in the outbound\_order\_line dataset. |
| customer\_tpartner\_id 2 | string | No | Unique identifier for a specific user. Corresponds to customer\_tpartner\_id field in outbound\_order\_line dataset. |
| site\_id 2 | string | No | Unique identifier for a specific site or location. |
| ship\_to\_site\_id 2 | string | No | Unique identifier for a specific site or location. This corresponds to the *ship\_to\_site\_id* in the *outbound\_order\_line* dataset. |
| ship\_to\_site\_address\_zip | string | No | Postal code of *ship\_to\_site\_id*. |
| geo\_id 2 | string | No | Geographical hierarchy ID. |
| ship\_from\_site\_id 2 | string | No | Corresponds to the *ship\_from\_site\_id* in the *outbound\_order\_line* dataset. |
| ship\_from\_site\_address\_zip | string | No | Postal code of *ship\_from\_site\_id*. |
| time\_series\_name | string | Yes | The *time\_series\_name* must start with a letter, should be 2 to 56 characters long, and can contain letters, numbers, and underscores. No other special characters are allowed. |
| time\_series\_value | string | Yes | Value corresponding to the specific time series. This could represent quantities, metric, or string that is relevant to the type of the data. Demand planning only supports numerical value as additional forecast input. |
| source\_event\_id | string | No | ID of the event created in the source system. |
| source\_update\_dttm | timestamp | No | Date time stamp of the update made in the source system. |

1You must enter a value. When you ingest data from SAP or EDI, the default value for *string* is SCN\_RESERVED\_NO\_VALUE\_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| product\_id | Product | product | id |
| site\_id | Network | site | id |
| customer\_tpartner\_id | Organization | trading\_partner | id |
| ship\_to\_site\_id | Outbound fulfilment | outbound\_order\_line | ship\_to\_site\_id |
| geo\_id | Organization | geography | id |
| ship\_from\_site\_id | Outbound fulfilment | outbound\_order\_line | ship\_from\_site\_id |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
