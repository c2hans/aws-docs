---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/custom-metrics-troubleshooting.html
---

# Considerations for custom metrics in a predictive scaling policy
<a name="custom-metrics-troubleshooting"></a>

If an issue occurs while using custom metrics, we recommend that you do the following:
+ If an error message is provided, read the message and resolve the issue it reports, if possible.
+ If an issue occurs when you are trying to use a search expression in a blue/green deployment scenario, first make sure that you understand how to create a search expression that looks for a partial match instead of an exact match. Also, check that your query finds only the Auto Scaling groups that are running the specific application. For more information about the search expression syntax, see [CloudWatch search expression syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/search-expression-syntax.html) in the *Amazon CloudWatch User Guide*.
+ If you did not validate an expression in advance, the [put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scaling-policy.html) command validates it when you create your scaling policy. However, there is a possibility that this command might fail to identify the exact cause of the detected errors. To fix the issues, troubleshoot the errors that you receive in a response from a request to the [get-metric-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-data.html) command. You can also troubleshoot the expression from the CloudWatch console.
+ When you view your **Load** and **Capacity** graphs in the console, the **Capacity** graph might not show any data. To ensure that the graphs have complete data, make sure that you consistently enable group metrics for your Auto Scaling groups. For more information, see [Enable Auto Scaling group metrics (console)](ec2-auto-scaling-metrics.md#as-enable-group-metrics).
+ The capacity metric specification is only useful for blue/green deployments when you have applications that run in different Auto Scaling groups over their lifetime. This custom metric lets you provide the total capacity of multiple Auto Scaling groups. Predictive scaling uses this to show historical data in the **Capacity** graphs in the console.
+ You must specify `false` for `ReturnData` if `MetricDataQueries` specifies the SEARCH() function on its own without a math function like SUM(). This is because search expressions might return multiple time series, and a metric specification based on an expression can return only one time series.
+ All metrics involved in a search expression should be of the same resolution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
