---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/fulfillment_scenario.html
---

# Data mapping example for fulfillment
<a name="fulfillment_scenario"></a>

Below is an example to map brick and mortar or online sales to outbound order line dataset and optimize the historical demand setup. Use this example to structure your data for accurate forecasting. Review the configurations in this example to make sure your forecasting models capture the different fulfillment scenarios.

**Note**
If the data fields *ship\_from\_site\_id*, *ship\_to\_site\_id*, and *channel\_id* are selected for forecast granularity, make sure they have values or enter *NULL* as the value. The forecast will fail if the fields are blank.

| Data field | Description | Scenario 1 – Store sales (POS) | Scenario 2 – E-commerce demand fulfilled by store | Scenario 3 – E-commerce demand fulfilled by online fulfillment center (direct to customer) |
| --- | --- | --- | --- | --- |
| ship\_from\_site\_id | Site at which inventory is managed | Store ID | Store ID | Fulfillment Center ID |
| ship\_to\_site\_id | Site that received the order | Enter NULL to avoid forecast failure | Country, Region, State, or Zip – as applicable | External retailer sore ID, or Country, Region, State, or Zip – as applicable |
| channel\_id | Map how an item is sold | Brick and mortar | E-commerce | E-commerce |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
