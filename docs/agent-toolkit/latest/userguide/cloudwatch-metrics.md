---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/cloudwatch-metrics.html
---

# AWS MCP Server CloudWatch metrics
<a name="cloudwatch-metrics"></a>

AWS MCP Server automatically publishes metrics to Amazon CloudWatch at no additional cost. You can use these metrics to monitor usage patterns, track success rates, identify errors, and set up alarms for your AWS MCP Server operations.

## Metrics namespace
<a name="cloudwatch-metrics-namespace"></a>

All AWS MCP Server metrics are published under the `AWS-MCP` namespace in CloudWatch. Metrics are organized by tool name, allowing you to monitor which MCP tools you use most frequently (such as `aws___call_aws` or `aws___list_regions`) and track their success rates.

## Available metrics
<a name="available-metrics"></a>

The following metrics are available for AWS MCP Server. All metrics use standard resolution (1-minute granularity).

| Metric | Description | Unit |
| --- | --- | --- |
| `Invocation` | The number of times a tool was called, regardless of the response status. | Count |
| `Success` | The number of successful requests that returned a 200 response. | Count |
| `UserError` | The number of requests that failed with a 4XX client error (excluding throttles). | Count |
| `SystemError` | The number of requests that failed with a 5XX server error. | Count |
| `Throttle` | The number of requests that were throttled with a 429 response. | Count |

## Metric dimensions
<a name="metric-dimensions"></a>

Metrics include the following dimensions to help you filter and analyze your data:

**Tool Name**
The name of the specific MCP tool that was invoked. For example, `aws___call_aws`, `aws___list_regions`, or `aws___retrieve_skill`. For a complete list of available tools, see [Understanding the MCP Server tools](understanding-mcp-server-tools.md).

## Using metrics
<a name="using-metrics"></a>

You can use AWS MCP Server metrics to:

Monitor usage patterns
Track which tools you use most frequently to understand your interaction patterns with AWS services.

Identify errors
Monitor `UserError` and `SystemError` metrics to quickly detect and troubleshoot issues such as permission problems or service disruptions.

Track success rates
Calculate success rates by comparing `Success` counts to `Invocation` counts to ensure your operations are completing successfully.

Set up alarms
Create CloudWatch alarms to notify you when error rates exceed thresholds or when usage patterns change unexpectedly.

Optimize costs
Monitor invocation counts to identify inefficient usage patterns that might be increasing your AWS costs.

For more information about working with CloudWatch metrics, see [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in the *CloudWatch User Guide*.

## Example use cases
<a name="example-use-cases"></a>

The following examples show how you can use AWS MCP Server metrics:

Calculate success rate for API calls
Filter metrics by `Tool Name = aws___call_aws` and compare `Success` to `Invocation` to calculate your API call success rate. Set up an alarm to notify you if the success rate drops below 95%.

Detect permission issues
Monitor `UserError` metrics for specific tools. A spike in user errors often indicates IAM permission issues or incorrect API parameters.

Track tool usage trends
Compare `Invocation` counts across different tools over time to understand which AWS services and operations you interact with most frequently.

Monitor system health
Set up alarms for `SystemError` metrics to be notified of service disruptions or infrastructure issues that might affect your operations.

## Usage metrics
<a name="usage-metrics"></a>

AWS MCP Server publishes usage metrics to the `AWS/Usage` namespace in CloudWatch. These metrics help you monitor your resource consumption relative to your account quotas. You can use these metrics with the Service Quotas console to measure utilization and create alarms as you approach a quota.

All usage metrics include the following dimensions: `Type`, `Resource`, `Service`, and `Class`. The `Service` dimension is always `AWS MCP` and the `Class` dimension is always `None`.

| Metric name | Type | Resource | Description | Unit |
| --- | --- | --- | --- | --- |
| `CallCount` | API | Request | The number of requests made to the AWS MCP Server in this account in the current Region. | Count |
| `ResourceCount` | Resource | ConcurrentConnection | The number of concurrent connections per AWS account in the current Region. | Count |
| `ResourceCount` | Resource | AccountSessionCount | The number of concurrent active sessions per AWS account in the current Region. | Count |
| `ResourceCount` | Resource | UserSessionCount | The number of concurrent active sessions per user in this AWS account in the current Region. | Count |

**Note**
Requests that are throttled before reaching the AWS MCP Server are not reflected in the `CallCount` metric. As a result, the metric may not reliably report values above the throttling limit.

For more information about monitoring your usage and setting up alarms, see [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *CloudWatch User Guide* and [Service Quotas and Amazon CloudWatch](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html) in the *Service Quotas User Guide*.
