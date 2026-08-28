---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html
---

# Transformation metrics and errors
<a name="Transformation-Errors-Metrics"></a>

CloudWatch Logs publishes transformation metrics to CloudWatch. These metrics include `TransformedLogEvents`, `TransformedBytes`, and `TransformationErrors`. For more information, see [Log transformer metrics and dimensions](CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md#CloudWatchLogs-Transformer-Metrics).

Whenever CloudWatch Logs tries and fails to transform a log event, it adds a `@transformationError` system field to that log event. When you run a CloudWatch Logs Insights query, you will see this field in all log events that had a transformation failure. You can query for this field with a query such as `filter ispresent(@transformationError)` to find all the failed transformation events.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
