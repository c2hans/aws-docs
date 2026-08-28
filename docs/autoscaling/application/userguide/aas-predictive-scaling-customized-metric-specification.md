---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/aas-predictive-scaling-customized-metric-specification.html
---

# Advanced predictive scaling policy using custom metrics
<a name="aas-predictive-scaling-customized-metric-specification"></a>

In a predictive scaling policy, you can use predefined or custom metrics. Custom metrics are useful when the predefined metrics do not sufficiently describe your application load.

When creating a predictive scaling policy with custom metrics, you can specify other CloudWatch metrics provided by AWS, or you can specify metrics that you define and publish yourself. You can also use metric math to aggregate and transform existing metrics into a new time series that AWS doesn't automatically track. When you combine values in your data, for example, by calculating new sums or averages, it's called *aggregating*. The resulting data is called an *aggregate*.

The following section contains best practices and examples of how to construct the JSON structure for the policy.

**Topics**
+ [Best practices](#custom-metrics-best-practices)
+ [Prerequisites](#custom-metrics-prerequisites)
+ [Constructing the JSON for custom metrics](construct-json-custom-metrics.md)
+ [Considerations for custom metrics in a predictive scaling policy](custom-metrics-troubleshooting.md)

## Best practices
<a name="custom-metrics-best-practices"></a>

The following best practices can help you use custom metrics more effectively:
+ For the load metric specification, the most useful metric is a metric that represents the load on your application.
+ The scaling metric must be inversely proportional to capacity. That is, if the scalable target increases, the scaling metric should decrease by roughly the same proportion. To ensure that predictive scaling behaves as expected, the load metric and the scaling metric must also correlate strongly with each other.
+ The target utilization must match the type of scaling metric. For a policy configuration that uses CPU utilization, this is a target percentage. For a policy configuration that uses throughput, such as the number of requests or messages, this is the target number of requests or messages per instance during any one-minute interval.
+ If these recommendations are not followed, the forecasted future values of the time series will probably be incorrect. To validate that the data is correct, you can view the forecasted values. Alternatively, after you create your predictive scaling policy, inspect the `LoadForecast` and `CapacityForecast` objects returned by a call to the [GetPredictiveScalingForecast](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_GetPredictiveScalingForecast.html) API.
+ We strongly recommend that you configure predictive scaling in forecast only mode so that you can evaluate the forecast before predictive scaling starts actively scaling capacity.

## Prerequisites
<a name="custom-metrics-prerequisites"></a>

To add custom metrics to your predictive scaling policy, you must have `cloudwatch:GetMetricData` permissions.

To specify your own metrics instead of the metrics that AWS provides, you must first publish your metrics to CloudWatch. For more information, see [Publishing custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in the *Amazon CloudWatch User Guide*.

If you publish your own metrics, make sure to publish the data points at a minimum frequency of five minutes. Application Auto Scaling retrieves the data points from CloudWatch based on the length of the period that it needs. For example, the load metric specification uses hourly metrics to measure the load on your application. CloudWatch uses your published metric data to provide a single data value for any one-hour period by aggregating all data points with timestamps that fall within each one-hour period.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
