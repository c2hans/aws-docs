---
source_url: https://docs.aws.amazon.com/forecast/latest/dg/how-it-works.html
---

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# How Amazon Forecast Works
<a name="how-it-works"></a>

When creating forecasting projects in Amazon Forecast, you work with the following resources:
+ ** [Importing Datasets](howitworks-datasets-groups.md) ** – *Datasets* are collections of your input data. Dataset groups are collections of datasets that contain complimentary information. Forecast algorithms use your dataset groups to train custom forecasting models, called predictors.
+ ** [Training Predictors](howitworks-predictor.md) ** – *Predictors* are custom models trained on your data. You can train a predictor by choosing a prebuilt algorithm,or by choosing the AutoML option to have Amazon Forecast pick the best algorithm for you.
+ ** [Generating Forecasts](howitworks-forecast.md) ** – You can generate forecasts for your time-series data, query them using the [QueryForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_QueryForecast.html) API, or visualize them in the console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Forecast. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query forecast` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
