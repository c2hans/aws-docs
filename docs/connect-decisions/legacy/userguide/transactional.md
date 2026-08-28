---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/transactional.html
---

# Transactional data
<a name="transactional"></a>

**Topics**
+ [Forecast](#forecast)
+ [Sales history or demand](#demand)
+ [Inventory level](#inventory-level)
+ [Inbound orders](#in-flight-orders)

## Forecast
<a name="forecast"></a>

Supply Planning uses two different sources and types of forecast. You can use the following source systems to retrieve forecast source:
+ *External* – Supply Planning uses the data that is being ingested into the data lake forecast entity.
+ *Demand Planning* – Supply Planning uses the forecasts from Demand Planning.
+ *None* – Supply Planning uses the sales or demand history data from the outbound order line.

Supply Planning supports two types of forecast: deterministic and stochastic. Deterministic forecasts contain only the mean of the forecast. Stochastic forecasts contain P10/P50/P90, sometimes along with mean. When mean is not provided with stochastic forecasts, Supply Planning uses P50(median) as mean.

Each forecast record has four fields to represent the demand forecast:
+ mean(double)
+ p10(double)
+ p50(also known as median, double)
+ p90(double)

Based on the configured inventory policy, different fields in this entity are required. For *sl*, p10/p50/90 is required; for *doc\_fcst*, policy p50 or mean is required. Supply Planning uses p50 as an approximation of the mean, and for *doc\_dem* and *abs\_level*, none of the forecast fields are required.

**Daily planning**

Forecasts may be different for daily planning compared to weekly planning. Here is an example of the daily and weekly planning forecast requirement.

![Daily planning](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/daily-planning.png)

**Weekly planning**

You can use the daily planning forecast example for weekly planning, or you can also use the following example for weekly planning.

![Weekly planning](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/weekly-planning.png)

## Sales history or demand
<a name="demand"></a>

Inventory policy *doc\_dem* requires demand history to compute the historical average demand. Supply Planning gets the demand history from the *outbound\_order\_line* entity under the *Outbound* category. Supply Planning uses the following fields:
+ *ship\_from\_site\_id*(string)
+ *product\_id*(string)
+ *actual\_delivery\_date*(timestamp); when missing, use *promised\_delivery\_date*(timestamp)

As part of the calculation, Supply Planning uses historical outbound order lines with delivery dates in the past 30 days. The target field used for quantity is *quantity\_delivered*; when missing, use *quantity\_promised*. If *quantity\_promised* is missing, then *final\_quantity\_requested* will be used. If all are missing, then *0* will be used.

For example, if you use Supply Planning for product “laptop” at site “TX0” on July 1, 2023, the record in *outbound\_order\_line* where *product\_id=laptop*, *ship\_from\_site\_id=TX0*, and *actual\_delivery\_date* is from June 1, 2023 to June 30, 2023. Supply Planning adds all the records and divides by 30 days to get the daily demand.

## Inventory level
<a name="inventory-level"></a>

Supply Planning requires a beginning inventory level to start the planning process. Supply Planning searches for the inventory level under the *entity inv\_level* data entity. Supply Planning searches for a record with the following fields:
+ *product\_id*
+ *site\_id*

Supply Planning uses *on\_hand\_inventory* to determine the inventory level.

## Inbound orders
<a name="in-flight-orders"></a>

Supply Planning uses *inbound\_order\_line* to retrieve the in-flight order quantity. If an order is delivered during the planning horizon, the quantity is considered as part of the existing supply.

Supply Planning searches for a record under *inbound\_order\_line* with the following fields:
+ *order\_receive\_date*; when missing, use *expected\_delivery\_date*
+ *product\_id*
+ *to\_site\_id*

The following are the supported Order Types: PO (Purchase), TO (Transfer), and MO (Production or Manufacturing).

Supply Planning uses the *quantity\_received*; when missing, use *quantity\_confirmed* then *quantity\_submitted* to determine the on-order quantity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
