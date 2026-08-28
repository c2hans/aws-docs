---
source_url: https://docs.aws.amazon.com/forecast/latest/dg/aggregation-guidelines.html
---

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# Data Aggregation Assumptions
<a name="aggregation-guidelines"></a>

Forecast doesn't assume that your data is from any specific time zone. However, it makes the following assumptions when aggregating time series data:
+ All data is from the same time zone.
+ All forecasts are in the same time zone as the data in the dataset.
+ If you specify the [SupplementaryFeature](API_SupplementaryFeature.md) holiday feature in the [InputDataConfig](API_InputDataConfig.md) parameter for the [CreatePredictor](API_CreatePredictor.md) operation, the input data is from the same country.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Forecast. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query forecast` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
