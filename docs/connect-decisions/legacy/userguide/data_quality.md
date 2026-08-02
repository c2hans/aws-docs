---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data_quality.html
---

# Prequisites before uploading your dataset
<a name="data_quality"></a>

To successfully generate a forecast, make sure your dataset adheres to the following.
+ At least one *product\_id* has a sales history of at least four times the forecast time horizon provided in the *outbound\_order\_line* dataset. For example, if the forecast time horizon is 26 weeks, the minimum order data requirement is 26\*4 = 104 weeks.
+ *Product\_id* under the product data entity should not contain any incomplete data (null or empty string) or duplicates.
+ All the additional columns selected for granularity in the forecast configuration (that are *conditionally required* ‘) does not contain incomplete data (null or empty string).
+ The column *id* across all data entities (for example, product\_id, site\_id, ship\_from\_site\_id) does not contain special characters, such as asterisk (\*) and double quotes (" ").
+ The *order\_date* does not contain invalid date. For example, 2/29/2023, that is 29th February 2023 is only valid on a leap year.

To improve forecast accuracy, Demand Planning highly recommends the following.
+ Upload two to three years of outbound order line history as input to generate an accurate forecast. This duration allows the forecasting models to capture your business cycles and ensure a more robust and reliable prediction.
+  For improved forecast accuracy, it is also recommended to include product attributes such as *brand*, *color*, *product\_group\_id*, *product\_introduction\_day* and *discontinue\_day* in the product data entity.
+ You can provide additional demand drivers information through the *supplementary\_time\_series* data entity. Note, only numerical values are supported.
+ You provide alternate product mapping when you have similar products or previous version for a new product.
+ Remove any non-recurring or one-time event such as COVID before uploading the historical sales data.
