---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-metrics-api.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business API operation metrics
<a name="qbusiness-metrics-api"></a>

The following table shows the API operation metrics that Amazon Q Business sends to CloudWatch.

| Metric name | Unit | Description |
| --- | --- | --- |
| `success` | Count | The number of successful API operation calls. This metric is emitted for each successful API operation execution.<br />Valid dimensions: `MethodType`, `ApplicationId` |
| `failure` | Count | The number of failed API operation calls. This metric is emitted for each failed API operation execution.<br />Valid dimensions: `MethodType`, `ApplicationId` |
| `latency` | Milliseconds | The time taken to complete an API operation call. This metric measures the response time for individual API operations.<br />Valid dimensions: `MethodType`, `ApplicationId` |

The `MethodType` dimension can include values such as:
+ `ListPlugins`
+ (Additional method types may be available depending on API usage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
