---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/custom-metrics-troubleshooting.html
---

# Considerations for custom metrics in a predictive scaling policy
<a name="custom-metrics-troubleshooting"></a>

If an issue occurs while using custom metrics, we recommend that you do the following:
+ If an error message is provided, read the message and resolve the issue it reports, if possible.
+ If you did not validate an expression in advance, the [ put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scaling-policy.html) command validates it when you create your scaling policy. However, there is a possibility that this command might fail to identify the exact cause of the detected errors. To fix the issues, troubleshoot the errors that you receive in a response from a request to the [get-metric-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-data.html) command. You can also troubleshoot the expression from the CloudWatch console.
+ You must specify `false` for `ReturnData` if `MetricDataQueries` specifies the SEARCH() function on its own without a math function like SUM(). This is because search expressions might return multiple time series, and a metric specification based on an expression can return only one time series.
+ All metrics involved in a search expression should be of the same resolution.

**Limitations**
The following limitations apply.
+ You can query data points of up to 10 metrics in one metric specification.
+ For the purposes of this limit, one expression counts as one metric.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
