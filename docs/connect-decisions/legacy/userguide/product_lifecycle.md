---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product_lifecycle.html
---

# Product lifecycle
<a name="product_lifecycle"></a>

Product lifecycle describes the lifecycle of a product from introduction to End of Life (EoL). AWS Supply Chain supports forecasting products through it's lifecycle. To enable the Product lifecycle feature, populate the *product\_introduction\_day* and *discontinue\_day* columns in the *Product* data entity. Demand Planning uses the data from these columns to create forecast for a product when the product is active. For more information data entities, see [Data entities and columns used in AWS Supply Chain](data-model.md).

To enable product lifecycle, make sure the columns *id*, *description*, *product\_available\_day*, *discontinue\_day*, and *is\_deleted* are populated in the *Product* data entity.

The example below displays how Demand Planning works when data is ingested in the Product data entity.

| Column name | Required for Data Lake | Required for Demand Planning | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 | Scenario 5 | Scenario 6 | Scenario 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| id | Yes | Yes | Product123 | Product123 | Product123 | Product123 | Product123 | Product123 | Product123 |
| description | Yes | Yes | Bottle | Bottle | Bottle | Bottle | Bottle | Bottle | Bottle |
| product\_available\_day | No | No | May 1, 2023 | May 1, 2023 | May 1, 2023 | Null | Null | May 1, 2022 | May 1, 2022 |
| discontinue\_day | No | No | Null | December 31, 2023 | December 31, 2023 | Null | Null | May 1, 2023 | Past |
| is\_deleted | No | No | No | No | Yes | No | Null | No | No |
| **Expected behavior** | NA | NA | Forecast will be created starting 3 months prior (or as configured) prior to May 1, 2023 to the end of the planning horizon since there is no discontinue date. | Forecast will be created starting 3 months prior (or as configured) prior to May 1, 2023 until the discontinue date (or as configured). | Forecast will not be created since the product is considered inactive. | Forecast will be created for the entire planning horizon. | Assumed that the product is active. | Forecast will be created for one day (May 1). | In case of conflict between is\_deleted and discontinue\_day, is\_deleted is considered. |

For information on how to configure Product lifecycle, see [Create your first demand plan](onboarding.md).

Under Demand Planning settings, you can set your forecast start date depending on the *product\_available\_day* in the Product data entity. By default, the forecast starts on the *product\_available\_day*. *Period* refers to the time interval set under **Scope** (daily, weekly, monthly, or yearly). You can adjust the start date to optimize inventory management.

Similar to start date, you can set an end date for your forecast depending on the *product\_discontinue\_day* in the Product data entity. By default, forecast will end on the *product\_discontinue\_day*. You can adjust the end date to prevent inaccurate forecasting beyond the product shelf life and avoid excess inventory cost. Enter zero if you want the forecast to match the *product\_available\_day* and *product\_discontinue\_day*. This global setting will apply to all eligible products.

When *product\_available\_day* and *product\_discontinue\_day* are not available, the forecast is created for the entire planning horizon.

You can also configure your system to initialize forecast values for products without historical data or alternate product links. The default value is zero. You can also set the period until which your system should use the initialize product forecast value based on the time interval set under **Scope** (daily, weekly, monthly, or yearly). The default value is three periods. This global setting will apply to all eligible products at the intersection of site, customer and channel dimensions, if they are selected as additional forecast granularity. For example, when forecast is set to weekly with an initialized value of 10 for 12 periods, and the start forecast is set to three periods before the *product\_available\_day*, for a Product X with October 2, 2023 product\_available\_date, the initialized value of 10 will be applied for each week from September 11, 2023 to December 3, 2023.

To change the *product\_available\_day* and *product\_discontinue\_day*, update the Product data entity in AWS Supply Chain data lake. You can also update the forecast start and stop date. When you change the initialization value and period settings, the changes are applied to all eligible products, including those which were initialized with a different value in the previous planning cycles. All the updates are applied to the next forecast creation cycle.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
