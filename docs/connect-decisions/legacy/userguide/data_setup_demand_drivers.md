---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data_setup_demand_drivers.html
---

# Demand driver recommendations
<a name="data_setup_demand_drivers"></a>

While configuring aggregation and filling methods for demand drivers, a general guideline is to assign *mean* aggregation for both boolean and continuous data types. To fill a missing value, use *zero* filling for boolean data while *mean* filling is suitable for continuous data.

Note that the choice of aggregation and filling method configuration depends on the data characteristics and assumptions about missing values. Here is an example.

![Demand driver recommendation](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/demand_driver_recommendation.png)

Demand Planning recommends adjusting the demand driver configuration to best suit your dataset needs. The demand driver configuration will impact the forecast accuracy.

On the AWS Supply Chain web application, under **Demand planning**, **Overview**, you will view the impact scores associated with demand drivers, aggregated at the demand plan level. These impact scores measure the relative influence of demand drivers on forecast. A low impact score does not indicate that the demand driver has a minimal effect on forecast values. Instead, it suggests that its influence on forecast value is comparatively lower than the other demand drivers. When the impact score is zero under certain circumstances, it should be interpreted as the demand driver has no impact on the forecast values. Demand Planning recommends revisiting the aggregation and filling method configuration applied to that particular demand driver.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
