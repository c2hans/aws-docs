---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data-validation-rules.html
---

# Data Validation Rules
<a name="data-validation-rules"></a>

The validations performed prior to forecast creation are below. For more information, see [Demand Planning](required_entities.md).

| Rule Type | Rule | Datasets | Description | Export error records? |
| --- | --- | --- | --- | --- |
| Data Structure Validation | Mandatory columns existence validation | Product, Outbound order line, Supplementary time series | Verifies presence of critical columns in datasets in required datasets:<br />Outbound order line: product\_id, order\_date, final\_quantity\_requested<br />Product: id, description<br />Verifies presence of critical columns in recommended datasets, if provided:<br />Supplementary Time Series: id, order\_date, time\_series\_name, time\_series\_value | No |
| Data Structure Validation | Granularity columns existence validation | Product, Outbound order line | Verifies presence of columns set as forecast granularity, if set in the demand plan settings.<br />Outbound order line: product\_id, ship\_from\_site\_id, ship\_to\_site\_id, ship\_to\_site\_address\_city, ship\_to\_address\_state, ship\_to\_address\_country, channel\_id, customer\_tpartner\_id<br />Product: id, product\_group\_id, product\_type, brand\_name, color, display\_desc, parent\_product\_id | No |
| Data Structure Validation | Active product's history validation | Product, Outbound order line,Product Alternate | Verifies that there is atleast one active product that has history on its own or through product lineage | No |
| Data Quality Validation | Missing values in mandatory columns validation | Product, Outbound order line, Supplementary time series | Verifies for null/empty values in mandatory columns specified in Mandatory columns existence check | Yes |
| Data Quality Validation | Missing values in granularity columns validation | Product, Outbound order line | Verifies for null/empty values in mandatory columns specified in Granularity columns existence check | Yes |
| Data Quality Validation | Date Range validation | OutboundOrderLine, SupplementaryTimeSeries | The order\_date column in the dataset must contain dates in a sane time range: Anywhere from 01/01/1900 00:00:00 to 12/31/2050 00:00:00.  | Yes |
| Forecasting Eligibility Validation | Timeseries per Predictor validation | OutboundOrderLine | The timeseries per predictor must not exceed 5,000,000. <br />"Timeseries per predictor" is calculated by taking the count of unique values for the product\_id column and each of the forecast granularity columns and then taking the product of all those counts. | No |
| Forecasting Eligibility Validation | Count of active products validation | Product | The number of active products with records in the OOL dataset must not exceed 800,000. | No |
| Forecasting Eligibility Validation | Historical data sufficiency validation | Outbound order line | Verifies if at least one product in the dataset has sufficient historical demand data to generate reliable forecasts<br />The forecast horizon must be no greater than 1/3 the time range in the dataset (if training a new auto predictor) or 1/4 the time range in the dataset (if training an existing auto predictor).<br />There is also a global maximum forecast horizon, which is 500. | No |
| Forecasting Eligibility Validation | Row Count validation | Partitioned OutboundOrderLine | The number of records in the partitioned OOL dataset must not exceed 3,000,000,000. There are certain forecast models that have smaller limits that are checked here as well, if those models are being used. | No |
| Forecasting Eligibility Validation | Maximum Timeseries validation | Partitioned OutboundOrderLine | The number of distinct timeseries must not exceed the model's limit, if there is one. <br />"Distinct timeseries" is defined as the number of distinct rows in the dataset when product\_id \+ all forecast granularity columns are considered. | No |
| Forecasting Eligibility Validation | Data Density validation | Partitioned OutboundOrderLine | The Data density of the dataset must be at least 5.<br />Data density is defined as (number of distinct products in the dataset) / (total number of rows in the dataset). In other words it is "average rows per product".The rule applies only when Prophet is selected as the forecasting algorithm. | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
