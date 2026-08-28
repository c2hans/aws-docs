---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/required_entities.html
---

# Demand Planning
<a name="required_entities"></a>

The following table lists the data entities and columns used by Demand Planning.

**How to read the table:**
+ **Required** – The columns in this data entity are mandatory to execute a demand forecast without any failures.
+ **Conditionally required** – The columns in this data entity are required depending on the configurations set under demand plan settings. For more information, see [Manage Demand Plan settings](settings.md).
+ **Recommended for forecast quality** – The columns in this data entity are required for the quality for the forecast.
+ **Optional** – The column name is optional. For enhanced feature output, it is recommended to add the column name with values.

- ** outbound\_order\_line **
  - **Is this data entity required?:** Required
  - **How is this data entity used?:** Demand Planning uses this data as the primary source of historical demand for forecast. Additionally, fields selected as granularity are sent for training and are available as filters to review the demand plan.
  - **Column:** id / **Is the column required?:** Required / **How is this column used in Forecasting?:** id, cust\_order\_id, and product\_id are used to uniquely identify a record in the data entity and this combination should always be unique. Make sure the column values do not have invalid characters such as asterisk and double-quotes.
  - **Column:** cust\_order\_id / **Is the column required?:** Required
  - **Column:** product\_id / **Is the column required?:** Required
  - **Column:** order\_date / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for forecast creation. Identifies the period for time-series forecasting.
  - **Column:** final\_quantity\_requested / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for forecast creation. Identifies the quantity used for time-series forecasting. This column must not contain null values and must be numerical. Make sure there are no commas in the values. For example, 500000.00 is an accepted value in Demand Planning.
  - **Column:** ship\_from\_site\_id / **Is the column required?:** Conditionally required / **How is this column used in Forecasting?:** This column is conditionally required for forecast creation if the column is selected for forecast dimension (Site Hierarchy). This column must have a value and is used for filtering and analysis of data. For information on how to map data for different fulfillment scenarios, see [Data mapping example for fulfillment](fulfillment_scenario.md).
  - **Column:** ship\_to\_site\_id / **Is the column required?:** Conditionally required
  - **Column:** channel\_id / **Is the column required?:** Conditionally required / **How is this column used in Forecasting?:** This column is conditionally required for forecast creation if the column is selected for forecast dimension (Channel Hierarchy). This column must have a value and is used for filtering and analysis of data. For information on how to map data for different fulfillment scenarios, see [Data mapping example for fulfillment](fulfillment_scenario.md).
  - **Column:** customer\_tpartner\_id / **Is the column required?:** Conditionally required / **How is this column used in Forecasting?:** This column is conditionally required for forecast creation if the column is selected for forecast dimension (Customer Hierarchy). This column must have a value and is used for filtering and analysis of data. For information on how to map data for different fulfillment scenarios, see [Data mapping example for fulfillment](fulfillment_scenario.md).
  - **Column:** ship\_to\_site\_address\_city / **Is the column required?:** Conditionally required / **How is this column used in Forecasting?:** This column is conditionally required for forecast creation if the column is selected for forecast dimension (Site Hierarchy). This column must have a value and is used for filtering and analysis of data. For information on how to map data for different fulfillment scenarios, see [Data mapping example for fulfillment](fulfillment_scenario.md).
  - **Column:** ship\_to\_site\_address\_state / **Is the column required?:** Conditionally required
  - **Column:** ship\_to\_site\_address\_country / **Is the column required?:** Conditionally required
  - **Column:** status / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** This column is recommended for forecast quality. Orders with canceled status are not considered as forecast input.

- ** product **
  - **Is this data entity required?:** Required
  - **How is this data entity used?:** Demand Planning uses the product attributes to establish hierarchy filters for demand plan review and for model training.
  - **Column:** id / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). Make sure the column values do not have duplicate IDs and special characters such as asterix and double-quotes.
  - **Column:** description / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). This column can contain special characters such as asterix, hyphen, quotes, and double-quotes.
  - **Column:** parent\_product\_id / **Is the column required?:** Conditionally required / **How is this column used in Forecasting?:** This column is conditionally required for forecast creation if the column is selected for forecast dimensions (Product Hierarchy). Make sure the column has values and is used for filtering and analysis of data and model training.
  - **Column:** product\_group\_id / **Is the column required?:** Conditionally required
  - **Column:** product\_type / **Is the column required?:** Conditionally required
  - **Column:** brand\_name / **Is the column required?:** Conditionally required
  - **Column:** color / **Is the column required?:** Conditionally required
  - **Column:** display\_desc / **Is the column required?:** Conditionally required
  - **Column:** product\_available\_day / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** Recommended. The value in this column improves forecast quality by allowing the forecasting model to consider the timing of new product introductions.
  - **Column:** discontinue\_day / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** Recommended. The value in this column improves forecast quality by allowing the forecasting model to consider the timing for product retirements.
  - **Column:** base\_uom / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** Unit of measure for product. Default is Eaches.
  - **Column:** is\_deleted / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** Recommended. Enter Y if the product ID should be excluded from forecasting.
  - **Column:** pkg\_height / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** Recommended. The physical characteristics of the product that the forecasting models can understand.
  - **Column:** pkg\_length / **Is the column required?:** Recommended for forecast quality
  - **Column:** pkg\_width / **Is the column required?:** Recommended for forecast quality
  - **Column:** shipping\_dimension / **Is the column required?:** Recommended for forecast quality
  - **Column:** casepack\_size / **Is the column required?:** Recommended for forecast quality

