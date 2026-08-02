---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-mcp-limits.html
---

# Quotas for AWS MCP Server
<a name="aws-mcp-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for AWS MCP Server, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS MCP Server**.

To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

**Topics**
+ [Connection and session quotas](#connection-quotas)
+ [Throttling quotas](#throttling-quotas)
+ [Session limits](#session-limits)
+ [Monitoring your quotas](#monitoring-quotas)

## Connection and session quotas
<a name="connection-quotas"></a>

The following quotas apply to connections and sessions for AWS MCP Server.

| Quota | Default value | Adjustable | Description |
| --- | --- | --- | --- |
| Concurrent connections per account per Region | 27 | No | The maximum number of concurrent MCP connections per AWS account in a single Region. |
| Concurrent active sessions per account per Region | 180 | Yes | The maximum number of concurrent active sessions per AWS account in a single Region. |
| Concurrent active sessions per user per Region | 90 | Yes | The maximum number of concurrent active sessions per IAM user or role in a single Region. |

## Throttling quotas
<a name="throttling-quotas"></a>

The following quotas apply to request rates for AWS MCP Server. Requests that exceed these limits are throttled with a 429 response.

| Quota | Default value | Adjustable | Description |
| --- | --- | --- | --- |
| Requests per account per Region | 3 per second (sustained) | No | The maximum number of requests per second to the AWS MCP Server per AWS account in a single Region. |

## Session limits
<a name="session-limits"></a>

The following limits apply to individual sessions with AWS MCP Server. These limits are not adjustable.

| Limit | Value | Adjustable | Description |
| --- | --- | --- | --- |
| Maximum ephemeral storage retention | 8 hours | No | The maximum duration that ephemeral compute storage is retained for a session. After this time, ephemeral storage is reclaimed. |

## Monitoring your quotas
<a name="monitoring-quotas"></a>

AWS MCP Server publishes usage metrics to the `AWS/Usage` namespace in CloudWatch. You can use these metrics with the Service Quotas console to measure your utilization and create alarms as you approach a quota. The following usage metrics are available:
+ `CallCount` (Resource: `Request`) – The number of requests made to the AWS MCP Server
+ `ResourceCount` (Resource: `ConcurrentConnection`) – The number of concurrent connections
+ `ResourceCount` (Resource: `AccountSessionCount`) – The number of concurrent active sessions per account
+ `ResourceCount` (Resource: `UserSessionCount`) – The number of concurrent active sessions per user

For more information about these metrics, see [Usage metrics](cloudwatch-metrics.md#usage-metrics) in the [AWS MCP Server CloudWatch metrics](cloudwatch-metrics.md) section.

**Note**
Requests that are throttled before reaching the AWS MCP Server are not reflected in the `CallCount` metric. For more information about this limitation, see [Usage metrics](cloudwatch-metrics.md#usage-metrics).

For more information about monitoring your usage and setting up alarms, see [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *CloudWatch User Guide* and [Service Quotas and Amazon CloudWatch](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html) in the *Service Quotas User Guide*.
