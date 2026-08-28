---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/configuration_demand_drivers.html
---

# Demand driver configuration
<a name="configuration_demand_drivers"></a>

To use demand drivers, you must configure them. You can configure demand drivers only when you've ingested data in the *supplementary\_time\_series* data entity.

**Note**
If you don't configure the demand drivers, you can still generate a forecast. However, Demand Planning won't use the demand drivers.

## Demand drivers data filling method
<a name="filling_method_demand_drivers"></a>

A *filling method* represents (or "fills") missing values in a time series. Demand Planning supports the following filling methods. The filling method that Demand Planning applies depends on the location of the gap in the data.
+ Back filling – Applied when the gap is between a product's earlier recorded date and the last recorded date.
+ Middle filling – Applied when the gap is between the last recorded data point for a given product and the global last recorded date.
+ Future filling – Applied when the demand driver has at least one data point in the future and there is a gap in the future time horizon.

![Demand drivers filling method](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/filling_method.png)

Demand Planning utilizes the last 64 data points from the *supplementary\_time\_series* data entity corresponding to the demand driver for consideration. Demand Planning supports *zero*, *median*, *mean*, *maximum*, and *minimum* options for all three filling methods.

The following example illustrates how demand drivers handle missing data when data is ingested to the *price* column in the *supplementary\_time\_series* data entity for Product 1, that includes both history and future data.

![Demand drivers filling method](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/filling_method_example1.png)

## Aggregation method
<a name="aggregation_method_demand_drivers"></a>

Demand Planning uses the aggregation method to facilitate the integration of demand drivers at various levels of granularity by consolidating data over specific periods and granularity levels.

Time period aggregation – For example, when the *Inventory* demand driver is available at daily level but the forecast is at weekly level, demand planning will apply the aggregation method configured under the demand plan settings for inventory to use the information for forecasting.

![Aggregation method used by Demand Planning](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/aggregation_example1.png)

Granularity level aggregation – Here is an example of how demand planning uses the granularity level aggregation. *out\_of\_stock\_indicator* is available daily at product-site level but forecast granularity is only available at product level. Demand Planning will apply the aggregation method configured under the demand plan settings for this demand driver.

![Granularity method used by Demand Planning](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/granularity_example.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