- ** product\_alternate **
  - **Is this data entity required?:** Recommended for forecast quality
  - **How is this data entity used?:** Demand Planning uses the data of product’s predecessor(s) or alternate(s) to create forecast for new products. When data is ingested into the product\_alternate data entity, Product lineage support for forecast is enabled. For more information, see [Product lineage](product_lineage.md). You can skip ingesting data into the product\_alternate data entity and the forecast can still be generated.
  - **Column:** alternative\_product\_id / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). Unique record identifier.
  - **Column:** product\_id / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). ID of the new product or new version of the product. Make sure product\_id is populated in the product data entity.
  - **Column:** product\_alternate\_id / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into SCDL. Identifier for a similar product or previous version of the product. To consider multiple similar products as a single product\_id, enter the products in separate rows. Make sure product\_alternate\_id is populated in the product data entity.
  - **Column:** alternate\_type / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for applying product supercession or lineage. Use the static value similar\_demand\_product in all the rows.
  - **Column:** alternate\_product\_qty / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for applying product supercession or lineage. Enter the proportion of history of the alternate\_product\_id  you want to use for forecasting product\_id. For example, if it is 60%, enter 60. When you have multiple alternative\_product\_id  for a single product\_id, the alternate\_product\_qty does not have to add up to 100.
  - **Column:** alternate\_product\_qty\_uom / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for applying product supercession or lineage. Use the specific static value "percentage".
  - **Column:** eff\_start\_date / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into SCDL. Enter the start timeframe to consider the history of a similar product. Make sure this date is on or before the eff\_end\_date or you can leave this field empty and Demand Planning will auto-fill the year with 1000.
  - **Column:** eff\_end\_date / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into SCDL. Enter the end timeframe to consider in history of a similar product. Make sure this date is on or after the eff\_start\_date or you can leave this field empty and Demand Planning will auto-fill the year with 9999..
  - **Column:** status / **Is the column required?:** Recommended for forecast quality / **How is this column used in Forecasting?:** Recommended. Enter Inactive to ignore the product supercession or lineage mapping.

- ** supplementary\_time\_series **
  - **Is this data entity required?:** Recommended for forecast quality
  - **How is this data entity used?:** Demand Planning uses this data as the primary source for tagging casual factors such as promotional events, discounts, holidays, and so on.
  - **Column:** id / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). Unique record identifier.
  - **Column:** order\_date / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). Timestamp when the timeseries was recorded.
  - **Column:** time\_series\_name / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into Supply Chain Data Lake (SCDL). Name of the specific type of time series. The time\_series\_name column must start with a letter, be 2 to 56 characters long, and can contain letters, numbers, and underscores. No other special characters are allowed.
  - **Column:** time\_series\_value / **Is the column required?:** Required / **How is this column used in Forecasting?:** Required for data ingestion into SCDL. Value corresponding to the specific time series. Demand Planning only supports numerical input and time-series with categorical value is not considered.
  - **Column:** product\_id / **Is the column required?:** Optional / **How is this column used in Forecasting?:** Recommended. Unique identifier for a specific product. Use this column if the demand driver is available at product level.
  - **Column:** site\_id / **Is the column required?:** Optional / **How is this column used in Forecasting?:** Recommended. Unique identifier for a specific site or location. Use this column if the demand driver is available at site level. This column can represent either ship\_from\_site\_id or ship\_to\_site\_id based on the lowest level site hierarchy configuration.
  - **Column:** channel\_id / **Is the column required?:** Optional / **How is this column used in Forecasting?:** Recommended. Unique identifier for a specific channel. Use this column if the demand driver is available at channel level.
  - **Column:** customer\_tpartner\_id / **Is the column required?:** Optional / **How is this column used in Forecasting?:** Recommended. Unique identifier for a specific customer. Use this column if the demand driver is available at customer level.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
